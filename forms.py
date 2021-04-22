from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, email


#form used in checkout
class CheckoutForm(FlaskForm):
    firstName = StringField("First name", validators=[InputRequired()])
    surname = StringField("Surname", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), email()])
    phone = StringField("Phone number", validators=[InputRequired()])
    streetAddress = StringField("Street address", validators=[InputRequired()])
    suburb = StringField("Suburb", validators=[InputRequired()])
    state = StringField("State", validators=[InputRequired()])
    postcode = StringField("Postcode", validators=[InputRequired()])
    country = StringField("Country", validators=[InputRequired()])
    ccName = StringField("Name on Credit Card", validators=[InputRequired()])
    ccNumber = StringField("Credit Card Number", validators=[InputRequired()])
    ccExpDate = StringField("Expiry Date", validators=[InputRequired()])
    CCV = StringField("CCV", validators=[InputRequired()])
    submit = SubmitField("Submit Payment")

