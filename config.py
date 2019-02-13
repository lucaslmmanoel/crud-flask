"""
Arquivo de configurações de ambiente
"""
class Config(object):
    """
    Configuração comum entre os ambientes
    """


class DevelopmentConfig(Config):
    """
    Configurações de desenvolvimento
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Configurações de produção
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}