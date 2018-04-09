import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY = 'e89fb969868d4dd995c4311b256d7274'
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/'
    #NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/{}?apiKey={}' // APPLIES WHEN THE base_url is passed as the string



class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    pass


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
