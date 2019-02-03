from django.core.management.base import BaseCommand
from django_seed import Seed
from django.db import models
from workers.models import Employee
from django.db.models import Min, Max

import random

class Command(BaseCommand):
    help = 'Fill db with test data.'
    args = ''

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(Employee, 1, {
            'full_name': lambda x: seeder.faker.name(),
            'position': 'chief',
            'employment_date': lambda x: seeder.faker.date_time_between(start_date="-15y", end_date="now", tzinfo=None),
            'salary': lambda x: random.uniform(5000.0,10000.0),
            'parent_id' : None
        })
        seeder.execute()

        ids = list(Employee.objects.filter(position='chief').values('id'))
        idslist = []
        for i in ids:
            idslist.append(i['id'])

        seeder.add_entity(Employee, 2, {
            'full_name': lambda x: seeder.faker.name(),
            'position': 'ceo',
            'employment_date': lambda x: seeder.faker.date_time_between(start_date="-10y", end_date="now", tzinfo=None),
            'salary': lambda x: random.uniform(4000.0,5000.0),
            'parent_id' : lambda x: Employee.objects.get(id=random.choice(idslist))
        })
        seeder.execute()


        ids = list(Employee.objects.filter(position='ceo').values('id'))
        idslist = []
        for i in ids:
            idslist.append(i['id'])

        seeder.add_entity(Employee, 2, {
            'full_name': lambda x: seeder.faker.name(),
            'position': 'general manager',
            'employment_date': lambda x: seeder.faker.date_time_between(start_date="-8y", end_date="now", tzinfo=None),
            'salary': lambda x: random.uniform(3000.0,4000.0),
            'parent_id' : lambda x: Employee.objects.get(id=random.choice(idslist))
        })
        seeder.execute()

        ids = list(Employee.objects.filter(position='general manager').values('id'))
        idslist = []
        for i in ids:
            idslist.append(i['id'])

        seeder.add_entity(Employee, 2, {
            'full_name': lambda x: seeder.faker.name(),
            'position': 'manager',
            'employment_date': lambda x: seeder.faker.date_time_between(start_date="-5y", end_date="now", tzinfo=None),
            'salary': lambda x: random.uniform(2000.0,3000.0),
            'parent_id' : lambda x: Employee.objects.get(id=random.choice(idslist))
        })
        seeder.execute()

        ids = list(Employee.objects.filter(position='manager').values('id'))
        idslist = []
        for i in ids:
            idslist.append(i['id'])

        seeder.add_entity(Employee, 2, {
            'full_name': lambda x: seeder.faker.name(),
            'position': 'engineer',
            'employment_date': lambda x: seeder.faker.date_time_between(start_date="-5y", end_date="now", tzinfo=None),
            'salary': lambda x: random.uniform(2000.0,3000.0),
            'parent_id' : lambda x: Employee.objects.get(id=random.choice(idslist))
        })
        seeder.execute()