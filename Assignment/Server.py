from flask import (Flask, Response, request, render_template, make_response,
                   redirect)
from flask.ext.restful import Api, Resource, reqparse, abort
import os
import json
import string
import random
from functools import wraps
from datetime import datetime

#Load catalog json file as data
with open('catalog.json') as data:
    data = json.load(data)

#Load order json file as data
with open('order.json') as mydata:
    mydata = json.load(mydata)

#print data['Categories']['Fruit']['products'][0]
    
item_parser = reqparse.RequestParser()
item_parser.add_argument(
    'name', type=str, required=True)
item_parser.add_argument(
    'quantity', type=int, default=1, required=True)
item_parser.add_argument(
    'link', type=str, required=True) 
    
#Define catalog resource
class Catalog(Resource):
    def get(self):
        return make_response(render_template('Item Catalog.html', categories=data['Categories']), 200)

#Define category resource
class Category(Resource):
    def get(self, category):
        for c in data['Categories']:
            if category.lower() == str(c).lower():
                return make_response(render_template('Category.html', products=data['Categories'][c]), 200)
        return make_response("404 - The requested category could not be found. ", 404)

#Define item resource           
class Item(Resource):
    def get(self, category, item):
        for c in data['Categories']:
            if category.lower() == str(c).lower():
                products = data['Categories'][c]['products']
                for p in products:
                    if item.lower() == str(p['name']).lower():
                        return make_response(render_template('Item.html', item=data['Categories'][c]['products'][products.index(p)]))
        return make_response("404 - The requested item could not be found. ", 404)

#Define payment resource
class Payment(Resource):
    def get(self):
        return make_response(render_template('Payment.html'), 200)

#Define order resource
class Order(Resource):
    def get(self):
        return make_response(render_template('Order.html', items=mydata['Ordered']), 200)
        
    def post(self):
        item = item_parser.parse_args()
        for i in mydata['Ordered']:
            if item['name'] == i['name']:
                items = mydata['Ordered']
                mydata['Ordered'][items.index(i)]['quantity'] += 1
        ordered_item = {
            "name" : item['name'],
            "quantity" : item['quantity'],
            "link" : item['link']
        }
        mydata['Ordered'].append(ordered_item)
        return make_response(render_template('Order.html', items=mydata['Ordered']), 201)

app = Flask(__name__)
api = Api(app)
api.add_resource(Catalog, '/catalog')
api.add_resource(Category, '/catalog/<string:category>')
api.add_resource(Item, '/catalog/<string:category>/<string:item>')
api.add_resource(Payment, '/payment')
api.add_resource(Order, '/order')

@app.route('/')
def index():
    return redirect(api.url_for(Catalog), code=303)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)