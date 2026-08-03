# 🏥 Hospital Management System  
### Full Stack Web Application for Healthcare Management

A complete Hospital Management System built using Python and Web Technologies to manage patients, doctors, appointments, and administrative operations efficiently.

---

## Abstract of the Project

The healthcare industry requires efficient systems to manage patient data, doctor availability, and hospital operations.

This project provides a centralized system where:

- Patients can register and book appointments  
- Doctors can manage schedules and view patient details  
- Admin can monitor overall hospital activities  

The system ensures better data organization, faster access, and improved healthcare service delivery.

---

## Objectives

- Digitize hospital management processes  
- Manage patient records efficiently  
- Enable doctor-patient interaction  
- Improve hospital workflow and data tracking  

---

## System Modules

### Admin Module
- Manage doctors  
- View all patients  
- Monitor appointments  
- System overview dashboard  

---

### Doctor Module
- View assigned patients  
- Update patient records  
- Manage appointments  
- Track treatment details  

---

### Patient Module
- Register/Login  
- Book appointments  
- View prescriptions  
- Track medical history  

---

## Application Flow


User Login (Admin / Doctor / Patient)
↓
Dashboard Access
↓
Perform Operations
↓
Database Update
↓
Real-Time Data Management


---

## Project Structure


HospitalManagementSystem/
│
├── static/
│ ├── css/
│ ├── js/
│ └── images/
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── dashboard.html
│ ├── patient.html
│ ├── doctor.html
│ └── admin.html
│
├── app.py
├── models.py
├── database.db
├── requirements.txt
└── README.md


---

## Application Screenshots

### Home Page

<p align="center">
  <img src="screenshots/home.jpg" width="700"/>
</p>

---

### Login Page

<p align="center">
  <img src="screenshots/login.jpg" width="700"/>
</p>

---

### Dashboard

<p align="center">
  <img src="screenshots/dashboard.jpg" width="700"/>
</p>

---

### Doctor Panel

<p align="center">
  <img src="screenshots/doctor.jpg" width="700"/>
</p>

---

### Patient Panel

<p align="center">
  <img src="screenshots/patient.jpg" width="700"/>
</p>

---

## Technologies Used

### Backend
- Python  
- Flask / Django  

### Database
- SQLite / MySQL  

### Frontend
- HTML  
- CSS  
- JavaScript  

---

## Installation

Clone repository:

```bash
git clone <your-repo-link>
cd HospitalManagementSystem

Create virtual environment:

python -m venv .venv

Activate:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Run Application
python app.py

Open browser:

http://127.0.0.1:5000
Key Features
Multi-user login system
Patient record management
Appointment scheduling
Doctor dashboard
Admin control panel
Secure data handling
Future Improvements
Add online payment system
Integrate real-time notifications
Cloud deployment
AI-based diagnosis support
Mobile app integration
Disclaimer

This project is developed for educational purposes only.
