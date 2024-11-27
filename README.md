### Virtual env
Create your virtul env and use it:
```
# create venv
python -m venv venv
# activate it 
source venv/bin/activate
```
### install requirements
```
pip install -r requirements.txt
```

### Datebase
Execute this before using this application:
```
# Migrate your database
python manage.py migrate
# Create your admin user
python manage.py createsuperuser --username=admin
```