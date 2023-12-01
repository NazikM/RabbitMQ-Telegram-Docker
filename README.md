# Project Setup and Configuration Guide
#### This guide provides instructions on setting up and configuring the project from the GitHub repository. The project includes a RabbitMQ service, a producer service, and a Telegram bot using the aiogram library.

## Prerequisites
#### Ensure you have the following prerequisites installed on your system:

1. Docker: Install Docker
2. Docker Compose: Install Docker Compose
3. Clone the GitHub repository to your local machine:


```bash
git clone https://github.com/NazikM/RabbitMQ-Telegram-Docker.git

cd RabbitMQ-Telegram-Docker
```

#### Configure RabbitMQ Service

Create .env file and set the environment variables. Example you can find in .env-example You can customize values for:
* AMQP_USER: username for RabbitMQ.
* AMQP_PASSWORD: Password for RabbitMQ.
* AMQP_ADDRESS: RabbitMQ server address.
* AMQP_VHOST: RabbitMQ virtual host.
* AMQP_PORT: Port to connect to RabbitMQ..
* EXTERNAL_API_URL: Where eto send post requests
* TELEGRAM_BOT_TOKEN: Token from telegram bot


Set the environment variables for the producer service section. You can customize values for AMQP_ADDRESS, AMQP_VHOST, AMQP_PORT, AMQP_USER, AMQP_PASSWORD, EXTERNAL_API_URL, and TELEGRAM_BOT_TOKEN.


## Build and Run the Services
#### Open a terminal in the project directory and run the following command:

```bash
Copy code
docker-compose up --build
```
This command will build the Docker images and start the RabbitMQ and producer services.

## Cleanup
#### To stop and remove the containers, run the following command in the project directory:

```bash
docker-compose down
```
This concludes the setup and configuration guide for the project. Customize the environment variables and adapt the code to suit your specific use case.