# Stage 1: Build the application
FROM python:3.12 AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip3 install poetry

# Set the working directory
WORKDIR /app

# Copy the dependencies files
COPY pyproject.toml poetry.lock /app/
COPY requirements.txt /app/

# Install dependencies using Poetry
#RUN poetry install --no-root --no-interaction

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

# Install dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Stage 2: Production-ready image
FROM python:3.12-slim AS production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the application code from the builder stage
COPY --from=builder /app .

## Activate the virtual environment
#ENV VIRTUAL_ENV=/venv
#RUN python -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the rest of the application
COPY . .

# Collect static files (replace this with your own collectstatic command if needed)
# RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run Django app on container startup
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
