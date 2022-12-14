"""
WSGI config for blogsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import whitenoise

''''''
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling



from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings')

application = Cling(get_wsgi_application())

'''
from django.core.wsgi import get_wsgi_application

#from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
whitenoise.WhiteNoise(application)'''
