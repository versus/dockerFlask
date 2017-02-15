FROM alpine:latest

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask
RUN pip install Flask-Script

# Bundle app source
COPY manage.py /src/manage.py

EXPOSE  8000
CMD ["python", "/src/manage.py", "runserver", "-h 0.0.0.0", "-p 8000"]
