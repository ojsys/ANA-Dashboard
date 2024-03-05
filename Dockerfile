# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip3 install poetry


# Copy the dependencies file to the working directory
COPY ./pyproject.toml /app/
COPY ./poetry.lock /app/

# Install dependencies using Poetry
RUN poetry install --no-root --no-interaction

# Copy the current directory contents into the container at /code/
COPY . /app/

# Collect static files
#RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django app on container startup
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
