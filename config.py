class Config:
    SECRET_KEY = 'jhgjhgjgjgjgj'        # os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'kaa-it@yandex.ru'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'k28L07v60@'        # os.environ.get('MAIL_PASSWORD')
    OMNILINER_ADMIN = 'kaa-it@yandex.ru'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}