# Deze file is zelf gemaakt. Dit is de hoofd app.

from flask import Flask             # We are importing this `Flask`-class.
from flask import render_template   # De `render_template`-functie is om templates te gebruiken in Flask.
from flask import url_for           # This is a function that makes it easier to change afterwards the URL-locaion. See `URL BUILDING`, Page 12.
from flask import flash             # Easy way a sent one time alert.
from flask import redirect          # Om een gebruiker na het succesvol inloggen direct te redirecten.

# Omdat je wtf_forms gebruikt, moet je de zelfgemaakte Classes importeren van je zelfgemaakte `forms.py`-file:
from forms import RegistrationForm, LoginForm # De `RegistrationForm` en `LoginForm` zijn zelfgekozen.

app = Flask(__name__)               # We are making an instanse called `app` of this `Flask`-class. With `__name__`, it is default Python and it knows where to look for static files and templates.

app.config['SECRET_KEY'] = 'just_a_temp_secret_key' # You need this for CSRF-protection (Cross Site Request Forgery) in Forms. You  can add some random numbers yourself (hint: use python for that)

# Dit wordt wat dummy data, aangezien we nog geen database hebben.
posts = [
    {
        'author' : 'Dion Dresschers',
        'title' : 'Blog Post 1',
        'content' : 'Eerste bericht',
        'date_posted': '2021-03-08',
    },
    {
        'author' : 'Henk Heemstede',
        'title' : 'Blog Twee',
        'content' : 'Hier staat info in bericht',
        'date_posted': '2021-03-09',
    }
]

@app.route("/")                     # This is the route, this is a route decorator. The `route` is the method.
@app.route("/home")    
def home():                        # This is the function
    return render_template('home.html', posts=posts, title="ja een titelatuur!")            # De eerste `posts` wordt gebruikt in de Jinja2 template, de tweede `posts`, is de posts variabele hierboven. # De `title` is ook zelfgekozen en wordt gebruikt in de Jinja2 als `title`.
##    return("<h1>Hello World!</h1>")          # This will be returned

@app.route("/about")
def about():
    return render_template('about.html', title="ABOUT!")
##    return("About page")

@app.route("/register", methods=['GET', 'POST']) # Anders werkt het formulier niet, dan krijg je iets van een melding "Method Not Allowed The method is not allowed for the requested URL."
def register():
    # Create an instance of the Form of the Class that you've created in `forms.py`:
    form = RegistrationForm()
    
    # Hieronder de valdatie voor het formulier:
    if form.validate_on_submit(): # We gaan Flash-messages gebruiken, deze moeten we dus importeren. De `.validate_on_submit() is dus een standaard method.`
        flash(f'Account created for {form.username.data}!', 'success') # Python 3.6 support f-strings. # The 'success' is a Bootstrap message we can sent with the Flask flash. # De template moet ook nog aangepast worden, zodat deze flash messages kan weergeven.
        return redirect(url_for('home')) # Als de validatie goed is gedaan, redirect de gebruiker naar de url_for, dat is `home`. De `home` is de functie genaamd `home` voor de homepagina.
    return render_template('register.html', title='Register', form=form) # Voeg ook de form toe. De eerste `form`, wordt gebruikt in de template. De tweede `form` is de instance die je hierboven gecreerd hebt met `form = RegistrationForm()`

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Create an instance of the Form of the Class that you've created in `forms.py`:
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password': # The `data`, is the data that is submitted in the form by the user.
            flash('You have been logged in!', 'success') # The first argument is the setting, the second argument is the Bootstrap.
            return redirect(url_for('home')) # Go to home
        else:
            flash('Login unsuccesful. Please check again', 'danger')
    # This is going to be some dummy code to simulate a succesful login

    return render_template('login.html', title='Login', form=form) # Voeg ook de form toe. De eerste `form`, wordt gebruikt in de template. De tweede `form` is de instance die je hierboven gecreerd hebt met `form = RegistrationForm()`

#if __name__ == "__main__":          # If we don't run this directly, but import than the __name__ will be something different, and then the Debug will not be set.
#    app.run(debug=True)             # Run Flask Debug. With this, you can also run this Flask directly via `python3 fopen-lms.py`

