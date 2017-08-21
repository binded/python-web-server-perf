import os
import logging
from sanic import Sanic
from sanic.response import json, text

app = Sanic()

logging.getLogger('network').setLevel(logging.ERROR)
logging.getLogger('sanic').setLevel(logging.ERROR)

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/health', methods=['GET'])
async def health(request):
    return text('ok')

@app.route('/upload', methods=['POST'])
def upload(request):
    # TODO: load the file in memory
    return text('ok')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(
        host='0.0.0.0',
        port=port,
        workers=1,
        debug=False
    )

