import web
import json


render = web.template.render('views/')
urls = ('/(.*)', 'index')

class index:
    def GET(self, data):
        data = []
        with open('data.json', 'r') as file:
            temp_data = json.load(file)
            data = temp_data['results']
        return render.index(data)      
         
if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()  