import os, sys # noqa
from django.core.wsgi import get_wsgi_application

#  path a donde esta el manage.py de nuestro proyecto Django
sys.path.append('/Users/claudiorojasrodriguez/src/personal/vetadmin/vetadmin-backend') # noqa

#  referencia (en python) desde el path anterior al fichero settings.py
#  Importante hacerlo así, si hay varias instancias coriendo (en lugar de setdefault) # noqa
os.environ['DJANGO_SETTINGS_MODULE'] = 'vetadmin-backend.settings'
#  os.environ.setdefault(“DJANGO_SETTINGS_MODULE”, “proyectodjango.settings”)

#  prevenimos UnicodeEncodeError
os.environ.setdefault('LANG', 'es_CL.UTF-8')
os.environ.setdefault('LC_ALL', 'es_CL.UTF-8')

#  activamos nuestro virtualenv
activate_this = '/Users/claudiorojasrodriguez/src/personal/vetadmin/env/bin/activate' # noqa
exec(open("./activate_this").read(), dict(__file__=activate_this))

#  obtenemos la aplicación

application = get_wsgi_application()


'''
[uwsgi]socket = 127.0.0.1:3031
chdir = /Users/claudiorojasrodriguez/src/personal/vetadmin/backend
pythonpath = ..
env = DJANGO_SETTINGS_MODULE=backend.settings
module = django.core.handlers.wsgi:WSGIHandler()
processes = 4
threads = 2
stats = 127.0.0.1:9191
'''
