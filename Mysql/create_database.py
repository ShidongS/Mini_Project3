import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Mini3'

TABLES = {}
TABLES['pictures'] = (
    "CREATE TABLE `pictures` ("
    "  `pic_no` int(11) NOT NULL,"
    "  `url` varchar(150) NOT NULL,"
    "  `account_name` varchar(30) NOT NULL,"
    "  PRIMARY KEY (`pic_no`)"
    ") ENGINE=InnoDB")

TABLES['tags'] = (
    "CREATE TABLE `tags` ("
    "  `tag_no` int(10) NOT NULL,"
    "  `tag_name` varchar(40) NOT NULL UNIQUE,"
    "  PRIMARY KEY (`tag_no`)"
    ") ENGINE=InnoDB")

TABLES['link'] = (
    "CREATE TABLE `link` ("
    "  `pic_no` int(10) NOT NULL,"
    "  `tag_no` int(10) NOT NULL,"
    "  PRIMARY KEY (`pic_no`,`tag_no`), KEY `pic_no` (`pic_no`), KEY `tag_no` (`tag_no`), "
    "  FOREIGN KEY (`pic_no`) REFERENCES `pictures` (`pic_no`) ON DELETE CASCADE,"
    "  FOREIGN KEY (`tag_no`) REFERENCES `tags` (`tag_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='username',
	                          password='password')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()