"""
The flask application package.
"""
from flask import render_template
from dummy.config import connex_app, app
from dummy.build_database import create_db
from dummy.rate import read_rate_by_name, read_rate_by_rate

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yml', strict_validation=True,
                   validate_responses=True, )


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    data = read_rate_by_rate()
    print(data)
    return render_template('home.html', data=data)


create_db()

if __name__ == '__main__':
    connex_app.run(debug=True)
