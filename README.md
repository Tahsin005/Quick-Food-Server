
# 🍔 Quick Food API


Welcome to the Quick Food API, the backend for an online food ordering platform built with Django Rest Framework. This repository contains the RESTful API that powers Quick Food, allowing users to browse restaurants, manage orders, and perform secure transactions.
## ✨ Features


- **✔ JWT Authentication** – Secure login & token-based authentication.
- **✔ Role-Based Access** – Users & restaurant owners have different access levels.
- **✔ Restaurant Management** – Restaurant owners can create, update, and manage restaurants & menu items.
- **✔ Order System** – Users can place & track orders, while owners manage order status.
- **✔ User Profiles** – API endpoints for registration, login, and profile.
- **✔ Search & Filtering **– Easily search and filter restaurants.
- **✔ Payment System** – Users can deposit money into their accounts.

## 🚀 Getting Started

1. Clone Repository: Clone this repository to your local machine using git clone https://github.com/Tahsin005/Quick-Food-Server.git

2. Install Dependencies: Navigate to the project directory and install the required dependencies using pip install -r requirements.txt.

3. Database Setup: Configure your database settings in the settings.py file. By default, the project is configured to use PostgreSQL, but you can change it to use SQLite or MySQL as per your preference.

4. Migrations: Run database migrations to create the necessary database schema using python manage.py migrate.

5. Create Superuser: Create a superuser account to access the Django admin panel and manage users, restaurants, menus and order listings using python manage.py createsuperuser.

6. Run Server: Start the Django development server using python manage.py runserver.

7. Explore API Endpoints: Explore the available API endpoints by navigating to http://127.0.0.1:8000/ in your web browser or API client.
## 🛠️ Technology used



**Backend:** Django REST API
<br/>
**Database:** PostgreSQL


## 📌 API Documentation

[Documentation](https://quick-food-server.onrender.com/swagger/)


## 🌍 Live API

[Live API](https://quick-food-server.onrender.com/)


