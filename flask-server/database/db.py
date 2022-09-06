import os
import psycopg2
from psycopg2 import DatabaseError
#from decouple import config
#from config import config
#SECRET_KEY=P4SSW0RD
#PGSQL_HOST=Localhost
#PGSQL_USER=postgres
#PGSQL_PASSWORD=root
#PGSQL_HOST_DATABASE=python_flask_rest

def get_connection():
    
    try:
        return psycopg2.connect(
            host="localhost",
            user="postgres",
            password="root",
            database="python_flask_rest"
        )
    except DatabaseError as ex:
        raise ex
