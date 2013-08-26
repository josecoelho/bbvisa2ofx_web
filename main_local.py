import sys, os
sys.path.append(os.getcwd())

import web, index
from index import index


urls = (
    '/', 'index'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


