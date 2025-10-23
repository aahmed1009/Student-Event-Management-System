from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Event, Registration
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Creates sample data for testing the application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create users
        self.stdout.write('Creating users...')
        
        # Admin user
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('✓ Admin user created (username: admin, password: admin123)'))
        else:
            admin = User.objects.get(username='admin')
            self.stdout.write(self.style.WARNING('Admin user already exists'))

        # Organizer user
        if not User.objects.filter(username='organizer').exists():
            organizer = User.objects.create_user(
                username='organizer',
                email='organizer@example.com',
                password='organizer123',
                first_name='John',
                last_name='Organizer',
                is_staff=True
            )
            self.stdout.write(self.style.SUCCESS('✓ Organizer user created (username: organizer, password: organizer123)'))
        else:
            organizer = User.objects.get(username='organizer')
            self.stdout.write(self.style.WARNING('Organizer user already exists'))

        # Student users
        students = []
        student_data = [
            ('student', 'student123', 'Alice', 'Student', 'alice@example.com'),
            ('student2', 'student123', 'Bob', 'Johnson', 'bob@example.com'),
            ('student3', 'student123', 'Carol', 'Williams', 'carol@example.com'),
        ]

        for username, password, first_name, last_name, email in student_data:
            if not User.objects.filter(username=username).exists():
                student = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                students.append(student)
                self.stdout.write(self.style.SUCCESS(f'✓ Student user created (username: {username}, password: {password})'))
            else:
                student = User.objects.get(username=username)
                students.append(student)
                self.stdout.write(self.style.WARNING(f'Student user {username} already exists'))

        # Create events
        self.stdout.write('\nCreating events...')
        
        events_data = [
            {
                'title': 'Python Programming Workshop',
                'description': 'Learn the fundamentals of Python programming in this hands-on workshop. Perfect for beginners and intermediate programmers looking to enhance their skills.',
                'date': timezone.now() + timedelta(days=7),
                'location': 'Computer Lab A, Building 3',
                'organizer': organizer
            },
            {
                'title': 'Annual Tech Conference 2024',
                'description': 'Join us for the biggest tech conference of the year! Network with industry professionals, attend keynote speeches, and explore the latest in technology.',
                'date': timezone.now() + timedelta(days=14),
                'location': 'Main Auditorium',
                'organizer': organizer
            },
            {
                'title': 'Web Development Bootcamp',
                'description': 'Intensive 3-day bootcamp covering HTML, CSS, JavaScript, and modern web frameworks. Build real-world projects and launch your web development career.',
                'date': timezone.now() + timedelta(days=21),
                'location': 'Innovation Hub',
                'organizer': admin
            },
            {
                'title': 'Data Science Seminar',
                'description': 'Explore the world of data science, machine learning, and AI. Learn from industry experts and discover career opportunities in this exciting field.',
                'date': timezone.now() + timedelta(days=10),
                'location': 'Lecture Hall B',
                'organizer': organizer
            },
            {
                'title': 'Hackathon 2024',
                'description': '24-hour coding challenge! Form teams, solve real-world problems, and compete for amazing prizes. All skill levels welcome.',
                'date': timezone.now() + timedelta(days=30),
                'location': 'Student Center',
                'organizer': admin
            },
            {
                'title': 'Career Fair - Tech Companies',
                'description': 'Meet recruiters from top tech companies. Bring your resume, network with professionals, and explore internship and job opportunities.',
                'date': timezone.now() + timedelta(days=5),
                'location': 'Sports Complex',
                'organizer': organizer
            },
        ]

        created_events = []
        for event_data in events_data:
            if not Event.objects.filter(title=event_data['title']).exists():
                event = Event.objects.create(**event_data)
                created_events.append(event)
                self.stdout.write(self.style.SUCCESS(f'✓ Event created: {event.title}'))
            else:
                event = Event.objects.get(title=event_data['title'])
                created_events.append(event)
                self.stdout.write(self.style.WARNING(f'Event already exists: {event.title}'))

        # Create registrations
        self.stdout.write('\nCreating sample registrations...')
        
        registration_count = 0
        for i, event in enumerate(created_events[:4]):  # Register students for first 4 events
            for j, student in enumerate(students):
                if (i + j) % 2 == 0:  # Register some students to some events
                    if not Registration.objects.filter(student=student, event=event).exists():
                        Registration.objects.create(student=student, event=event)
                        registration_count += 1

        self.stdout.write(self.style.SUCCESS(f'✓ Created {registration_count} sample registrations'))

        # Summary
        self.stdout.write('\n' + '='*50)
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write('='*50)
        self.stdout.write('\nLogin credentials:')
        self.stdout.write('  Admin:     username: admin     password: admin123')
        self.stdout.write('  Organizer: username: organizer password: organizer123')
        self.stdout.write('  Student:   username: student   password: student123')
        self.stdout.write('\nYou can now run: python manage.py runserver')
