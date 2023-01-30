import os
SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'

# Remplacez par l'id de l'app TEST que vous avez créée précédemment.
FB_APP_ID = 12345678901234567890

basedir = os.path.abspath(os.path.dirname(__file__))

# Nouvelle base de données pour les tests.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

# Facebook test user
FB_USER_NAME = "Ellen"
FB_USER_PW = "YOLOYOLO"
FB_USER_EMAIL = "ellen_rmilrcp_page@tfbnw.net"
FB_USER_ID = 100018814390853
FB_USER_GENDER = 'female'
