FROM python:3.11
LABEL authors="Alexandru"
ENV PYTHONUNBUFFERED 1

RUN apt update -y
RUN apt install iputils-ping -y

# Copy the current directory contents into the container at /app
COPY . .

RUN mv /example_local_settings.py /src/sports_accounting/local_settings.py
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src

# Run the migrations
RUN python manage.py makemigrations --skip-checks
#RUN python manage.py migrate --skip-checks

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]