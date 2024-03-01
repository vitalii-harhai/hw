import pandas as pd


def calculate_average(file='hw.csv') -> str:
    """
    Calculates the average height and weight from csv file containing <index>, <height>, <weight>
    :param file: path to csv file
    :return: tuple average height and weight
    """
    data = pd.read_csv(file, index_col=0)

    height = data.columns[0]
    weight = data.columns[1]
    rows = data.shape[0]

    sum_height = data[height].sum()
    sum_weight = data[weight].sum()

    average_height = round(sum_height / rows, 2)
    average_weight = round(sum_weight / rows, 2)

    return f'Average height = {average_height}, average weight = {average_weight}'
