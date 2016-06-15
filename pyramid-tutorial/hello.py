from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello, World!')


if __name__ == '__main__':
    config = Configurator()
    config.add_view(hello_world)
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
