import web

urls = (
    '/hello', 'Index'
)

render = web.template.render('templates/', base="layout")
app = web.application(urls, globals())

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet=None, datafile={}})
        greeting = "%s, %s" % (form.greet, form.name)
        datafile = form.datafile
        return render.index(greeting=greeting, datafile=datafile)

if __name__ == "__main__":
    app.run()
