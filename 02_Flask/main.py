from flask import Flask

import route_calculate_average
import route_generate_password
import route_generate_students
import route_all_info_about_track
import route_get_bitcoin_value
import route_calculate_hours
import route_get_sales
import settings
app = Flask(__name__)


@app.route('/')
def index_page():
    return ('<a href="/generate-password"> Generate your password</a></br>'
            '<a href="/calculate-average"> Calculate high and weight</a></br>'
            '<a href="/generate-students"> Generate students</a></br>'
            '<a href="/get-bitcoin-value"> Get bitcoin rate</a></br>'
            '<a href="/get-sales"> Calculate sales by country</a></br>'
            '<a href="/get-all-info-about-track"> Get all info about track</a></br>'
            '<a href="/calculate-all-tracks-hours"> Calculate all track hours</a></br>')


@app.route('/generate-password')
def generate_password_page():
    return route_generate_password.generate_password()


@app.route('/calculate-average')
def calculate_average_page():
    return route_calculate_average.calculate_average()


@app.route('/generate-students')
def generate_students_page():
    return route_generate_students.generate_students()


@app.route('/get-bitcoin-value')
def get_bitcoin_value_page():
    return route_get_bitcoin_value.get_bitcoin_value()


@app.route('/get-sales')
def get_sale_page():
    return route_get_sales.order_price()


@app.route('/get-all-info-about-track')
def get_all_info_about_track_page():
    return route_all_info_about_track.get_all_info_about_track()


@app.route('/calculate-all-tracks-hours')
def calculate_hours_all_tracks_page():
    return route_calculate_hours.calculate_all_track_hours()


if __name__ == '__main__':
    app.run(debug=True)
