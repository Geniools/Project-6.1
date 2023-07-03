FROM python:3.10.11
ENV PYTHONUNBUFFERED 1

RUN apt update -y
RUN apt install iputils-ping nano curl -y

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src

# Create the migrations
RUN python manage.py makemigrations --skip-checks
