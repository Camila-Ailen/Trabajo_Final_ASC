'''
from cross_run.wsgi import *
#from cliente.models import Cliente

from django.test import TestCase

# Create your tests here.
# c = Cliente.objects.get(pk=1)

c = Cliente.objects.all()
print (c)



print ("Hola mundo")

'''
