from collections import Counter, OrderedDict
from functools import wraps
from requests import get


def cache(max_limit=64):
    """
    Decorator to cache functions result using LFU method
    Key - function arguments like tuple
    Using two dictionaries, one (Counter) - {key: count of used} and second (OrderedDict) - {key: function result}
    :param max_limit: cache size
    :return: decorated function
    """
    def internal(f):
        @wraps(f)
        def deco(*args, **kwargs):

            cache_key = (args, tuple(kwargs.items()))

            if cache_key in deco.keys:
                deco.keys.update({cache_key})
                return deco.cache[cache_key]

            result = f(*args, **kwargs)

            if len(deco.keys) >= max_limit:
                delete_element = min(deco.keys, key=lambda x: deco.keys[x])
                deco.keys.pop(delete_element)
                deco.cache.pop(delete_element)

            deco.keys.update({cache_key})
            deco.cache.update({cache_key: result})

            return result

        deco.keys = Counter()
        deco.cache = OrderedDict()

        return deco

    return internal


@cache(3)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    response = get(url)
    return response.content[:first_n] if first_n else response.content
