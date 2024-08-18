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

1. Клонировать репозиторий<br>
`git clone https://github.com/TatianaBelova333/Gazprom_id_people.git`

2. В корне проекта создать файл .env по типу env.example.

3. Перейти в папку infra из корня проекта<br>
```
cd infra

```
4. Выполнить следующие команды<br>
- Запустить приложение в контейнерах
```
docker compose up
```
- Создать миграции
```
docker compose exec backend python manage.py makemigrations
```
- Применить миграции
```
docker compose exec backend python manage.py migrate
```
- Заполнить базу тестовыми данными

```
docker compose exec backend python manage.py loaddata skill status company office timezone position progress_status tag department company_team company_unit employee project service component
```

- Собрать статику
```
docker compose exec backend python manage.py collectstatic
```
- Скопировать статику в volume
```
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/

```
- Создать суперпользователя
```
docker compose exec backend python manage.py createsuperuser
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
