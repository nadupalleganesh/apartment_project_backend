 Apartment Management System – Backend
 Overview
This is the backend API for the Apartment Management System, developed using Python Flask and PostgreSQL.
The system supports user authentication, apartment units, bookings, amenities, and admin approvals with JWT-based authentication.
This project demonstrates real-world backend architecture, REST APIs, role-based access flow, and database design.

Tech Stack

Backend Framework: Flask

Authentication: JWT (flask-jwt-extended)

Database: PostgreSQL

ORM: SQLAlchemy

API Style: REST

CORS: Flask-CORS

Project Structure
apartment_backend/
│── backend/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│
│── models/
│   ├── user.py
│   ├── tower.py
│   ├── unit.py
│   ├── amenity.py
│   ├── booking.py
│
│── routes/
│   ├── auth.py
│   ├── user.py
│   ├── admin.py
│
│── venv/
│── requirements.txt
│── README.md

 Authentication Flow

Register → Create new user

Login → Generate JWT Access Token

Protected APIs → Access using Bearer Token

JWT is used to secure User and Admin APIs.

 API Endpoints
 Authentication
Method	Endpoint	Description
POST	/auth/register	Register user
POST	/auth/login	Login & get JWT

User APIs (Resident)
Method	Endpoint	Description
GET	/user/units	View available units
POST	/user/book	Book a unit

 Admin APIs
Method	Endpoint	Description
GET	/admin/bookings	View all bookings
PUT	/admin/booking/<id>/approve	Approve booking

Database Models

User – residents & admins

Tower – apartment towers

Unit – flats under towers

Amenity – facilities

Booking – unit booking records

Tables are auto-created using:

db.create_all()

▶️ How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Database

Update PostgreSQL details in config.py.

4️⃣ Run Server
python -m backend.app


Server runs at:

http://127.0.0.1:5000/

 Testing

APIs can be tested using Postman

JWT-protected routes require Authorization: Bearer <token>

(Postman usage is optional; focus is on backend architecture and logic.)

 Key Highlights

✔ Modular Flask architecture
✔ JWT Authentication
✔ Clean REST APIs
✔ Real-world database models
✔ Scalable project structure

 Developer

Ganesh Sharma
Python Full Stack Developer
(Django | Flask | REST APIs | Angular)
