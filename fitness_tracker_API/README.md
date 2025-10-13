🏋️‍♂️ Fitness Tracker API

📌 Project Overview

The Fitness Tracker API is a backend system built with Django and Django REST Framework (DRF) that allows users to manage and track their fitness activities.
Users can log, update, delete, and view their activity history while tracking performance metrics such as calories burned, total duration, and distance covered.

This project simulates a real-world backend application focusing on database management, user authentication, and activity tracking.

🚀 Features
** Activity Management (CRUD) **
- Create, Read, Update, and Delete fitness activities.
- Each activity includes:
    * Activity Type (e.g., Running, Cycling, Weightlifting)
    * Duration (minutes)
    * Distance (km/miles)
    * Calories Burned
    * Date
    * User ID (owner)
- Validations for required fields (Activity Type, Duration, Date).

** User Management (CRUD) **
- Users can register, update profiles, and delete accounts.
- Each user has:
    * Username
    * Email
    * Password
- Users can only manage their own activities.
- Permissions prevent users from modifying or deleting activities of others.

** Activity History **
- Endpoint to view all logged activities by the user.
- Optional filters:
    * By Date Range
    * By Activity Type

** Activity Metrics **
- Summary endpoint showing:
    * Total duration of activities
    * Total distance covered
    * Total calories burned
- Optional activity trends (weekly/monthly tracking).

** Ntifications and Reminders **
- A notification system that reminds users to log their activities or alerts them when they achieve specific fitness goals.

** Additional Features **
- Pagination for long activity histories.
- Sorting by Date, Duration, or Calories Burned.


🛠️ Technical Stack
- Backend: Django, Django REST Framework (DRF)
- Database: SQLite (development), PostgreSQL (production)
- Authentication: Django Authentication + JWT (optional)
- Deployment: PythonAnywhere

🔑 Authentication
- Users must sign up and log in before performing actions.
- Endpoints are secured; only authenticated users can create, update, or delete activities.
- JWT authentication available for enhanced security.

⚙️ Installation & Setup

1. Clone the Repository
    - git clone https://github.com/yourusername/forme-physique.git
    - cd forme-physique
    - cd fitness_tracker_API

2. Create Virtual Environment
    - python -m venv venv
    - source venv/bin/activate   # On Linux/Mac
    - venv\Scripts\activate      # On Windows

3. Install Dependencies
    - pip install -r requirements.txt

4. Run Migrations
    - python manage.py makemigrations
    - python manage.py migrate

5. Create Superuser
    - python manage.py createsuperuser

6. Run Development Server
    - python manage.py runserver

7. Access API
    - Base URL: https://stinger969.pythonanywhere.com/

*** API ENDPOINTS ***

User Authentication
** Registration of a user **

POST /api/auth/register/
Request Body:
{
  "username": "methusella",
  "email": "meth@gmail.com",
  "password": "meth123"
}

** User Login **

POST /api/auth/login/
Request Body:
{
  "email": "john@example.com",
  "password": "strongpassword123"
}

** User Logout **

{
    "refresh": "refresh_token"
}

Activities
** Create Activity **

POST /api/activities/
Request Body:
{
  "activity_type": "Running",
  "duration": 45,
  "distance": 10.5,
  "calories_burned": 450,
  "date": "2025-10-09"
}

** Get All Activities **

GET /api/activities/

** Get Single Activity **
GET /api/acitivities/<id>/

** Update Activity **

PUT /api/activities/<id>/
Request Body:
{
  "activity_type": "Cycling",
  "duration": 60,
  "distance": 15.0,
  "calories_burned": 600,
  "date": "2025-10-09"
}

** Delete Activity **

DELETE /api/activities/<id>/

** Metrics **

GET /api/activities/metrics/

** Notifications **

GET /api/notifications/notifications/


📄 License

This project is licensed under the MIT License – you are free to use and modify it.