# Demo Django Application with Django Ninja

A modern Django application demonstrating REST API development using Django Ninja, with PostgreSQL database and uv package manager.

## Tech Stack

- Python 3.13+
- Django 5.1+
- Django Ninja 1.3+
- PostgreSQL
- uv package manager

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.13 or higher
- PostgreSQL
- uv package manager (`pip install uv`)

## Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd demo-django-application-with-django-ninja
```

2. **Create and activate virtual environment:**
```bash
# Create virtual environment
uv venv

# Activate virtual environment
# On Unix/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

3. **Install dependencies:**
```bash
uv pip sync
```

## Environment Setup

1. **Create environment file:**
```bash
cp .env.example .env
```

2. **Update .env with your configuration:**
```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## Database Setup

1. **Create PostgreSQL database:**
```bash
createdb dbname
```

2. **Apply migrations:**
```bash
python manage.py migrate
```

3. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

## Running the Application

1. **Start development server:**
```bash
python manage.py runserver
```

2. **Access the application:**
- Main application: http://localhost:8000
- Admin interface: http://localhost:8000/admin
- API documentation: http://localhost:8000/api/docs

## API Documentation

The API documentation is automatically generated using Django Ninja's built-in Swagger/OpenAPI support:

- Swagger UI: http://localhost:8000/api/docs
- OpenAPI JSON: http://localhost:8000/api/openapi.json

## Project Structure
```
demo-django-application-with-django-ninja/
├── manage.py                  # Django management script
├── demo/                      # Main project directory
│   ├── __init__.py
│   ├── settings/             # Project settings
│   │   ├── __init__.py
│   │   ├── base.py          # Base settings
│   │   ├── local.py         # Local development settings
│   │   └── production.py    # Production settings
│   │   └── stage.py         # Stage settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
│   ├── app1/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── api_app1.py
│   │   ├── models/
│   │   ├── tests/
│   │   ├── schemas/
│   │  
│   ├── app2/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── api_app2.py
│   │   ├── models/
│   │   ├── tests/
│   │   ├── schemas/
│   ├── app3/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── api_app3.py
│   │   ├── models/
│   │   ├── tests/
│   │   ├── schemas/
├── pyproject.toml           # Project dependencies
└── README.md                # Project documentation
```



### Making Migrations
After modifying models, create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/amazing-feature
```
3. Commit your changes:
```bash
git commit -m 'Add some amazing feature'
```
4. Push to the branch:
```bash
git push origin feature/amazing-feature
```
5. Open a Pull Request

## Troubleshooting

### Common Issues

1. **Database Connection Issues**
   - Ensure PostgreSQL is running
   - Verify database credentials in .env
   - Check database exists

2. **Package Installation Issues**
   - Make sure virtual environment is activated
   - Update uv: `pip install -U uv`

### Getting Help
If you encounter any issues:
1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Check the [Django Ninja documentation](https://django-ninja.rest-framework.com/)
3. Open an issue in the repository

## License

[Add your license here]

## Contact

[Add your contact information]