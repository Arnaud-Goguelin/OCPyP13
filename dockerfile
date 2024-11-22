# ----------------------------------------------------------------------
# --- BASE STAGE ---
# ----------------------------------------------------------------------


# use --platform linux/amd64 to ensure compatibility with the architecture x86-64.
# use -slim to reduce the size of the image
FROM --platform=linux/amd64 python:3.12.3-slim as base

# Set environment variables
# This force Python to write to logs in real-time (no logs stored in a buffer)
ENV PYTHONUNBUFFERED=1
# This prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

# create a directory for the project and work in it
RUN mkdir -p /app /data
WORKDIR /app

# Install system dependencies and Python
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
# use --mount=type=cache to cache the dependencies and make the build faster
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip \
    && pip install -r requirements.txt \
    # Remove build dependencies to gain space
    && apt-get remove -y build-essential \
    && apt-get autoremove -y

# Create a non-root user (better security)
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd -g $GROUP_ID appgroup && \
    useradd -g $GROUP_ID -m appuser && \
    # owner can write, read and execute files in the app directory
    # others can read and execute only
    chmod -R 755 /app && \
    # owner can read, write and execute files in the data directory
    # others can't do anything
    chmod -R 700 /data

# Switch to the non-root user
# thus /app and /data owner is root user and they won't be modified by appuser

# ----------------------------------------------------------------------
# --- DEV STAGE ---
# ----------------------------------------------------------------------

FROM base as dev
# Copy project files
COPY . /app/
# in dev user should be able to modify the app
ENV ENVIRONMENT=development
CMD ["sleep", "infinity"]

# ----------------------------------------------------------------------
# --- PROD STAGE ---
# ----------------------------------------------------------------------
FROM base as prod
USER appuser
# Set environment variables
ENV ENVIRONMENT=production
ENV DJANGO_ALLOWED_HOSTS=*
# be sure to set the debug mode to False
ENV DJANGO_DEBUG=False

# Copy project files
COPY . /app/

# Collect static files for Django app
RUN ./manage.py collectstatic --noinput --clear

# Configure Gunicorn
COPY gunicorn.conf.py /app/gunicorn.conf.py

EXPOSE 8000

# Run the Django app with Gunicorn
# Entrypoint is the command that will be executed when the container starts
# reminder : in this case CMD would the args passed to ENTRYPOINT (but everything is in gunicorn.conf.py)
ENTRYPOINT ["gunicorn", "oc_lettings_site.wsgi:application", "-c", "/app/gunicorn.conf.py"]
# CMD are the args passed to the entrypoint
