HOST = "118.25.71.143"
PORT = "3306"
DB = "gathering"
USER = "root"
PASS = "zhang990113."
CHARSET = "utf8mb4"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASS, HOST, PORT, DB, CHARSET)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
JSON_AS_ASCII = False
SECRET_KEY = 'key'