# Gazprom_id_people

`python3 -m venv venv`
`source venv/bin/activate`
`pip install poetry`
`poetry install`
`python3 manage.oy makemigrations`
`python3 manage.py migrate`
`python3 manage.py createsuperuser`
`python3 manage.py runserver`


```
python3 manage.py loaddata skill.json status.json office.json timezone.json position.json progress_status.json tag.json department.json company_team.json company_unit.json company.json employee.json

```