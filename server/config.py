import logging
import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/v1")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "db")

MYSQL = {
    "user": os.getenv("APPLICATION_MYSQL_USER", "tZHMoJM3nT"),
    "pw": os.getenv("APPLICATION_MYSQL_PW", "wIoZa73qjF"),
    "host": os.getenv("APPLICATION_MYSQL_HOST", DB_CONTAINER),
    "port": os.getenv("APPLICATION_MYSQL_PORT", 3306),
    "db": os.getenv("APPLICATION_MYSQL_DB", "tZHMoJM3nT"),
}

# Uncomment this if you want to use mysql

# DB_URI = "mysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % MYSQL
DB_URI = 'sqlite:///payroll.db'

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
