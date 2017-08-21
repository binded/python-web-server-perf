import os
import logging
from flask import Flask

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return 'ok'

app.run(port=int(os.getenv('PORT', 8080)))
