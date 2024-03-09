def db_response_one_column_to_list(db_response: list[tuple]) -> list:
    """
    Converts a database response from [(x,), (y,), (x,)] to [x, y, z]
    :param db_response: response from database in format list(tuple(Any))
    :return: list of values from database response
    """
    result_list = []

    for row in db_response:
        result_list.append(row[0])

    return result_list


def db_response_to_html(db_response: list[tuple]) -> str:
    """
    Converts a database response from [(x, x1), (y, y1)] to string 'x, x1<br>y, y1<br>'
    :param db_response: response from database in format list(tuple(Any))
    :return: string of list of values from database response in html format
    """
    result_str = ''

    for row in db_response:
        temp_str = [str(item) for item in row]
        result_str += f"{', '.join(temp_str)}<br>"

    return result_str


def db_response_one_result_to_html(db_response: list[tuple]) -> str:
    """
    Converts a database response from [(x, y, z)] to string 'x<br>y<br>z<br>'
    :param db_response:
    :return: string of values from database response
    """
    result_str = ''

    for item in db_response[0]:
        result_str += f"{str(item)}<br>"

    return result_str
