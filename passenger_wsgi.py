import sys, os

# Указываем путь к папке приложения
sys.path.append(os.getcwd())

# Импортируем wsgi_app и переименовываем в application для cPanel
from api import wsgi_app as application

