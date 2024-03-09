from webargs import fields
from webargs.flaskparser import use_kwargs

from tools.convert import db_response_one_column_to_list
from tools.convert import db_response_to_html
from tools.db_connection import db_query


@use_kwargs({
    'country': fields.Str(required=False, missing=None)
    },
    location='query')
def order_price(country) -> str:
    """
    Calculate sales by country
    If parameter <country> is not provided, return sales by all countries
    :param country: country name
    :return: html string with <country> <sales>
    """

    countries = db_query('SELECT BillingCountry '
                         'FROM invoices '
                         'GROUP BY BillingCountry')

    countries = db_response_one_column_to_list(countries)

    query = 'SELECT BillingCountry, sum(Total) FROM invoices '

    if country and country in countries:
        query += f' WHERE BillingCountry = "{country}" '

    query += 'GROUP BY BillingCountry;'
    result = db_query(query)

    return db_response_to_html(result)
