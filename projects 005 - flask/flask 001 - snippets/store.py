import flask from Flask

app = Flask(__name__)

stores = [
    {
        'name': "My Store",
        'items' : [
            {
                "name":"My Item",
                "price":16.00
            }

        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    pass
@app.route("/store/<string:name>/item", methods=['POST'])
def create_items_in_store():
    pass

@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    pass


app.run(port=9999)