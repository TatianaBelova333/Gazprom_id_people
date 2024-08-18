# Gazprom_id_people

### Technology Stack
* React
* Django 
* Python 3.12
* Gunicorn
* Nginx
* Docker
* PostgreSQL

`python3 -m venv venv`<br>
`source venv/bin/activate`<br>
`pip install poetry`<br>
`poetry install`<br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`<br>
`python3 manage.py createsuperuser`<br>
`python3 manage.py runserver`<br>


```
python3 manage.py loaddata skill.json status.json company.json office.json timezone.json position.json progress_status.json tag.json department.json company_team.json company_unit.json employee.json project.json

```

### Team

Александра Петелина - PM<br>
Артем Пацев - PdM<br>
Ольга Гамаюнова - Старший в направлении design
Дмитрий Логунков - design
Екатерина Гадасина - design
Виктория Собко - design
Татьяна Луконина - design
Кирилл Ковригин - старший в направлении SA
Екатерина Байзигитова -  SA
Дарья Учаева -страший в направлении BA
Беклемышев Андрей - BA
Анастасия Лазарева - Frontend
Татьяна Белова - Backend
Кирилл Новиков -  QA
