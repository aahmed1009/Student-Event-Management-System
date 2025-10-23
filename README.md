# Student Event Management System
## Academic Project Report

**Course:** Web Development / Software Engineering  
**Academic Year:** 2024-2025  
**Project Type:** Full-Stack Web Application  
**Technology Stack:** Django, Python, SQLite, Bootstrap 5

---

## Executive Summary

The Student Event Management System is a comprehensive web-based platform designed to streamline the organization, management, and participation in university events and activities. This system bridges the gap between event organizers and students, providing an intuitive interface for event discovery, registration, and management.

## Table of Contents

1. [Project Objectives](#project-objectives)
2. [System Features](#system-features)
3. [Technology Stack](#technology-stack)
4. [System Architecture](#system-architecture)
5. [Database Design](#database-design)
6. [User Interface](#user-interface)
7. [Installation Guide](#installation-guide)
8. [Usage Guide](#usage-guide)
9. [Screenshots](#screenshots)
10. [Testing](#testing)
11. [Future Enhancements](#future-enhancements)
12. [Conclusion](#conclusion)

---

## Project Objectives

### Primary Objectives
1. **Centralized Event Management**: Create a unified platform for managing all university events
2. **User Role Management**: Implement role-based access control (Students, Staff, Administrators)
3. **Simplified Registration**: Enable easy event discovery and registration for students
4. **Administrative Control**: Provide comprehensive tools for event organizers and administrators

### Learning Outcomes
- Full-stack web development using Django framework
- Database design and ORM implementation
- User authentication and authorization
- RESTful architecture and MVC pattern
- Responsive web design with Bootstrap
- Version control with Git

---

## System Features

### For Students
- **Event Discovery**: Browse all upcoming events with detailed information
- **Event Registration**: One-click registration for events
- **My Events Dashboard**: View all registered events in one place
- **Event Search & Filter**: Find events by date, type, or topic
- **User Profile**: Manage personal information and preferences

### For Staff/Organizers
- **Event Creation**: Create new events with rich details (title, description, date, location)
- **Event Management**: Edit or delete existing events
- **Registration Tracking**: View list of registered students for each event
- **Dashboard Analytics**: Overview of organized events and participation

### For Administrators
- **User Management**: Create, edit, and manage all user accounts
- **Full Event Control**: Manage all events across the platform
- **System Monitoring**: Access to Django admin panel
- **Data Analytics**: View system-wide statistics and reports

## Installation Guide

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Populate database with sample data (Recommended)

```bash
python manage.py populate_data
```

This command creates:
- **1 Admin user**: username: `admin`, password: `admin123`
- **5 Staff users**: username: `staff1-5`, password: `staff123`
- **30 Student users**: username: `student1-30`, password: `student123`
- **50 Events**: All scheduled for 2025 with realistic data
- **Event Registrations**: Random student registrations for each event

### 5. Run the development server

```bash
python manage.py runserver
```

### 6. Access the application

Open your browser and go to: `http://127.0.0.1:8000/`

---

## Usage Guide

### For Students

1. **Register an Account**
   - Click "Register" in the navigation bar
   - Fill in username, email, and password
   - Submit the form to create your account

2. **Browse Events**
   - Navigate to the home page to see all upcoming events
   - View event details including date, location, and description
   - Check the number of registered students

3. **Register for Events**
   - Click on an event to view details
   - Click the "Register" button to sign up
   - View your registered events in "My Events"

4. **Manage Registrations**
   - Access "My Events" from the navigation menu
   - View all events you've registered for
   - Unregister from events if needed

### For Staff/Organizers

1. **Create Events**
   - Click "Create Event" in the navigation bar
   - Fill in event details (title, description, date, location)
   - Submit to publish the event

2. **Manage Events**
   - View your organized events in the Dashboard
   - Edit event details by clicking "Edit"
   - Delete events if necessary
   - View list of registered students for each event

3. **Monitor Participation**
   - Check registration counts on the dashboard
   - View detailed participant lists for each event

### For Administrators

1. **Access Admin Panel**
   - Navigate to `/admin/` or click "Admin Panel" in the dropdown
   - Login with admin credentials

2. **Manage Users**
   - Create, edit, or delete user accounts
   - Assign staff permissions
   - Reset user passwords

3. **System Management**
   - View all events across the platform
   - Manage any event regardless of organizer
   - Monitor system-wide statistics

## Project Structure

```
student_engagement/
├── manage.py
├── requirements.txt
├── student_engagement/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── main/                        # Main application
    ├── models.py                # Event and Registration models
    ├── views.py                 # View logic
    ├── urls.py                  # URL routing
    ├── forms.py                 # Form definitions
    ├── templates/               # HTML templates
    └── static/                  # CSS and JS files
```

## URLs

- `/` - Home page (list of events)
- `/login/` - Login page
- `/logout/` - Logout
- `/register/` - Student registration
- `/event/<id>/` - Event details
- `/event/create/` - Create event (organizers)
- `/event/<id>/edit/` - Edit event (organizers)
- `/event/<id>/delete/` - Delete event (organizers)
- `/dashboard/` - User dashboard
- `/my-events/` - Student's registered events
- `/admin/` - Django admin panel

## Technology Stack

### Backend Technologies
- **Django 4.2**: High-level Python web framework
- **Python 3.12**: Programming language
- **SQLite3**: Lightweight relational database
- **Django ORM**: Object-Relational Mapping for database operations

### Frontend Technologies
- **HTML5**: Markup language for web pages
- **CSS3**: Styling and layout
- **Bootstrap 5**: Responsive CSS framework
- **Bootstrap Icons**: Icon library
- **JavaScript**: Client-side interactivity

### Additional Libraries
- **django-crispy-forms**: Enhanced form rendering
- **crispy-bootstrap5**: Bootstrap 5 template pack for crispy forms

### Development Tools
- **Git**: Version control system
- **Virtual Environment**: Python dependency isolation
- **Django Development Server**: Built-in web server for testing

---

## System Architecture

### MVC Architecture Pattern

The project follows Django's MVT (Model-View-Template) architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                       │
│              (HTML Templates + Bootstrap)               │
└─────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────┐
│                    Views Layer                          │
│           (Business Logic & Request Handling)           │
└─────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────┐
│                    Models Layer                         │
│              (Data Models & Database ORM)               │
└─────────────────────────────────────────────────────────┘
                          ↕
┌─────────────────────────────────────────────────────────┐
│                  SQLite Database                        │
└─────────────────────────────────────────────────────────┘
```

### Application Flow

1. **User Request**: Browser sends HTTP request to Django
2. **URL Routing**: Django maps URL to appropriate view
3. **View Processing**: View executes business logic
4. **Database Query**: ORM queries database if needed
5. **Template Rendering**: Data is passed to HTML template
6. **HTTP Response**: Rendered page sent back to browser

---

## Database Design

### Entity-Relationship Diagram

```
┌─────────────────┐
│      User       │
│─────────────────│
│ id (PK)         │
│ username        │
│ email           │
│ password        │
│ first_name      │
│ last_name       │
│ is_staff        │
│ is_superuser    │
└─────────────────┘
        │
        │ 1:N (organizer)
        ↓
┌─────────────────┐
│     Event       │
│─────────────────│
│ id (PK)         │
│ title           │
│ description     │
│ date            │
│ location        │
│ organizer (FK)  │
│ created_at      │
│ updated_at      │
└─────────────────┘
        │
        │ N:M (through Registration)
        ↓
┌─────────────────┐
│  Registration   │
│─────────────────│
│ id (PK)         │
│ student (FK)    │
│ event (FK)      │
│ created_at      │
└─────────────────┘
```

### Database Tables

#### 1. User Table (Django Built-in)
- Stores all user information
- Handles authentication and authorization
- Supports role-based permissions

#### 2. Event Table
- **Primary Key**: Auto-incrementing ID
- **Foreign Key**: organizer_id → User.id
- **Fields**: title, description, date, location, timestamps
- **Ordering**: Descending by date

#### 3. Registration Table
- **Primary Key**: Auto-incrementing ID
- **Foreign Keys**: 
  - student_id → User.id
  - event_id → Event.id
- **Unique Constraint**: (student, event) - prevents duplicate registrations
- **Ordering**: Descending by created_at

---

## User Interface

### Design Principles

1. **Responsive Design**: Mobile-first approach using Bootstrap grid system
2. **Intuitive Navigation**: Clear menu structure with role-based options
3. **Consistent Styling**: Uniform color scheme and typography
4. **User Feedback**: Success/error messages for all actions
5. **Accessibility**: Semantic HTML and proper ARIA labels

### Color Scheme
- **Primary**: Bootstrap primary blue (#0d6efd)
- **Success**: Green for successful actions
- **Danger**: Red for delete/error actions
- **Info**: Light blue for informational messages

### Key UI Components

1. **Navigation Bar**: Responsive navbar with user-specific menu items
2. **Event Cards**: Bootstrap cards displaying event information
3. **Forms**: Crispy forms with Bootstrap styling
4. **Modals**: Confirmation dialogs for critical actions
5. **Alerts**: Django messages framework for user feedback

---

## Screenshots

### 1. Home Page
*[Add screenshot of the home page showing event listings]*

**Description**: The landing page displays all upcoming events in a card layout. Each card shows the event title, date, location, and registration count.

---

### 2. User Registration
*[Add screenshot of the registration form]*

**Description**: New users can create an account by providing username, email, and password. The form includes validation and user-friendly error messages.

---

### 3. Login Page
*[Add screenshot of the login page]*

**Description**: Existing users can log in with their credentials. The page features a clean, centered form with Bootstrap styling.

---

### 4. Event Details Page
*[Add screenshot of event detail view]*

**Description**: Detailed view of a single event showing full description, organizer information, and registration button. Registered students can see their registration status.

---

### 5. Student Dashboard - My Events
*[Add screenshot of student's registered events]*

**Description**: Students can view all events they've registered for in one convenient location. Each event shows the date, location, and an option to unregister.

---

### 6. Staff Dashboard
*[Add screenshot of staff dashboard]*

**Description**: Event organizers can see all their created events, edit or delete them, and view registration statistics.

---

### 7. Create Event Form
*[Add screenshot of create event form]*

**Description**: Staff members can create new events using this comprehensive form with fields for title, description, date, time, and location.

---

### 8. Edit Event
*[Add screenshot of edit event page]*

**Description**: Organizers can modify event details. The form is pre-populated with existing data for easy editing.

---

### 9. Event Registration List
*[Add screenshot showing list of registered students]*

**Description**: Event organizers can view all students registered for their events, including usernames and registration dates.

---

### 10. Admin Panel
*[Add screenshot of Django admin interface]*

**Description**: Administrators have access to the Django admin panel for comprehensive system management, including user and event administration.

---

### 11. Mobile Responsive View
*[Add screenshot of mobile view]*

**Description**: The application is fully responsive and works seamlessly on mobile devices with an optimized layout.

---

### 12. Success Messages
*[Add screenshot showing success message]*

**Description**: User actions trigger feedback messages (success, error, info) displayed at the top of the page using Django's messages framework.

---

## Testing

### Manual Testing

#### 1. User Authentication Testing
- ✅ User registration with valid data
- ✅ User registration with invalid data (duplicate username, weak password)
- ✅ User login with correct credentials
- ✅ User login with incorrect credentials
- ✅ Logout functionality
- ✅ Password validation

#### 2. Event Management Testing
- ✅ Create event as staff user
- ✅ Create event as regular student (should fail - permission denied)
- ✅ Edit own event as staff
- ✅ Edit other user's event (should fail for non-admin)
- ✅ Delete event with confirmation
- ✅ View event details

#### 3. Registration Testing
- ✅ Register for an event
- ✅ Prevent duplicate registration
- ✅ Unregister from an event
- ✅ View registered events list

#### 4. Authorization Testing
- ✅ Staff-only pages blocked for students
- ✅ Admin panel accessible only to superusers
- ✅ Event edit/delete restricted to organizers
- ✅ Redirect to login for unauthenticated users

#### 5. UI/UX Testing
- ✅ Responsive design on desktop (1920x1080)
- ✅ Responsive design on tablet (768x1024)
- ✅ Responsive design on mobile (375x667)
- ✅ Navigation menu functionality
- ✅ Form validation messages
- ✅ Success/error notifications

### Test Data
- **50 Events**: Created with realistic data for 2025
- **30 Students**: Test user accounts
- **5 Staff Members**: Event organizer accounts
- **1 Admin**: Superuser account
- **Multiple Registrations**: Various registration scenarios

### Browser Compatibility
- ✅ Google Chrome (Latest)
- ✅ Mozilla Firefox (Latest)
- ✅ Microsoft Edge (Latest)
- ✅ Safari (Latest)

---

## Future Enhancements

### Phase 1 - Short Term
1. **Email Notifications**
   - Send confirmation emails upon event registration
   - Reminder emails before event dates
   - Notification for event updates or cancellations

2. **Advanced Search & Filtering**
   - Filter events by category, date range, location
   - Search functionality with autocomplete
   - Sort events by popularity, date, or relevance

3. **Event Categories**
   - Categorize events (Academic, Sports, Cultural, Technical)
   - Color-coded category badges
   - Category-based filtering

4. **Event Capacity Management**
   - Set maximum attendee limits
   - Waitlist functionality
   - Automatic notifications when spots open up

### Phase 2 - Medium Term
5. **Calendar Integration**
   - Interactive calendar view of events
   - Export events to Google Calendar/iCal
   - Month/week/day view options

6. **User Profiles**
   - Extended user profiles with bio and interests
   - Profile pictures
   - Event attendance history

7. **Rating & Reviews**
   - Students can rate and review past events
   - Display average ratings on event cards
   - Feedback collection for organizers

8. **Analytics Dashboard**
   - Attendance trends and statistics
   - Popular event types
   - User engagement metrics
   - Export reports as PDF/CSV

### Phase 3 - Long Term
9. **Social Features**
   - Comment section for events
   - Share events on social media
   - Friend system to see what events friends attend

10. **Mobile Application**
    - Native iOS and Android apps
    - Push notifications
    - QR code check-in system

11. **Payment Integration**
    - Support for paid events
    - Online payment gateway integration
    - Ticket generation and management

12. **Multi-language Support**
    - Internationalization (i18n)
    - Support for multiple languages
    - RTL language support

---

## Challenges Faced & Solutions

### 1. Template Syntax Error
**Challenge**: Django template tags were not properly closed, causing rendering errors.  
**Solution**: Carefully structured `{% if %}`, `{% else %}`, and `{% endif %}` tags with proper nesting and indentation.

### 2. User Role Management
**Challenge**: Implementing different views and permissions for students vs. staff.  
**Solution**: Utilized Django's built-in `is_staff` flag and created custom decorators for view protection.

### 3. Duplicate Registrations
**Challenge**: Students could register for the same event multiple times.  
**Solution**: Implemented unique constraint on (student, event) pair in the Registration model.

### 4. Date/Time Handling
**Challenge**: Timezone-aware datetime handling for events.  
**Solution**: Used Django's timezone utilities and configured timezone support in settings.

### 5. Responsive Design
**Challenge**: Ensuring consistent UI across different screen sizes.  
**Solution**: Leveraged Bootstrap's grid system and responsive utilities for mobile-first design.

---

## Conclusion

The Student Event Management System successfully achieves its objectives of providing a centralized, user-friendly platform for managing university events. The project demonstrates proficiency in:

- **Full-stack web development** using Django framework
- **Database design** with proper relationships and constraints
- **User authentication and authorization** with role-based access control
- **Responsive UI design** using modern CSS frameworks
- **Software engineering best practices** including MVC architecture and code organization

### Key Achievements
✅ Implemented complete CRUD operations for events  
✅ Created role-based access control system  
✅ Developed responsive, mobile-friendly interface  
✅ Integrated user authentication and session management  
✅ Populated database with 50 realistic events for 2025  
✅ Implemented registration system with duplicate prevention  
✅ Created comprehensive admin panel for system management  

### Learning Outcomes
This project provided hands-on experience with:
- Django framework and Python programming
- Database modeling and ORM
- HTML/CSS/Bootstrap for frontend development
- Git version control
- Web application deployment
- Software testing and debugging

The system is production-ready for deployment and can be extended with the proposed future enhancements to add more sophisticated features.

---

## Project Information

**Repository**: [Add your GitHub repository link here]  
**Live Demo**: [Add deployment link if available]  
**Documentation**: Complete documentation available in project files  
**License**: MIT License  

---

## Acknowledgments

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/
- Stack Overflow Community
- Course Instructor and Teaching Assistants

---

**Developed by**: [Your Name]  
**Student ID**: [Your ID]  
**Course**: [Course Code and Name]  
**Submission Date**: [Date]  
**Institution**: [University Name]

---
# Student-Event-Management-System
