# Pull base image
FROM python:3.9.5-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src

# Install dependencies
COPY Pipfile Pipfile.lock /src/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /src/