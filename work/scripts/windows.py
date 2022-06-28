# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:45:07 2022

@author: vific
"""

import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np

v = os.getcwd()
v1 = v.split("\\")
v2 = "\\".join(v1[:-1])
sys.path.append(v2)
os.chdir(v2)

import library
from datetime import datetime, timedelta
from tkinter.ttk import Combobox
from tkinter import messagebox
# from tkcalendar import DateEntry, Calendar


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

library_m = pd.read_excel("./data/library.xlsx")
books =  pd.read_excel("./data/books.xlsx")
id_books =  pd.read_excel("./data/id-name.xlsx")
id_author =  pd.read_excel("./data/id-author.xlsx")
library_cards = pd.read_excel("./data/library-card.xlsx")
rating_place = pd.read_excel('./data/rating-place.xlsx')
genre_shelf = pd.read_excel('./data/genre-shelf.xlsx')
publisher = pd.read_excel('./data/publisher.xlsx')


class MainWindow:
    def __init__(self, width, height, title="Window", resizable=(True, True), icon=None):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+800+50")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
            
            
        self.lbl_result2 = tk.Label(text="0")
        self.lbl_result4 = tk.Label(text="0")
        self.lbl_result5 = tk.Label(text="0")
        self.information = tk.Label(text="0")
        
        self.input_data1 = tk.LabelFrame(text="0")
        self.input_data2 = tk.LabelFrame(text="0")
        self.input_data3 = tk.LabelFrame(text="0")
        self.input_data4 = tk.LabelFrame(text="0")
        self.input_data5 = tk.LabelFrame(text="0")
        self.con = tk.LabelFrame(text="0")
        self.new_note = tk.LabelFrame(text="0")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def open_data_base(self):
        self.win_data_base = tk.Toplevel(self.root)
        self.win_data_base.title("База данных библиотеки")
        self.win_data_base.resizable()
        self.win_data_base.geometry("600x600+800+50")
        self.win_data_base.iconbitmap("./images/book.ico")
        
        def store1():
            """
            Сохранение изменений в исходном DataFrame
            Считываются строки
        
            Returns
            -------
            None.
        
            """
            if (choice.get() == "Издательства"):   
                publisher.loc[len(publisher)] = [self.field_name_pub.get(),
                                                 self.field_city_pub.get(),
                                                 self.field_mail_pub.get()]
                publisher.to_excel("./data/publisher.xlsx", index=False) 
                
            elif (choice.get() == "Авторы"):
                id_author.loc[len(id_author)] = [int(self.field_id_author.get()),
                                                 self.field_name_author.get()]
                id_author.to_excel("./data/id-author.xlsx", index=False) 
                
            elif (choice.get() == "Книги"):                
                for index, row in id_author.iterrows():
                    if (self.field_author == row["Автор"]):
                        p = index
                
                books.loc[len(books)] = [int(self.field_id_book.get()),
                                         p,
                                         self.field_genre.get(),
                                         self.field_pub.get(),
                                         self.field_rate()]
                books.to_excel("./data/books.xlsx", index=False) 
                
            elif (choice.get() == "Студенты"):
                library_cards.loc[len(library_cards)] = [self.field_lib_card.get(),
                                                         self.field_name_student.get(),
                                                         self.field_bith.get()]
                library_cards.to_excel("./data/library-card.xlsx", index=False)
            
            messagebox.showinfo(title="Информация", message="Данные сохранены")
            
        def change():
            lbl1.config(text="Информация из категории " + choice.get())
            
            self.con.destroy()
            self.new_note.destroy()
            
            self.con = tk.LabelFrame(self.win_data_base, text="Информация")
            self.con.pack(side=tk.TOP)
            
            if (choice.get() == "Издательства"):   
                param = pd.read_excel("./data/publisher.xlsx")
                name_col = ["Название", "Город", "Электронная почта"]
            elif (choice.get() == "Авторы"):
                param = pd.read_excel("./data/id-author.xlsx")
                name_col = ["Номер автора", "Автор"]
            elif (choice.get() == "Книги"):
                param1 = pd.read_excel("./data/books.xlsx")
                param2 = pd.merge(param1, id_books)
                param3 = pd.merge(param2, id_author)
                param = pd.DataFrame(param3, columns=['Код книги', 'Название книги', 'Автор', 'Жанр', 'Название издательства', 'Возрастной рейтинг'])
                name_col = ['Код книги', 'Название книги', 'Автор', 'Жанр', 'Название издательства', 'Возрастной рейтинг']
            elif (choice.get() == "Студенты"):
                param = pd.read_excel("./data/library-card.xlsx")
                name_col = ["Номер читательского билета", "Читатель", "Год рождения"]
            
            height1 = param.shape[0]
            width1 = param.shape[1]
            pub1 = np.empty(shape=(height1, width1), dtype="O")
            pub2 = np.empty(shape=(height1, width1), dtype="O")
            
            for i in range(len(name_col)):
                lbl_col = tk.Label(self.con, text=name_col[i])
                lbl_col.grid(row=0, column=i)
                
            for i in range(height1): 
                for j in range(width1): 
                    pub2[i, j] = tk.StringVar()
            
            for i in range(height1): 
                
                for j in range(width1): 
                    pub1[i, j] = tk.Entry(self.con, textvariable = pub2[i, j]) 
                    pub1[i, j].grid (row=i+1, column=j)
                    
            for i in range(height1): 
                for j in range(width1): 
                    cnt = param.iloc[i, j]
                    pub2[i, j].set(str(cnt))
                    
            
            self.new_note = tk.LabelFrame(self.win_data_base, text="Ввод данных о новой записи")
            self.new_note.pack(side=tk.TOP)
            
            if (choice.get() == "Издательства"):   
                lbl_name_pub = tk.Label(self.new_note, text="Название издательства")
                lbl_name_pub.grid(column=0, row=0)
                
                self.field_name_pub = tk.Entry(self.new_note, bd=5)
                self.field_name_pub.grid(column=1, row=0)
                
                lbl_city_pub = tk.Label(self.new_note, text="Город издательства")
                lbl_city_pub.grid(column=0, row=1)
                
                self.field_city_pub = tk.Entry(self.new_note, bd=5)
                self.field_city_pub.grid(column=1, row=1)
                
                lbl_mail_pub = tk.Label(self.new_note, text="Электронная почта издательства")
                lbl_mail_pub.grid(column=0, row=2)
                
                self.field_mail_pub = tk.Entry(self.new_note, bd=5)
                self.field_mail_pub.grid(column=1, row=2)
                
            elif (choice.get() == "Авторы"):
                lbl_id_author = tk.Label(self.new_note, text="Номер автора")
                lbl_id_author.grid(column=0, row=0)
                
                self.field_id_author = tk.Entry(self.new_note, bd=5)
                self.field_id_author.grid(column=1, row=0)
                
                lbl_name_author = tk.Label(self.new_note, text="Автор")
                lbl_name_author.grid(column=0, row=1)
                
                self.field_name_author = tk.Entry(self.new_note, bd=5)
                self.field_name_author.grid(column=1, row=1)
                
            elif (choice.get() == "Книги"):
                lbl_id_book = tk.Label(self.new_note, text="Код книги")
                lbl_id_book.grid(column=0, row=0)
                
                self.field_id_book = tk.Entry(self.new_note, bd=5)
                self.field_id_book.grid(column=1, row=0)
                
                lbl_name_book = tk.Label(self.new_note, text="Название книги")
                lbl_name_book.grid(column=0, row=1)
                
                self.field_name_book = tk.Entry(self.new_note, bd=5)
                self.field_name_book.grid(column=1, row=1)
                
                lbl_author = tk.Label(self.new_note, text="Автор")
                lbl_author.grid(column=0, row=2)
                
                self.field_author = tk.Entry(self.new_note, bd=5)
                self.field_author.grid(column=1, row=2)
                
                lbl_genre = tk.Label(self.new_note, text="Жанр")
                lbl_genre.grid(column=0, row=3)
                
                self.field_genre = tk.Entry(self.new_note, bd=5)
                self.field_genre.grid(column=1, row=3)
                
                lbl_pub = tk.Label(self.new_note, text="Издательство")
                lbl_pub.grid(column=0, row=4)
                
                self.field_pub = tk.Entry(self.new_note, bd=5)
                self.field_pub.grid(column=1, row=4)
                
                lbl_rate = tk.Label(self.new_note, text="Возрастной рейтинг")
                lbl_rate.grid(column=0, row=5)
                
                self.field_rate = tk.Entry(self.new_note, bd=5)
                self.field_rate.grid(column=1, row=5)
                
                
            elif (choice.get() == "Студенты"):
                lbl_lib_card = tk.Label(self.new_note, text="Номер читательского билета")
                lbl_lib_card.grid(column=0, row=0)
                
                self.field_lib_card = tk.Entry(self.new_note, bd=5)
                self.field_lib_card.grid(column=1, row=0)
                
                lbl_name_student = tk.Label(self.new_note, text="Читатель")
                lbl_name_student.grid(column=0, row=1)
                
                self.field_name_student = tk.Entry(self.new_note, bd=5)
                self.field_name_student.grid(column=1, row=1)
                
                lbl_bith = tk.Label(self.new_note, text="Год рождения")
                lbl_bith.grid(column=0, row=2)
                
                self.field_bith = tk.Entry(self.new_note, bd=5)
                self.field_bith.grid(column=1, row=2)
            
            btn_save1 = tk.Button(self.new_note, text='Сохранить', font="Arial 10",
                                  bg='#cdd0d1', command=store1)
            btn_save1.grid(row=6, column=1)
        
        

        
        lbl1 = tk.Label(self.win_data_base, width=35, height=2, bg="#cdd0d1",
                        text="Информация из категории Издательства", font="Arial 20")
        lbl1.pack()

        choice = Combobox(self.win_data_base, state="readonly",
                          values=("Издательства", "Авторы", "Книги", "Студенты"))
        choice.pack(padx=10, pady=10)
        choice.current(0)
        
        btn_set_choise = tk.Button(self.win_data_base, text='Выбрать', font="Arial 10",
                              bg='#cdd0d1', command=change)
        btn_set_choise.pack(padx=1, pady=1)
        
        btn_exit2 = tk.Button(self.win_data_base, text='Выход', font="Arial 10",
                              bg='#cdd0d1', command=self.win_data_base.destroy)
        btn_exit2.pack(padx=5, pady=1)
        
    
    def open_dairy(self):
        self.win_dairy = tk.Toplevel(self.root)
        self.win_dairy.title("Текущий журнал")
        self.win_dairy.resizable(True, True)
        self.win_dairy.geometry("600x600+800+50")
        self.win_dairy.iconbitmap("./images/book.ico")
        library_m = pd.read_excel("./data/library.xlsx")
        
        height = library_m.shape[0]
        width = library_m.shape[1]
        pnt = np.empty(shape=(height, width), dtype="O")
        vrs = np.empty(shape=(height, width), dtype="O")

        lbl1 = tk.Label(self.win_dairy, width=20, height=2, bg="#cdd0d1",
                        text="Журнал библиотеки", font="Arial 20")
        lbl1.pack()
        
        def store():
            """
            Сохранение изменений в исходном DataFrame
            Считываются строки !!!
        
            Returns
            -------
            None.
        
            """
            end_date = datetime.strptime(field_start_date.get(), "%d.%m.%Y") + timedelta(days=30)
            library_m.loc[len(library_m)] = [self.field_library_card.get(),
                                             int(self.field_id_book.get()),
                                             datetime.strptime(field_start_date.get(), "%d.%m.%Y"),
                                             end_date]
            library_m.to_excel("./data/library.xlsx", index=False) 
            messagebox.showinfo(title="Информация", message="Данные сохранены")
            
        def delete_user():
            id_card = self.field_libr_card.get()
            id_book = int(self.field_book_id.get())
            tmp = library_m.copy()
            tmp1 = library_m.copy()
            
            for i, row in tmp.iterrows():
                if row['Номер читательского билета'] == id_card and row['Код книги'] == id_book:
                        tmp1 = tmp.drop([i])
            
            tmp1.to_excel("./data/library.xlsx", index=False) 
            messagebox.showinfo(title="Информация", message="Данные удалены")
        
            
        # Инициализация указателей на буферы
        for i in range(height): 
            for j in range(width): 
                vrs[i, j] = tk.StringVar()

        top = tk.LabelFrame(self.win_dairy, text="Текущий журнал")
        top.pack(side=tk.TOP)
        
        name_col = ["Номер билета", "Код книги", "Дата выдачи", "Дата возврата"]
        for i in range(len(name_col)):
            lbl_col = tk.Label(top, text=name_col[i])
            lbl_col.grid(row=0, column=i)
            
        for i in range(height): 
            for j in range(width): 
                pnt[i, j] = tk.Entry(top, textvariable = vrs[i, j]) 
                pnt[i, j].grid (row=i+1, column=j)
        
        # Заполнение таблицы значениями
        for i in range(height): 
            for j in range(width): 
                cnt = library_m.iloc[i, j]
                vrs[i, j].set(str(cnt))

        # Измененные значения можно затем получить из буферов методом get()
        new_users = tk.LabelFrame(self.win_dairy, text="Ввод данных о новой записи")
        new_users.pack(side=tk.TOP)
        
        lbl_library_card = tk.Label(new_users, text="Выберите номер читательского билета")
        lbl_library_card.grid(column=0, row=0)
        
        choice_list1 = library_cards["Номер читательского билета"].tolist()
        self.field_library_card = Combobox(new_users, state="readonly",
                                   width=20, values=choice_list1)
        self.field_library_card.current(0)
        self.field_library_card.grid(column=1, row=0)
        
        lbl_id_book = tk.Label(new_users, text="Выберите номер книги")
        lbl_id_book.grid(column=0, row=1)
        
        choice_list1 = id_books["Код книги"].tolist()
        self.field_id_book = Combobox(new_users, state="readonly",
                                   width=20, values=choice_list1)
        self.field_id_book.current(0)
        self.field_id_book.grid(column=1, row=1)
        
        lbl_library_card = tk.Label(new_users, text="Введите дату")
        lbl_library_card.grid(column=0, row=2)
        
        field_start_date = tk.Entry(new_users)
        field_start_date.grid(row=2, column=1)
        
        
        btn_save1 = tk.Button(new_users, text='Сохранить', font="Arial 10",
                              bg='#cdd0d1', command=store)
        btn_save1.grid(row=3, column=1)
        
        delete_users = tk.LabelFrame(self.win_dairy, text="Удаление записи")
        delete_users.pack(side=tk.TOP)
        
        lbl_libr_card = tk.Label(delete_users, text="Выберите номер читательского билета")
        lbl_libr_card.grid(column=0, row=0)
        
        choice_list1 = library_m["Номер читательского билета"].tolist()
        self.field_libr_card = Combobox(delete_users, state="readonly",
                                   width=20, values=choice_list1)
        self.field_libr_card.current(0)
        self.field_libr_card.grid(column=1, row=0)
        
        lbl_book_id = tk.Label(delete_users, text="Выберите номер книги")
        lbl_book_id.grid(column=0, row=1)
        
        choice_list2 = library_m["Код книги"].tolist()
        self.field_book_id = Combobox(delete_users, state="readonly",
                                   width=20, values=choice_list2)
        self.field_book_id.current(0)
        self.field_book_id.grid(column=1, row=1)
        
        btn_delete1 = tk.Button(delete_users, text='Удалить', font="Arial 10",
                              bg='#cdd0d1', command=delete_user)
        btn_delete1.grid(row=2, column=1)
        
        btn_exit1 = tk.Button(self.win_dairy, text='Выход', font="Arial 15",
                              bg='#cdd0d1', command=self.win_dairy.destroy)
        btn_exit1.pack()

    def open_options(self):
        self.win_options = tk.Toplevel(self.root)
        self.win_options.title("Опции")
        self.win_options.resizable(True, True)
        self.win_options.geometry("600x600+800+50")
        self.win_options.iconbitmap("./images/book.ico")
        
        def actions():
            if (options.get() == "Доступ по возрастному рейтингу"):
                self.lbl_result4.destroy()
                
                D1 = pd.merge(library_m, library_cards, on="Номер читательского билета")
                D2 = pd.merge(D1, books)
                result4 = library.reports.permissionForStudent(D2, self.field_card.get(), int(self.field_id_book.get()))
                if result4:
                    self.lbl_result4 = tk.Label(self.input_data1, text="Выдача книги разрешена", bg='#9ffa7a')
                else:
                    self.lbl_result4 = tk.Label(self.input_data1, text="Выдача запрещена по закону 'О защите детей от информации, причиняющей вред их здоровью и развитию'",
                                                bg='#fa7a7a')
                self.lbl_result4.grid(column=0, row=3, columnspan=2)
                
            elif (options.get() == "Статус книги"):
                result2 = library.reports.statusOfBook(books, int(self.field_name_book.get()))
                
                height1 = result2.shape[0]
                width1 = result2.shape[1]
                pub1 = np.empty(shape=(height1, width1), dtype="O")
                pub2 = np.empty(shape=(height1, width1), dtype="O")
                
                if (width1 == 1):
                    # date_return = datetime.strptime(str(result2.index[0]), "%d.%m.%Y")
                    
                    name_col = tk.Label(self.input_data2, text="Дата возврата книги")
                    name_col.grid(row=2, column=0)
                    
                    data_col = tk.Label(self.input_data2, text=str(result2.iloc[0, 0]))
                    data_col.grid(row=2, column=1)
                else:
                    name_col = ["Автор", "Код книги", "Название книги", "Жанр", "Издательство", "Рейтинг"]
                    for i in range(len(name_col)):
                        lbl_col = tk.Label(self.input_data2, text=name_col[i])
                        lbl_col.grid(row=3, column=i)
                        
                    for i in range(height1): 
                        for j in range(width1): 
                            pub2[i, j] = tk.StringVar()
                    
                    for i in range(height1): 
                        for j in range(width1): 
                            pub1[i, j] = tk.Entry(self.input_data2, textvariable = pub2[i, j]) 
                            pub1[i, j].grid (row=i+4, column=j)
                            
                    for i in range(height1): 
                        for j in range(width1): 
                            cnt = result2.iloc[i, j]
                            pub2[i, j].set(str(cnt))
                
            elif (options.get() == "Узнать об издательстве"):
                D0 = pd.merge(books, id_author, on="Номер Автора")
                D3 = pd.merge(id_books, D0, on="Код книги")
                D4 = pd.merge(D3, publisher, on="Название издательства")
                
                result5 = library.reports.publisherOfBook(D4, self.field_name_book.get())
                
                height1 = result5.shape[0]
                width1 = result5.shape[1]
                pub1 = np.empty(shape=(height1, width1), dtype="O")
                pub2 = np.empty(shape=(height1, width1), dtype="O")
                
                name_col = ["Название книги", "Автор", "Издательство", "Город",  "Электронная почта"]
                for i in range(len(name_col)):
                    lbl_col = tk.Label(self.input_data3, text=name_col[i])
                    lbl_col.grid(row=3, column=i)
                    
                for i in range(height1): 
                    for j in range(width1): 
                        pub2[i, j] = tk.StringVar()
                
                for i in range(height1): 
                    for j in range(width1): 
                        pub1[i, j] = tk.Entry(self.input_data3, textvariable = pub2[i, j]) 
                        pub1[i, j].grid (row=i+4, column=j)
                        
                for i in range(height1): 
                    for j in range(width1): 
                        cnt = result5.iloc[i, j]
                        pub2[i, j].set(str(cnt))
                
            elif (options.get() == "Книги определенной категории"):
                print("hi")
                
            elif (options.get() == "Состояние читательского билета"):
                self.information.destroy()
                
                information = ""
                condition_card_frame1 = pd.merge(library_m, books, how='left')
                condition_card_frame1.drop(columns=["Жанр", "Название издательства", "Возрастной рейтинг"], axis=1, inplace=True)
                
                condition_card_frame1 = pd.merge(condition_card_frame1, id_books, how='left')
                condition_card_frame1 = pd.merge(condition_card_frame1, id_author, how='left')
                condition_card_frame1 = pd.merge(condition_card_frame1, library_cards, how='left')
                condition_card_frame1.drop(columns=["Номер Автора", "Год рождения"], axis=1, inplace=True)
                result3 = library.pivot_table.studentAndHisBooks(condition_card_frame1, self.field_card.get(), information)
                
                count = result3.shape[0]
                if count < 5:
                    information = f"Возможно взять еще {5-count} книг"
                    self.information = tk.Label(self.input_data5, text=information, bg='#9ffa7a')
                    self.information.grid(column=0, row=2)
                else:
                    information = "Студент взял максимальное количество книг"
                    self.information = tk.Label(self.input_data5, text=information, bg='#fa7a7a')
                    self.information.grid(column=0, row=2)
                
                height1 = result3.shape[0]
                width1 = result3.shape[1]
                pub1 = np.empty(shape=(height1, width1), dtype="O")
                pub2 = np.empty(shape=(height1, width1), dtype="O")
                
                name_col = ["Номер читательского билета", "Код книги", "Дата выдачи", "Дата возврата",  "Название книги", "Автор", "Имя читателя"]
                for i in range(len(name_col)):
                    lbl_col = tk.Label(self.input_data5, text=name_col[i])
                    lbl_col.grid(row=3, column=i)
                    
                for i in range(height1): 
                    for j in range(width1): 
                        pub2[i, j] = tk.StringVar()
                
                for i in range(height1): 
                    for j in range(width1): 
                        pub1[i, j] = tk.Entry(self.input_data5, textvariable = pub2[i, j]) 
                        pub1[i, j].grid (row=i+4, column=j)
                        
                for i in range(height1): 
                    for j in range(width1): 
                        cnt = result3.iloc[i, j]
                        pub2[i, j].set(str(cnt))
            
            
        def chosen_option():
            if (options.get() == "Доступ по возрастному рейтингу"):
                self.input_data1.destroy()
                self.input_data2.destroy()
                self.input_data3.destroy()
                self.input_data4.destroy()
                self.input_data5.destroy()
                
                self.input_data1 = tk.LabelFrame(self.win_options, text="Поле для ввода")
                self.input_data1.pack(side=tk.TOP)
                
                self.card = tk.Label(self.input_data1, text="Выберите номер читательского билета", font="Arial 10")
                self.card.grid(column=0, row=0)
                
                choice_list1 = library_cards["Номер читательского билета"].tolist()
                self.field_card = Combobox(self.input_data1, state="readonly",
                                           width=20, values=choice_list1)
                self.field_card.current(0)
                self.field_card.grid(column=1, row=0)
                
                self.id_book = tk.Label(self.input_data1, text="Выберите номер книги", font="Arial 10")
                self.id_book.grid(column=0, row=1)
                
                choice_list2 = id_books["Код книги"].tolist()
                self.field_id_book = Combobox(self.input_data1, state="readonly", 
                                              width=20, values=choice_list2)
                self.field_id_book.current(0)
                self.field_id_book.grid(column=1, row=1)
                
                
                btn_save3 = tk.Button(self.input_data1, text='Выбрать', font="Arial 10",
                                      bg='#cdd0d1', command=actions)
                btn_save3.grid(column=1, row=2)
                
                
            elif (options.get() == "Статус книги"):
                self.input_data1.destroy()
                self.input_data2.destroy()
                self.input_data3.destroy()
                self.input_data4.destroy()
                self.input_data5.destroy()
                
                self.input_data2 = tk.LabelFrame(self.win_options, text="Поле для ввода")
                self.input_data2.pack(side=tk.TOP)
                
                self.name_book = tk.Label(self.input_data2, text="Выберите номер книги", font="Arial 10")
                self.name_book.grid(column=0, row=0)
                
                choice_list2 = id_books["Код книги"].tolist()
                self.field_name_book = Combobox(self.input_data2, state="readonly", 
                                                width=20, values=choice_list2)
                self.field_name_book.current(0)
                self.field_name_book.grid(column=1, row=0)
                
                btn_save3 = tk.Button(self.input_data2, text='Выбрать', font="Arial 10",
                                      bg='#cdd0d1', command=actions)
                btn_save3.grid(column=1, row=1)
                
                
            elif (options.get() == "Узнать об издательстве"):
                self.input_data1.destroy()
                self.input_data2.destroy()
                self.input_data3.destroy()
                self.input_data4.destroy()
                self.input_data5.destroy()
                
                self.input_data3 = tk.LabelFrame(self.win_options, text="Поле для ввода")
                self.input_data3.pack(side=tk.TOP)
                
                self.name_book = tk.Label(self.input_data3, text="Выберите название книги", font="Arial 10")
                self.name_book.grid(column=0, row=0)
                
                choice_list3 = id_books["Название книги"].tolist()
                self.field_name_book = Combobox(self.input_data3, state="readonly", 
                                                width=20, values=choice_list3)
                self.field_name_book.current(0)
                self.field_name_book.grid(column=1, row=0)
                
                btn_save3 = tk.Button(self.input_data3, text='Выбрать', font="Arial 10",
                                      bg='#cdd0d1', command=actions)
                btn_save3.grid(column=1, row=1)
                
            elif (options.get() == "Книги определенной категории"):
                self.input_data1.destroy()
                self.input_data2.destroy()
                self.input_data3.destroy()
                self.input_data4.destroy()
                self.input_data5.destroy()
                
                self.input_data4 = tk.LabelFrame(self.win_options, text="Поле для ввода")
                self.input_data4.pack(side=tk.TOP)
                
                def clicked1():  
                    
                    S = pd.merge(id_books, books)
                    S = pd.merge(id_author, S)
                    S = pd.merge(S, rating_place)
                    S = S.merge(library_m, how='left', on='Код книги')
                    S.drop(['Номер Автора','Название издательства','Дата выдачи','Дата возврата'],
                            inplace=True, axis=1) 
                    par = [choice.get(), choice_list_l.get()]
                    res_optionsOfBook = library.pivot_table.optionsOfBook(S, par)

                    
                    height1 = res_optionsOfBook.shape[0]
                    width1 = res_optionsOfBook.shape[1]
                    pub1 = np.empty(shape=(height1, width1), dtype="O")
                    pub2 = np.empty(shape=(height1, width1), dtype="O")
                    
                    for i in range(height1): 
                        for j in range(width1): 
                            pub2[i, j] = tk.StringVar()
                    
                    for i in range(height1): 
                        for j in range(width1): 
                            pub1[i, j] = tk.Entry(self.input_data4, textvariable = pub2[i, j]) 
                            pub1[i, j].grid (row=i+3, column=j)
                            
                    for i in range(height1): 
                        for j in range(width1): 
                            cnt = res_optionsOfBook.iloc[i, j]
                            pub2[i, j].set(str(cnt))

                def clicked():  
                    choice_list_l.grid(column=1, row=1)
                    choice_list_l.current(0)
                    btn1.grid(column=3, row=1)
                    
                    v = choice.get()
                    
                    if (v == "Автор"):
                        choice_list = id_author[v].tolist()
                    elif (v == "Жанр"):
                        choice_list = genre_shelf[v].tolist()
                
                    choice_list_l["values"] = choice_list
                    choice_list_l.current(0)
                    
                lbl = tk.Label(self.input_data4, text="Выберите параметр для поиска") 
                lbl.grid(column=0, row=0) 
                choice = Combobox(self.input_data4, state="readonly", 
                                  width=20, values=("Автор", "Жанр"))
                choice.grid(column=1, row=0)
                choice.current(0)
                
                v = choice.get()
                if (v == "Автор"):
                    choice_list = id_author[v].tolist()
                elif (v == "Жанр"):
                    choice_list =  genre_shelf[v].tolist()
                choice_list_l = Combobox(self.input_data4, state="readonly", 
                                         width=20, values=choice_list)
                choice_list_l.current(0)
                
                btn = tk.Button(self.input_data4, text="Подтвердить", command=clicked)  
                btn.grid(column=3, row=0)  
                
                btn1 = tk.Button(self.input_data4, text="Поиск", command=clicked1)
                
            elif (options.get() == "Состояние читательского билета"):
                self.input_data2.destroy()
                self.input_data3.destroy()
                self.input_data4.destroy()
                self.input_data1.destroy()
                self.input_data5.destroy()
                
                self.input_data5 = tk.LabelFrame(self.win_options, text="Поле для ввода")
                self.input_data5.pack(side=tk.TOP)
                
                self.card = tk.Label(self.input_data5, text="Введите номер читательского билета", font="Arial 10")
                self.card.grid(column=0, row=0)
                
                choice_list4 = library_cards["Номер читательского билета"].tolist()
                self.field_card = Combobox(self.input_data5, state="readonly", 
                                           width=20, values=choice_list4)
                self.field_card.current(0)
                self.field_card.grid(column=1, row=0)
                
                btn_save3 = tk.Button(self.input_data5, text='Выбрать', font="Arial 10",
                                      bg='#cdd0d1', command=actions)
                btn_save3.grid(column=1, row=1)
             
                       
        lbl1 = tk.Label(self.win_options, width=20, height=2, bg="#cdd0d1",
                    text="Выберите опцию", font="Arial 20")
        lbl1.pack()   
        
        options = Combobox(self.win_options, state="readonly", 
                           values=("Доступ по возрастному рейтингу", "Статус книги",
                                   "Узнать об издательстве", "Книги определенной категории",
                                   "Состояние читательского билета"), width=50)
        options.pack(padx=10, pady=10)
        options.current(0)
        
        btn_save2 = tk.Button(self.win_options, text='Выбрать', font="Arial 10",
                              bg='#cdd0d1', command=chosen_option)
        btn_save2.pack(padx=1, pady=1)

    def draw_widgets(self):
        self.header = tk.Label(self.root, text="Библиотека", bg="#cdd0d1", height=2, font="Arial 30")
        self.header.place(relwidth=1)

        self.btn_data_base = tk.Button(self.root, width=30, height=2, text="Базы данных библиотеки",
                                       font="Arial 20", bg="#cdd0d1", relief="groove", bd=8,
                                       command=self.open_data_base)
        self.btn_data_base.place(relx=0.2, rely=0.3)

        self.btn_dairy = tk.Button(self.root, width=30, height=2, text="Текущий журнал",
                                   font="Arial 20", bg="#cdd0d1", relief="groove", bd=8,
                                   command=self.open_dairy)
        self.btn_dairy.place(relx=0.2, rely=0.5)

        self.btn_options = tk.Button(self.root, width=30, height=2, text="Опции",
                                   font="Arial 20", bg="#cdd0d1", relief="groove", bd=8,
                                   command=self.open_options)
        self.btn_options.place(relx=0.2, rely=0.7)
    


if __name__ == "__main__":
    window = MainWindow(800, 800)
    window.run()
    window.open_data_base()
    window.open_dairy()
    window.open_options()