import os
import logging
from flask import Flask

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return 'ok'

@app.route('/upload', methods=['POST'])
def upload():
    # TODO: load the file in memory
    return 'ok'

app.run(threaded=True, port=int(os.getenv('PORT', 8080)))
