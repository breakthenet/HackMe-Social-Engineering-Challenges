import os, sys
import base64
sys.path.append("hackathon/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from django.contrib.auth.models import User

#I just saved you from a spoiler. Don't cheat, find this out through the challenge, it's more satisfying!
password = "Z29sZGZpc2g=" 
user = User.objects.create_superuser(username='scotty', email='scotty@outerspace.com', password=base64.b64decode(password))
