# ChefMatch

ChefMatch is an innovative platform that connects food enthusiasts with professional chefs for unique culinary experiences. This project provides a robust API for managing users, chefs, recipes, and bookings.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Setup](#setup)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview

ChefMatch aims to revolutionize the way people experience gourmet cooking. Our platform allows users to browse profiles of professional chefs, view their specialties and available dates, and book them for private cooking sessions or events.

## Features

- User management
- Chef profiles
- Booking system

## Project Structure
chefmatch/
│
├── chefmatch/            # Django project directory
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/                  # Django app directory
│   ├── migrations/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── pyproject.toml        # Poetry configuration file
├── poetry.lock
└── README.md

## Setup

1. Install [Python 3.12](https://www.python.org/downloads/)

1. Install [Poetry](https://python-poetry.org/docs/)

1. Install [Docker](https://docs.docker.com/desktop/)

1. Clone the repository
    ```sh
    git clone <repo-url>
    ```

1. Install Poetry if you haven't already:
   ```sh
   pip install poetry
   ```

1. Install project dependencies:
   ```sh
   poetry install
    ```
1. Apply migrations:
   ```sh
   poetry run python manage.py migrate
   ```

1. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

(Note: These are example endpoints. Adjust according to your actual implementation)

- `/api/users/`: User management
- `/api/chefs/`: Chef profiles
- `/api/bookings/`: Booking system

## Contributing

We welcome contributions to ChefMatch! Please follow these steps:

1. Fork the repository
2. Create your feature branch: 
    ```sh
    git checkout -b feature/AmazingFeature
    ```
3. Commit your changes: 
    ```sh
    git commit -m 'Add some AmazingFeature'
    ```
4. Push to the branch: 
    ```sh
    git push origin feature/AmazingFeature
    ```
5. Open a pull request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.