# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the dependencies files
COPY pyproject.toml poetry.lock requirements.txt /app/

# Install dependencies using Poetry
RUN poetry export --without-hashes -f requirements.txt > requirements-poetry.txt \
    && pip install --no-cache-dir -r requirements.txt -r requirements-poetry.txt

# Copy the rest of the application
COPY . .

# Collect static files (replace this with your own collectstatic command if needed)
# RUN poetry run python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django app on container startup
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
