from app import db

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    date_of_birth = db.Column(db.Date)
    address = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    postcode = db.Column(db.String)
    language = db.Column(db.String)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    category_id = db.Column(db.String)
    price = db.Column(db.Numeric)
    ingredients = db.Column(db.String)
    image_url = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    steps = db.Column(db.Text, nullable=False)
    region = db.Column(db.String(50), nullable=True)
    duration = db.Column(db.Integer)

class Rating(db.Model):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())

    # Relationship to Customer
    customer = db.relationship('Customer', backref='ratings')
    recipe = db.relationship('Recipe', backref='ratings')


class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)

    user = db.relationship('Customer', backref='favorites', lazy=True)
    recipe = db.relationship('Recipe', backref='favorites', lazy=True)

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    added_at = db.Column(db.DateTime, default=db.func.now())

class PurchasedRecipe(db.Model):
    __tablename__ = 'purchased_recipes'
    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    purchased_at = db.Column(db.DateTime, default=db.func.now())

    # Relationship to access the Recipe details easily
    recipe = db.relationship('Recipe', backref='purchases')

class ContactFormSubmission(db.Model):
    __tablename__ = 'contact_form_submissions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=db.func.now())
