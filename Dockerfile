# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY poetry.lock pyproject.toml /code/

# Install dependencies using Poetry
RUN poetry install --no-root --no-interaction

# Copy the current directory contents into the container at /code/
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django app on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
