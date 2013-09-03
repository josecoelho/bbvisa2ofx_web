import sys, os
sys.path.append(os.getcwd())

import web, index
from index import index


urls = (
    '/', 'index'
)

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()


