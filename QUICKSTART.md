# Quick Start Guide

## Option 1: Automated Setup (Recommended)

Run the setup script:

```bash
chmod +x setup.sh
./setup.sh
```

Then start the server:

```bash
source venv/bin/activate
python manage.py runserver
```

## Option 2: Manual Setup

### Step 1: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Sample Data

```bash
python manage.py create_sample_data
```

This creates:
- **Admin**: username: `admin`, password: `admin123`
- **Organizer**: username: `organizer`, password: `organizer123`
- **Student**: username: `student`, password: `student123`
- Sample events and registrations

### Step 5: Run Server

```bash
python manage.py runserver
```

### Step 6: Access Application

Open your browser to: **http://127.0.0.1:8000/**

## Testing the Application

### As a Student:
1. Login with: `student` / `student123`
2. Browse events on the home page
3. Click "View Details" on any event
4. Click "Register for Event"
5. View your registered events at "My Events"

### As an Organizer:
1. Login with: `organizer` / `organizer123`
2. Go to "Dashboard"
3. Click "Create New Event"
4. Fill in event details and submit
5. View registered students for your events

### As an Admin:
1. Login with: `admin` / `admin123`
2. Access Django admin panel at: http://127.0.0.1:8000/admin/
3. Manage all users and events
4. View all events in the dashboard

## Project Structure

```
student_engagement/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                    # Full documentation
├── QUICKSTART.md               # This file
├── setup.sh                    # Automated setup script
├── student_engagement/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── main/                       # Main application
    ├── models.py               # Event & Registration models
    ├── views.py                # View logic
    ├── urls.py                 # URL routing
    ├── forms.py                # Form definitions
    ├── admin.py                # Admin configuration
    ├── templates/              # HTML templates
    │   └── main/
    │       ├── base.html
    │       ├── index.html
    │       ├── login.html
    │       ├── register.html
    │       ├── event_detail.html
    │       ├── dashboard.html
    │       ├── my_events.html
    │       ├── create_event.html
    │       ├── edit_event.html
    │       ├── delete_event.html
    │       └── event_registrations.html
    ├── static/                 # CSS & JS files
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       └── script.js
    └── management/             # Custom commands
        └── commands/
            └── create_sample_data.py
```

## Features

✅ User authentication (login/logout/register)
✅ Three user roles: Student, Organizer, Admin
✅ Event browsing and details
✅ Student event registration
✅ Organizer event management (CRUD)
✅ Admin panel for full control
✅ Responsive Bootstrap UI
✅ Registration confirmations
✅ "My Events" page for students

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'django'`
**Solution**: Make sure virtual environment is activated and dependencies are installed

**Issue**: Database errors
**Solution**: Run migrations: `python manage.py migrate`

**Issue**: Static files not loading
**Solution**: Run: `python manage.py collectstatic` (for production)

## Next Steps

- Customize the UI in `main/templates/`
- Modify styles in `main/static/css/style.css`
- Add more features in `main/views.py`
- Configure email notifications
- Deploy to production server

Enjoy your Student Engagement Platform! 🎓
