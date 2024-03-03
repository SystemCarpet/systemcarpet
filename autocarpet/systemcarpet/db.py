import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#MYSQL = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'systemcarpet',
#        'USER': 'root',
#        'PASSWORD': '',
#        'HOST': 'localhost',
#        'PORT': '3306',
#		'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
#    }
#}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'systemcarpet',
        'USER': 'postgres',
        'PASSWORD': '4321',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}