# -*- coding: utf-8 -*-
"""
Данный файл содержит функции, которые строят сводные таблицы для пользователя

"""

import pandas as pd

def optionsOfBook(database: pd.DataFrame, nameOfOption: list) -> pd.pivot_table:
    """
    Варианты книг по заданным характеристикам
    ----------
    database : pd.DataFrame
        База с данными.
    nameOfOption : list
        Список критериев.

    Returns
    -------
    pd.pivot_table
        Сводная таблица.
    """

def studentAndHisBooks(database: pd.DataFrame, libraryCard: str) -> pd.pivot_table:
    """
    Наличие книг у студента
    ----------
    database : pd.DataFrame
        База с данными.
    libraryCard : str
        Номер читательского билета.

    Returns
    -------
    pd.pivot_table
        Сводная таблица по данным о книгах у студента

    """

