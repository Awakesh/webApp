import os


class Config:
    SECRET_KEY = "m\xb3Z\xceL\x1b0\xc9\xb623\xb8\x17\xeazp\xb8\xa8d\xb4\xaav\xfa\x81\x95\xe71;\xccQ\x04\xc9"
    SQLALCHEMY_DATABASE_URI = "mysql://root:Awakesh@143@localhost/test"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
