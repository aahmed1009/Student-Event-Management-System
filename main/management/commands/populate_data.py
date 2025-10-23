from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Event, Registration
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate database with 50 events and registrations for 2025'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data population...')

        # Create admin user if doesn't exist
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created admin user'))

        # Create staff users
        staff_users = []
        for i in range(1, 6):
            user, created = User.objects.get_or_create(
                username=f'staff{i}',
                defaults={
                    'email': f'staff{i}@example.com',
                    'first_name': f'Staff',
                    'last_name': f'Member{i}',
                    'is_staff': True,
                }
            )
            if created:
                user.set_password('staff123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created staff user: {user.username}'))
            staff_users.append(user)

        # Create student users
        student_users = []
        for i in range(1, 31):
            user, created = User.objects.get_or_create(
                username=f'student{i}',
                defaults={
                    'email': f'student{i}@example.com',
                    'first_name': f'Student',
                    'last_name': f'User{i}',
                }
            )
            if created:
                user.set_password('student123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created student user: {user.username}'))
            student_users.append(user)

        # Event data templates
        event_types = [
            'Workshop', 'Seminar', 'Conference', 'Lecture', 'Training',
            'Hackathon', 'Meetup', 'Webinar', 'Symposium', 'Forum'
        ]
        
        topics = [
            'Web Development', 'Machine Learning', 'Data Science', 'Cybersecurity',
            'Cloud Computing', 'Mobile Development', 'AI Ethics', 'Blockchain',
            'DevOps', 'UI/UX Design', 'Database Management', 'Network Security',
            'Python Programming', 'JavaScript Frameworks', 'Software Testing',
            'Agile Methodologies', 'Project Management', 'Digital Marketing',
            'Business Analytics', 'Internet of Things'
        ]

        locations = [
            'Main Auditorium', 'Conference Room A', 'Conference Room B',
            'Lab 101', 'Lab 102', 'Lecture Hall 1', 'Lecture Hall 2',
            'Innovation Center', 'Tech Hub', 'Online (Zoom)',
            'Library Meeting Room', 'Student Center', 'Building A - Room 301',
            'Building B - Room 205', 'Outdoor Amphitheater'
        ]

        descriptions = [
            'Join us for an engaging session covering the latest trends and best practices.',
            'An interactive workshop designed to enhance your skills and knowledge.',
            'Learn from industry experts and network with professionals in the field.',
            'Hands-on training session with practical exercises and real-world examples.',
            'Discover cutting-edge technologies and their applications in modern development.',
            'A comprehensive overview of fundamental concepts and advanced techniques.',
            'Participate in collaborative activities and gain valuable insights.',
            'Expert-led discussion on current challenges and innovative solutions.',
            'Deep dive into practical applications with live demonstrations.',
            'Enhance your understanding through case studies and group discussions.'
        ]

        # Create 50 events for 2025
        events_created = 0
        start_date = datetime(2025, 1, 1, 9, 0)
        
        for i in range(50):
            # Generate event date in 2025
            days_offset = random.randint(0, 364)
            hours_offset = random.randint(0, 9)
            event_date = start_date + timedelta(days=days_offset, hours=hours_offset)
            
            # Create event
            event_type = random.choice(event_types)
            topic = random.choice(topics)
            title = f"{event_type}: {topic}"
            
            event, created = Event.objects.get_or_create(
                title=title,
                date=event_date,
                defaults={
                    'description': random.choice(descriptions),
                    'location': random.choice(locations),
                    'organizer': random.choice(staff_users + [admin_user]),
                }
            )
            
            if created:
                events_created += 1
                
                # Register random students for this event
                num_registrations = random.randint(5, 20)
                registered_students = random.sample(student_users, min(num_registrations, len(student_users)))
                
                for student in registered_students:
                    Registration.objects.get_or_create(
                        student=student,
                        event=event
                    )
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created event {events_created}/50: {event.title} on {event.date.strftime("%Y-%m-%d")} '
                        f'with {num_registrations} registrations'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✓ Data population complete!\n'
                f'  - Created {events_created} events\n'
                f'  - Created {len(staff_users)} staff users\n'
                f'  - Created {len(student_users)} student users\n'
                f'  - All events are scheduled for 2025\n\n'
                f'Login credentials:\n'
                f'  Admin: username=admin, password=admin123\n'
                f'  Staff: username=staff1-5, password=staff123\n'
                f'  Students: username=student1-30, password=student123'
            )
        )
