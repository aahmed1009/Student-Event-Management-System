from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Events
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('event/<int:event_id>/unregister/', views.unregister_from_event, name='unregister_from_event'),
    path('event/<int:event_id>/registrations/', views.event_registrations, name='event_registrations'),
    
    # Event Management (Organizers)
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    
    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-events/', views.my_events, name='my_events'),
]
