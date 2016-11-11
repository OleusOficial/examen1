import web
import json


render = web.template.render('views/')
urls = ('/', 'index')

class index:
    def GET(self ): 
        return render.index( )      
         
if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()  