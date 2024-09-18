FROM python:3.9-slim

RUN pip install flask numpy

COPY . /app

EXPOSE 5000

WORKDIR /app

# Command to run the Flask app with python
CMD ["python3", "app.py"]
