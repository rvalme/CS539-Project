import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
django.setup()

from first_app.models import ZipStarbuck


def add_zip(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            z = ZipStarbuck.objects.get_or_create(zipcode=row[0], num_sb=row[1])

if __name__ == '__main__':
     print('populating script')
     add_zip('LinearRegression.csv')
