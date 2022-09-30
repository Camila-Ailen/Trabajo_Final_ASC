
#from config.wsgi import *
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cross_run.settings')

application = get_wsgi_application()


from cliente.models import Cliente
'''
from django.test import TestCase

# Create your tests here.
# c = Cliente.objects.get(pk=1)

c = Cliente.objects.all()
print (c)

'''
print ('Hola mundo')


