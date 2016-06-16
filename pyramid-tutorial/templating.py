from pyramid.config import Configurator
from pyramid.view import view_config
from waitress import serve


@view_config(route_name='home', renderer='index.mak')
def index(request):
    return dict(name='pyramid')


if __name__ == '__main__':
    import os

    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
    }
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_route('home', '/')
    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
