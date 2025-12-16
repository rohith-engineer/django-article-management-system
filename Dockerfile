# Use Python slim image
FROM python:3.12-slim

# Prevent Python buffering
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy project files (first only pyproject to optimize caching)
COPY pyproject.toml poetry.lock /code/

# Copy all source code
COPY . /code/

# Give execute permissions to /code directory and start-django.sh
RUN chmod 755 /code /code/start-django.sh

# Disable virtualenv creation + install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose Django port
EXPOSE 8000

# Use start-django.sh as entrypoint
ENTRYPOINT ["/code/start-django.sh"]
