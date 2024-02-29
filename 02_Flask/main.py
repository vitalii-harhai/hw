from flask import Flask

import route_generate_password
import route_calculate_average

app = Flask(__name__)


@app.route('/')
def index_page():
    return ('<a href="/generate-password"> Generate your password</a></br>'
            '<a href="/calculate-average"> Calculate high and weight</a>')


@app.route('/generate-password')
def generate_password_page():
    return route_generate_password.generate_password()


@app.route('/calculate-average')
def calculate_average_page():
    return route_calculate_average.calculate_average()


if __name__ == '__main__':
    app.run(debug=True)
