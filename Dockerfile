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

# Install dependencies using Poetry
RUN poetry install --no-root --no-interaction

# Stage 2: Production-ready image
FROM python:3.12-slim AS production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the application code from the builder stage
COPY --from=builder /app .

# Copy the rest of the application
COPY . .

# Collect static files (replace this with your own collectstatic command if needed)
# RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run Django app on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
