import sqlahelper
from bankaccount.resources import Root
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from sqlalchemy import engine_from_config
from bankaccount.models import BankAccount

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
    config.include('ps_alchemy')
    config.include('pyramid_sacrud')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('tempaltes')
    config.include('ps_crud')
    config.add_route('home', '/')
    config.add_route('deposit', '/deposit')
    config.add_route('withdraw', '/withdraw')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan('.views')
    settings = config.get_settings()
    settings['pyramid_sacrud.models'] = (('Group1', [BankAccount]),)
    return config.make_wsgi_app()
