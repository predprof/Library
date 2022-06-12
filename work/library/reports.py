# -*- coding: utf-8 -*-
"""
Данный файл содержит функции, которые сосотавляют отчеты для пользователя

"""

import pandas as pd

def permissionForStudent(database: pd.DataFrame, libraryCard: str, idBook: int) -> bool:
    """
    Разрешение на выдачу книги для читателя по возрастному рейтингу
    ----------
    database : pd.DataFrame
        База с данными.
    libraryCard : str
        Номер читательского билета.
    idBook : int
        Код желаемой книги.

    Returns
    -------
    bool
        True: Разрешено
        False: Отказано.
    """

def statusOfBook(database: pd.DataFrame, nameBook: str) -> pd.DataFrame:
    """
    Данные об интерисующей книге
    ----------
    database : pd.DataFrame
        База с данными.
    nameBook : str
        Название книги.

    Returns
    -------
    pd.DataFrame
        Таблица с данными о книге 

    """
    
def publisherOfBook(database: pd.DataFrame, nameBook: str) -> pd.DataFrame:
    """
    Информация об издательстве книги
    ----------
    database : pd.DataFrame
        База с данными.
    nameBook : str
        Название книги.

    Returns
    -------
    pd.DataFrame
        Таблица с данными об издательстве

    """