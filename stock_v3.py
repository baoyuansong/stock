import web
import json

urls = (
    '/stock/list', 'StockList',
)
app = web.application(urls, globals())
class StockList:
    def GET(self):
        content=['toothpaste zhonghua 2', 'toothbrush jiajieshi 3', 'dental floss korea 4']
        return json.dumps(content)

if __name__ == "__main__":
    app.run()
