import sqlahelper
from bankaccount.resources import Root
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from sqlalchemy import engine_from_config

my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings)
    sqlahelper.add_engine(engine=engine)

    config = Configurator(root_factory=Root,
                          settings=settings,
                          session_factory=my_session_factory)

    config.include('pyramid_mako')
    config.include('pyramid_tm')
    config.add_route('home', '/')
    config.add_route('deposit', '/deposit')
    config.add_route('withdraw', '/withdraw')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan('.views')
    return config.make_wsgi_app()
