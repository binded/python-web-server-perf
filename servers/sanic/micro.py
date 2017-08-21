import os
from sanic import Sanic
from sanic.response import json, text

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/health', methods=['GET'])
async def health(request):
    return text('ok')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

