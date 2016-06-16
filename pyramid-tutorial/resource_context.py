from datetime import date, datetime

from pyramid.config import Configurator
from pyramid.view import view_config
from waitress import serve


class MyContext(object):
    def __init__(self, request):
        self.request = request

    def get_date(self):
        return date.today()

    def greeting(self):
        now = datetime.now()
        if now.hour < 12:
            return 'Good morning'
        elif now.hour < 18:
            return 'Good afternoon'
        else:
            return 'Good evening'


@view_config(route_name='home', renderer='index2.mak')
def index(request):
    return dict()


if __name__ == '__main__':
    import os

    here = os.path.dirname(__file__)
    settings = {
        'mako.directories': [
            os.path.abspath(os.path.join(here, 'templates')),
        ],
    }
    config = Configurator(settings=settings, root_factory=MyContext)
    config.include('pyramid_mako')
    config.add_route('home', '/')
    config.scan()
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
