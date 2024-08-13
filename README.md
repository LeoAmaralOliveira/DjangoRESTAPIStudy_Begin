# 📚 Alura School API
## What is Alura School API?
Alura school API is an Django REST Framework API which registers students, courses and registrations. The focus is to register, read and analyze data to create some metrics later.

## Tech and skills
- `Python`
- `Python OOP`
- `Django`
- `Django REST Framework`
- `GitHub Issues`
- `GitHub Releases`

## Endpoints
| Allow | Endpoint | Description |
|---|---|---|
| `GET`, `POST` | students | Read and create new students |
| `GET`, `POST` | courses | Read and create new courses |
| `GET`, `POST` | registration | Read and create new registrations |
| `GET`, `PUT`, `PATCH`, `DELETE` | students/id | CRUD of student |
| `GET`, `PUT`, `PATCH`, `DELETE` | courses/id | CRUD of courses |
| `GET`, `PUT`, `PATCH`, `DELETE` | registrations/id | CRUD of registrations |
| `GET` | students/id/registrations | Read course registrations of a student |
| `GET` | courses/id/registrations | Read student registrations into a course |

## Installation
### Local installation
Python version: `3.12`

**Create the .env file with your Django SECRET_KEY**

Then, follow the sequence:

| Commands | Description |
|---|---|
| `pip install -r requirements.txt` | Install dependencies |
| `python manage.py migrate` | Migrate database |
| `python manage.py runserver` | Run application |

### Using Docker
You can install docker clicking right <a href="https://docs.docker.com/engine/install/" target="_blank">here</a>.

Build image: `docker build -t 'alura_schools_api' .`

Running container: `docker run -p 8000:8000 alura_schools_api`

## Collaborate
Feel free to collaborate with the project! Create your own version and make the modifications you want it to.
