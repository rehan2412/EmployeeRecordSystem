# EmployeeRecordSystem
Employee Record Transmission and Storage System

### README: Setup Instructions & Dependencies

# Setup Instructions:
1. Clone the repository: 'git clone <repo-url>'
2. Navigate to the project directory: 'cd EmployeeRecordSystem'
3. Create a virtual environment: 'python -m venv venv'
4. Activate the virtual environment:
   - Windows: 'venv\Scripts\activate'
   - Mac/Linux: 'source venv/bin/activate'
5. Install dependencies: 'pip install -r requirements.txt'
6. Configure MySQL settings in 'config/settings.py'
7. Apply migrations: 'python manage.py migrate'
8. Run the server: 'python manage.py runserver'

# Dependencies (requirements.txt):
django
mysqlclient
aiohttp

