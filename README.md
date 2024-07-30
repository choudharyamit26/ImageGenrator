# Django Application with Celery and Redis

This project is a Django application configured to use Celery for asynchronous tasks and Redis as the message broker. The application is containerized using Docker, and Docker Compose is used to manage the multi-container setup.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to get the application up and running locally:

1.**Clone the Repository**

   ```bash
   git clone https://github.com/choudharyamit26/ImageGenrator/new/master
   cd image_generator
   ```
2. **Create .env file**
  SECRET_KEY=your_secret_key
  DEBUG=True
  ALLOWED_HOSTS=localhost,127.0.0.1

3. **Build and Start the Containers**
```bash
  docker-compose up --build
```
4. **Access the Application**
```bash
 http://127.0.0.1:8000
```
5. **Create Superuser: To create a Django superuser, use**
```bash
docker-compose run web python manage.py createsuperuser
```


