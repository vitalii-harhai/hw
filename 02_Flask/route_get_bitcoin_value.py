import httpx
from webargs import fields, validate
from webargs.flaskparser import use_args

import settings


@use_args({'currency': fields.Str(required=False, validate=lambda value: value != '', load_default='USD'),
           'count': fields.Float(required=False, validate=validate.Range(min=0.0000001, max=100), load_default=1.0)},
          location='query')
def get_bitcoin_value(args: dict) -> str:
    """
    Displays the bitcoin rate for the given currency from GET-parameter <currency>
    :param args: arguments from request
    :return:
    """

    currency = args.get('currency')
    symbol_currency = ''
    count = args.get('count')
    result = ''

    currencies_from_api = httpx.get(f'{settings.URL_SUPPORTED_CURRENCIES}')

    if currencies_from_api.status_code == httpx.codes.OK:
        data_from_api = currencies_from_api.json()['data']
        for item in data_from_api:
            if item['code'] == currency:
                symbol_currency = item['symbol']
                break

    response_from_api = httpx.get(f'{settings.URL_BITCOIN_COURSE}{currency}')

    if response_from_api.status_code == httpx.codes.OK:
        data_from_api = response_from_api.json()
        rate = round(float(data_from_api.get('rate')), 2)
        result = f'<p> {count} BTC = {rate * count} {symbol_currency} </p>'

    return result
