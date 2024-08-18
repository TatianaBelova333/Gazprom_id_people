# Gazprom_id_people

### Technology Stack
* React
* Django 
* Python 3.12
* Gunicorn
* Nginx
* Docker
* PostgreSQL
<br>
<br>
<br>

1. Клонировать репозиторий
`git clone https://github.com/TatianaBelova333/Gazprom_id_people.git`

2. Создать виртуальное окружение<br>
`python3 -m venv venv`<br>
`source venv/bin/activate`<br>

3. Перейти в папку infra из корня проекта<br>
`cd infra`<br>
4. Выполнить следующие команды<br>
```
docker compose up
```
```
docker compose exec backend python manage.py migrate
```
```
docker compose exec backend python manage.py makemigrations
```
```
docker compose exec backend python manage.py migrate
```
`docker compose exec backend python manage.py loaddata skill status company office timezone position progress_status tag department company_team company_unit employee project service component`<br>




<b>Это не надо</b>
`pip install poetry`<br>
`poetry install`<br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`<br>
`python3 manage.py createsuperuser`<br>
`python3 manage.py runserver`<br>


```
python3 manage.py loaddata skill status company office timezone position progress_status tag department company_team company_unit employee project service component

```

### Team

* Александра Петелина - PM<br>
* Артем Пацев - PdM<br>
* Ольга Гамаюнова - Старший в направлении design<br>
* Дмитрий Логунков - design<br>
* Екатерина Гадасина - design<br>
* Виктория Собко - design<br>
* Татьяна Луконина - design<br>
* Кирилл Ковригин - старший в направлении SA<br>
* Екатерина Байзигитова -  SA<br>
* Дарья Учаева -страший в направлении BA<br>
* Беклемышев Андрей - BA<br>
* Анастасия Лазарева - Frontend<br>
* Татьяна Белова - Backend<br>
* Кирилл Новиков -  QA<br>
