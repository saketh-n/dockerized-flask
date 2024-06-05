# Build stage
FROM python:3.9-slim AS build

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Final stage
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /app /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app/main.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
