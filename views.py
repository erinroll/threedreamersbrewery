from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Product, Category, Range, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db


#use blueprint
bp = Blueprint('main', __name__)

#get index page
@bp.route('/')
def index ():
    products = Product.query.filter(Product.category_id)
    return render_template('index.html', products = products)

#get beer product page
@bp.route('/beer/<int:productid>/')
def product_beer(productid):
    products = Product.query.filter(Product.id)
    return render_template( 'product_beer.html', productid = productid, products = products)

#get merch product page
@bp.route('/merch/<int:productid>/')
def product_merch(productid):
    products = Product.query.filter(Product.id)
    return render_template( 'product_merch.html', productid = productid, products = products)

#get cartpage
@bp.route('/cart', methods=['POST','GET'])
def order():

    product_id = request.values.get('product_id')
    
    # get order if there is one already
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        
    else:
        # no order found
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstName='', surname='', email='', phone='', totalcost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('Failed at creating a new order. Please try again.')
            order = None

    # calculate totalcost
    totalcost = 0
    if order is not None:
        for product in order.products:
            totalcost = totalcost + product.price

    # calculate total GST
    totalGst = 0
    if order is not None:
        for product in order.products:
            totalGst = totalcost * 0.1

    # calculate subtotal
    subtotalcost = 0
    if order is not None:
        for product in order.products:
            subtotalcost = totalcost - totalGst
    
    # adding item to cart
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was a problem adding the item to your basket'
            return redirect(url_for('main.order'))

        # can not add more than one of each item to cart    
        else:
            flash('Item already in basket')
            return redirect(url_for('main.order'))

    return render_template('cart.html', order = order, subtotalcost = subtotalcost, totalcost = totalcost, totalGst = totalGst)

# delete all items in cart
@bp.route('/deleteorder/')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All cart items removed')
    return redirect(url_for('main.index'))

# delete single product item from cart 
@bp.route('/deleteorderitem/', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'There was a problem deleting item from order'
    return redirect(url_for('main.order'))

# submit order via checkout
# no credit card validation - only there to show style in form
@bp.route('/checkout/', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        totalcost = 0
        for product in order.products:
            totalcost = totalcost + product.price
        order.totalcost = totalcost
       
        if form.validate_on_submit():
            order.status = True
            order.firstName = form.firstName.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.streetAddress = form.streetAddress.data
            order.suburb = form.suburb.data
            order.state = form.state.data
            order.postcode = form.postcode.data
            order.country = form.country.data
            order.ccName = form.ccName.data
            order.ccNumber = form.ccNumber.data
            order.ccExpDate = form.ccExpDate.data
            order.CCV = form.CCV.data
            order.totalcost = order.totalcost
            
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your order! An email confirmation will be with you soon.')
                return redirect(url_for('main.index'))
            except:
                return 'There was a problem completing your order'
    return render_template('checkout.html', form = form, order = order)