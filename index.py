import web
import view, config
from view import render
from StringIO import StringIO


class index:
    def GET(self):
        return render.base(view.upload())


    def POST(self):
        from bbvisa2ofx import bbvisa2ofx
        i = web.input(txtfile={})

        txtFile = i['txtfile'].file
        strOfx = StringIO()
        bbvisa2ofx.convert(txtFile, strOfx, False)

        web.header('Content-Type', 'text/plain') # file type
        web.header('Content-disposition', 'attachment; filename='+ i['txtfile'].filename+'.ofx') # force browser to show "Save as" dialog.

        return strOfx.getvalue() # your blob
