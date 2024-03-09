from tools.db_connection import db_query
from tools.convert import db_response_one_result_to_html


def calculate_all_track_hours() -> str:
    """
    Calculate all track hours
    :return: string with hours, minutes and seconds in html format
    """
    query = ('SELECT \'Hours - \' || CAST(sum(tracks.Milliseconds) / 3600000 AS VARCHAR), '
             '\'Minutes - \' || CAST(sum(tracks.Milliseconds) % 3600000 / 60000  AS VARCHAR), '
             '\'Seconds - \' || CAST(sum(tracks.Milliseconds) % 60000 / 1000 AS VARCHAR) '
             'FROM tracks;')

    result = db_query(query)

    return db_response_one_result_to_html(result)
