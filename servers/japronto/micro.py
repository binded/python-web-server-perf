import os
from japronto import Application

def hello(request):
    return request.Response(text='Hello world!')


def health(request):
    return request.Response(text='OK')

app = Application()

r = app.router
r.add_route('/', hello, method='GET')
r.add_route('/health', health, method='GET')

app.run(port=int(os.getenv('PORT', 8080)))
