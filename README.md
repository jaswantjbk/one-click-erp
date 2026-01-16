🚀 One-Click ERP System (Django)

A modular, admin-controlled ERP system built using Django, where ERP modules can be enabled or disabled with a single click from the admin panel — without changing code.

This project demonstrates real-world ERP architecture, modular design, and dynamic UI updates.

📌 Key Concept

Customize once in code → Manage everything from Admin → UI updates automatically

✨ Features

🔧 Modular ERP Architecture

Modules like Attendance, Inventory, HR, Student, etc.

Enable/Disable modules from Admin panel

🧠 One-Click ERP Logic

Changes in admin instantly reflect in UI

No hard-coded sidebar or dashboard links

📊 Inventory Management

Add inventory items (name, quantity, price)

View items in tabular UI

🧑‍💼 Attendance Management

Mark attendance (Present / Absent)

View attendance records in UI

🛠 Admin-Driven System

Django Admin used for full control

No coding required for daily operations

🎨 Reusable UI Layout

Base template with sidebar and navbar

Clean and extensible design

🏗️ Tech Stack

Backend: Django (Python)

Frontend: Django Templates, HTML, CSS, Bootstrap

Database: SQLite (development)

Version Control: Git & GitHub

📂 Project Structure
erp_project/
│
├── core/            # Dashboard, modules, context processor

├── attendance/      # Attendance module

├── inventory/       # Inventory module

├── templates/       # Base layout and module templates

├── manage.py

├── .gitignore

└── README.md

🔄 How the One-Click ERP Works

Admin enables/disables modules from Admin → Core → Modules

Module state is stored in database

Context processor fetches enabled modules

Sidebar and dashboard update automatically

User sees changes instantly in UI

✅ No UI hardcoding
✅ No page duplication
✅ Scalable design

▶️ How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/one-click-erp.git
cd one-click-erp

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows (PowerShell):

venv\Scripts\activate

4️⃣ Install Dependencies
pip install django

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Run Server
python manage.py runserver


Open in browser:

Dashboard: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

👨‍💻 Usage Guide

Admin Panel

Add / manage modules

Add inventory items

Add attendance records

User Interface

View enabled modules

Access inventory & attendance data

Changes reflect instantly based on admin settings

🎓 Learning Outcomes

Understanding ERP architecture

Modular Django app design

Admin-driven configuration

Context processors

Real-world backend + UI integration

🚀 Future Enhancements

Role-based authentication

CRUD operations from UI

Charts & analytics dashboard

Fees / Payroll modules

REST API integration

React frontend (optional)

📜 License

This project is licensed under the MIT License — free to use and modify for learning and development.

🙌 Author

Jaswant
B.Tech (ECE) | Python & Django Learner
Project built for skill development and ERP understanding.
