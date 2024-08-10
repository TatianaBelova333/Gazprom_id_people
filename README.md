# Gazprom_id_people

`python3 -m venv venv`<br>
`source venv/bin/activate`<br>
`pip install poetry`<br>
`poetry install`<br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`<br>
`python3 manage.py createsuperuser`<br>
`python3 manage.py runserver`<br>


```
python3 manage.py loaddata skill.json status.json office.json timezone.json position.json progress_status.json tag.json department.json company_team.json company_unit.json company.json employee.json

```