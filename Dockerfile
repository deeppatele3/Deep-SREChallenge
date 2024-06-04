
FROM python
WORKDIR /app
COPY . /app


RUN pip install --no-cache-dir flask

# Expose the port Flask runs on
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]