import web
render= web.template.render("/home/code/")
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        datos=None
        
        datos={
      
            "Palabra":"Palabra buscada",
            "Significado":"Significado" ,
            
          }
        return render.index(datos)
if __name__ == "__main__":
    app.run()
