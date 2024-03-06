# Stage 1: Build environment
FROM python:3.12-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        curl \
        sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry via pip
RUN pip install poetry

# Set working directory in the builder stage
WORKDIR /app

# Copy only the poetry.lock/pyproject.toml to leverage Docker cache
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Set up virtual environment
ENV VIRTUAL_ENV=/app/env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the Django project into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Collect static files
#RUN python manage.py collectstatic --noinput

# Run the Django app
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]