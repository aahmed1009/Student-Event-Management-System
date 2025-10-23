from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from .models import Event, Registration
from .forms import StudentRegistrationForm, EventForm


def home(request):
    """Home page showing all events"""
    events = Event.objects.all()
    return render(request, 'main/index.html', {'events': events})


def login_view(request):
    """Login page for all users"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    """Logout user"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


def register_view(request):
    """Student registration page"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to the platform.')
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'main/register.html', {'form': form})


def event_detail(request, event_id):
    """Event detail page"""
    event = get_object_or_404(Event, id=event_id)
    is_registered = False
    
    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(student=request.user, event=event).exists()
    
    return render(request, 'main/event_detail.html', {
        'event': event,
        'is_registered': is_registered
    })


@login_required
def register_for_event(request, event_id):
    """Register student for an event"""
    event = get_object_or_404(Event, id=event_id)
    
    # Check if user is a student (not staff or superuser)
    if request.user.is_staff or request.user.is_superuser:
        messages.error(request, 'Only students can register for events.')
        return redirect('event_detail', event_id=event_id)
    
    try:
        registration = Registration.objects.create(student=request.user, event=event)
        messages.success(request, f'Successfully registered for "{event.title}"!')
    except IntegrityError:
        messages.warning(request, 'You are already registered for this event.')
    
    return redirect('event_detail', event_id=event_id)


@login_required
def unregister_from_event(request, event_id):
    """Unregister student from an event"""
    event = get_object_or_404(Event, id=event_id)
    
    try:
        registration = Registration.objects.get(student=request.user, event=event)
        registration.delete()
        messages.success(request, f'Successfully unregistered from "{event.title}".')
    except Registration.DoesNotExist:
        messages.error(request, 'You are not registered for this event.')
    
    return redirect('event_detail', event_id=event_id)


@login_required
def dashboard(request):
    """Dashboard for organizers and admins"""
    if request.user.is_staff or request.user.is_superuser:
        # Organizer/Admin dashboard
        if request.user.is_superuser:
            events = Event.objects.all()
        else:
            events = Event.objects.filter(organizer=request.user)
        
        return render(request, 'main/dashboard.html', {
            'events': events,
            'is_organizer': True
        })
    else:
        # Student dashboard - redirect to my events
        return redirect('my_events')


@login_required
def my_events(request):
    """Show student's registered events"""
    registrations = Registration.objects.filter(student=request.user).select_related('event')
    return render(request, 'main/my_events.html', {'registrations': registrations})


@login_required
def create_event(request):
    """Create a new event (organizers only)"""
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'Only organizers can create events.')
        return redirect('home')
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, f'Event "{event.title}" created successfully!')
            return redirect('dashboard')
    else:
        form = EventForm()
    
    return render(request, 'main/create_event.html', {'form': form})


@login_required
def edit_event(request, event_id):
    """Edit an existing event"""
    event = get_object_or_404(Event, id=event_id)
    
    # Check permissions
    if not request.user.is_superuser and event.organizer != request.user:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, f'Event "{event.title}" updated successfully!')
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'main/edit_event.html', {'form': form, 'event': event})


@login_required
def delete_event(request, event_id):
    """Delete an event"""
    event = get_object_or_404(Event, id=event_id)
    
    # Check permissions
    if not request.user.is_superuser and event.organizer != request.user:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        event_title = event.title
        event.delete()
        messages.success(request, f'Event "{event_title}" deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'main/delete_event.html', {'event': event})


@login_required
def event_registrations(request, event_id):
    """View registered students for an event (organizers only)"""
    event = get_object_or_404(Event, id=event_id)
    
    # Check permissions
    if not request.user.is_superuser and event.organizer != request.user:
        messages.error(request, 'You do not have permission to view registrations for this event.')
        return redirect('dashboard')
    
    registrations = Registration.objects.filter(event=event).select_related('student')
    
    return render(request, 'main/event_registrations.html', {
        'event': event,
        'registrations': registrations
    })
