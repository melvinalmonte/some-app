import os

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ["DATABASE"]
port = os.environ["MYSQL_PORT"]
DATABASE_CONNECTION_URI = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
