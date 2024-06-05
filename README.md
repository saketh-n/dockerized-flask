# Dockerized Flask Web Application

This is a simple Flask web application that is containerized using Docker. The application has one route (`/`) that returns a basic message.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Building and Running the Application

#### With Docker

1. Build the Docker image:

   ```sh
   docker build -t my_flask_app .
   ```

2. Run the Docker container:
   ```sh
   docker run -p 5000:5000 my_flask_app
   ```

#### With Docker Compose

1. Build and run the application:

   ```sh
   docker-compose up --build
   ```

2. Access the application at `http://localhost:5000`

### Stopping the Application

#### With Docker

1. Stop the running container (if needed):
   ```sh
   docker stop <container_id>
   ```

#### With Docker Compose

1. Stop the application:
   ```sh
   docker-compose down
   ```

### Enhancements

- Multi-stage builds
- Environment variables
- Best practices for a production-ready Docker setup
