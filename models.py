from . import db

#class for  products
class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default = 'can_pale_ale.jpg')
    abv = db.Column(db.String(60), nullable=False)
    ibu = db.Column(db.String(60), nullable=False)
    malt = db.Column(db.String(60), nullable=False)
    hops = db.Column(db.String(60), nullable=False)
    appearance = db.Column(db.String(60), nullable=False)
    aroma = db.Column(db.String(60), nullable=False)
    flavour = db.Column(db.String(60), nullable=False)
    body = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(60), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    range_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, ABV: {}, IBU: {}, Malt: {}, Hops: {}, Appearance: {}, Aroma: {}, Flavour: {}, Body: {}, Price: {}, Size: {}\n"
        str = str.format(self.id, self.name, self.description, self.image, self.abv, self.ibu, self.malt, self.hops, self.appearance, self.aroma, self.flavour, self.body, self.price, self.size)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id',db.Integer,db.ForeignKey('products.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'product_id') )

#class for to categorise products
class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
        
    def __repr__(self):
        str = "Id: {}, Name: {}\n" 
        str =str.format( self.id, self.name)
        return str


#class for to categorise beer
class Range(db.Model):
    __tablename__='ranges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
        
    def __repr__(self):
        str = "Id: {}, Name: {}\n" 
        str =str.format( self.id, self.name)
        return str


#class for orders
class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstName = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    streetAddress = db.Column(db.String(128))
    suburb = db.Column(db.String(128))
    state = db.Column(db.String(32))
    postcode = db.Column(db.String(128))
    country = db.Column(db.String(128))
    ccName = db.Column(db.String(32))
    ccNumber = db.Column(db.String(32))
    ccExpDate = db.Column(db.String(32))
    CCV = db.Column(db.String(32))
    subtotalcost = db.Column(db.Float)
    totalGst =db.Column(db.Float)
    totalcost = db.Column(db.Float)
    products = db.relationship("Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Street Address: {}, Suburb: {}, State: {}, Postcode: {}, Country: {}, CC Name: {}, CC Number: {},CC Exp Date: {}, CCV: {}, Total GST: {} Subtotal {}, Total Price: {}\n" 
        str = str.format( self.id, self.status,self.firstName,self.surname, self.email, self.phone, self.streetAddress, self.suburb, self.state, self.postcode, self.country, self.ccName, self.ccNumber, self.ccExpDate, self.CCV, self.totalGst, self.subtotalcost, self.totalcost)
        return str