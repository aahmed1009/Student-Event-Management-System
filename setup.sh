#!/bin/bash

# Student Engagement Platform - Quick Setup Script

echo "=========================================="
echo "Student Engagement Platform - Setup"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo ""
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create sample data
echo ""
echo "Creating sample data..."
python manage.py create_sample_data

# Success message
echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then open your browser to: http://127.0.0.1:8000/"
echo ""
echo "Login credentials:"
echo "  Admin:     username: admin     password: admin123"
echo "  Organizer: username: organizer password: organizer123"
echo "  Student:   username: student   password: student123"
echo ""
