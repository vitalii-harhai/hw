from webargs import fields
from webargs.flaskparser import use_kwargs

from tools.db_connection import db_query
from tools.convert import db_response_one_column_to_list
from tools.convert import db_response_one_result_to_html


@use_kwargs({
    'genre': fields.Str(required=True)
},
    location="query")
def stats_by_city(genre: str):
    genres = db_query('SELECT genres.name FROM genres ;')

    if genre not in db_response_one_column_to_list(genres):
        return 'Genre not found'

    query = db_query('SELECT invoices.BillingCity '
                     'FROM invoices '
                     'JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId '
                     'JOIN tracks ON invoice_items.TrackId = tracks.TrackId '
                     'JOIN genres ON tracks.GenreId = genres.GenreId '
                     'WHERE genres.Name = ? '
                     'GROUP BY invoices.BillingCity '
                     'ORDER BY count(*) DESC '
                     'LIMIT 1;', genre)

    result = db_response_one_result_to_html(query)
    return result
