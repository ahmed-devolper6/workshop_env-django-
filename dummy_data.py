import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from faker import Faker
import random
from job.models import Job , Category 
