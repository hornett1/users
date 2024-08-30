import sys
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from app_users.models import *

user1 = User(name='name1', email='email@gmail.com',role='Admin')

group = Group(group_name='group1')

user1.save()
group.save()

user = User.objects.get(id=1)
group = Group.objects.get(id=1)

user.group.add(group)