from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Event, Registration


class EventModelTest(TestCase):
    """Test cases for Event model"""
    
    def setUp(self):
        self.organizer = User.objects.create_user(
            username='testorganizer',
            password='testpass123',
            is_staff=True
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date=timezone.now() + timedelta(days=7),
            location='Test Location',
            organizer=self.organizer
        )
    
    def test_event_creation(self):
        """Test that event is created correctly"""
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.organizer, self.organizer)
    
    def test_event_str(self):
        """Test event string representation"""
        self.assertEqual(str(self.event), 'Test Event')
    
    def test_is_past(self):
        """Test is_past method"""
        self.assertFalse(self.event.is_past())


class RegistrationModelTest(TestCase):
    """Test cases for Registration model"""
    
    def setUp(self):
        self.student = User.objects.create_user(
            username='teststudent',
            password='testpass123'
        )
        self.organizer = User.objects.create_user(
            username='testorganizer',
            password='testpass123',
            is_staff=True
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date=timezone.now() + timedelta(days=7),
            location='Test Location',
            organizer=self.organizer
        )
    
    def test_registration_creation(self):
        """Test that registration is created correctly"""
        registration = Registration.objects.create(
            student=self.student,
            event=self.event
        )
        self.assertEqual(registration.student, self.student)
        self.assertEqual(registration.event, self.event)
    
    def test_unique_registration(self):
        """Test that a student can't register twice for the same event"""
        Registration.objects.create(student=self.student, event=self.event)
        with self.assertRaises(Exception):
            Registration.objects.create(student=self.student, event=self.event)


class ViewsTest(TestCase):
    """Test cases for views"""
    
    def setUp(self):
        self.client = Client()
        self.student = User.objects.create_user(
            username='teststudent',
            password='testpass123'
        )
        self.organizer = User.objects.create_user(
            username='testorganizer',
            password='testpass123',
            is_staff=True
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date=timezone.now() + timedelta(days=7),
            location='Test Location',
            organizer=self.organizer
        )
    
    def test_home_page(self):
        """Test home page loads correctly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Engagement Platform')
    
    def test_event_detail_page(self):
        """Test event detail page loads correctly"""
        response = self.client.get(reverse('event_detail', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)
    
    def test_login_required_for_registration(self):
        """Test that login is required to register for events"""
        response = self.client.get(reverse('register_for_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_student_can_register(self):
        """Test that student can register for event"""
        self.client.login(username='teststudent', password='testpass123')
        response = self.client.post(reverse('register_for_event', args=[self.event.id]))
        self.assertEqual(Registration.objects.filter(student=self.student, event=self.event).count(), 1)
    
    def test_organizer_dashboard_access(self):
        """Test that organizers can access dashboard"""
        self.client.login(username='testorganizer', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
