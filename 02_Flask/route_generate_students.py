import csv
from faker import Faker
from webargs import fields
from webargs.flaskparser import use_args

import settings


@use_args({
    'count': fields.Int(required=True, validate=lambda value: value <= settings.LIMIT_DATABASE_QUERIES)},
    location='query')
def generate_students(args: dict) -> str:
    """
    Generate random students with first name, last name, email, password and date of birth
    Count of students get from GET-parameter <count>
    List of students records to CSV_FILE_PATH_STUDENTS in csv format
    :param args: arguments from request
    :return: string with students in HTML format
    """
    count = args.get('count')

    faker = Faker('uk_UA')
    students_to_html = ''
    students_to_file = []
    for item in range(count):

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password(length=15)
        date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d.%m.%Y')

        students_to_file.append([first_name, last_name, email, password, date_of_birth])
        students_to_html += (f'<p># {item + 1} name - {first_name} {last_name}, email - {email}, password - {password},'
                             f' date of birth - {date_of_birth}</p>')

    #  NOTE: Use default delimiter ',' in csv file, because variable <password> not contains character ','
    with open(settings.CSV_FILE_PATH_STUDENTS, 'a') as file:
        csv.writer(file).writerows(students_to_file)

    return students_to_html
