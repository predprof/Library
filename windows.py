# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:45:07 2022

@author: vific
"""

import os
import tkinter as tk
import pandas as pd
import numpy as np
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import DateEntry, Calendar
os.chdir("C:/work")

library = pd.read_excel("./data/library.xlsx")
height = library.shape[0]
width = library.shape[1]
pnt = np.empty(shape=(height, width), dtype="O")
vrs = np.empty(shape=(height, width), dtype="O")


# library = pd.read_excel("./data/library.xlsx")
# height = library.shape[0]
# width = library.shape[1]

# name1 = ["Номер читательского билета", "Код книги", "Дата выдачи", "Дата возврата"]
# name_columns1 = np.empty(shape=(height, width), dtype="O")

class MainWindow:
    def __init__(self, width, height, title="Window", resizable=(True, True), icon=None):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+800+50")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def open_data_base(self):
        self.win_data_base = tk.Toplevel(self.root)
        self.win_data_base.title("База данных библиотеки")
        self.win_data_base.resizable()
        self.win_data_base.geometry("600x600+800+50")
        
        def change():
            lbl1.config(text="Информация из категории " + choice.get())
            
            con = tk.LabelFrame(self.win_data_base, text="Информация")
            con.pack(side=tk.TOP)
            
            if (choice.get() == "Издательства"):   
                param = pd.read_excel("./data/publisher.xlsx")
            elif (choice.get() == "Авторы"):
                param = pd.read_excel("./data/id-author.xlsx")
            elif (choice.get() == "Книги"):
                param = pd.read_excel("./data/books.xlsx")
            elif (choice.get() == "Студенты"):
                param = pd.read_excel("./data/library-card.xlsx")
            height1 = param.shape[0]
            width1 = param.shape[1]
            pub1 = np.empty(shape=(height1, width1), dtype="O")
            pub2 = np.empty(shape=(height1, width1), dtype="O")
            
            for i in range(height1): 
                for j in range(width1): 
                    pub2[i, j] = tk.StringVar()
            
            for i in range(height1): 
                for j in range(width1): 
                    pub1[i, j] = tk.Entry(con, textvariable = pub2[i, j]) 
                    pub1[i, j].grid (row=i, column=j)
                    
            for i in range(height1): 
                for j in range(width1): 
                    cnt = param.iloc[i, j]
                    pub2[i, j].set(str(cnt))
            

        lbl1 = tk.Label(self.win_data_base, width=35, height=2, bg="#cdd0d1",
                        text="Информация из категории Издательства", font="Arial 20")
        lbl1.pack()

        choice = Combobox(self.win_data_base, values=("Издательства", "Авторы", "Книги", "Студенты"))
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
            library.loc[len(library)] = [field_library_card.get(),
                                         field_id_book.get(),
                                         field_start_date.get(),
                                         field_end_date.get()]
            library.to_excel("./data/library.xlsx", index=False) 
            messagebox.showinfo(title="Информация", message="Данные сохранены")
            
        # Инициализация указателей на буферы
        for i in range(height): 
            for j in range(width): 
                vrs[i, j] = tk.StringVar()

        top = tk.LabelFrame(self.win_dairy, text="Текущий журнал")
        top.pack(side=tk.TOP)
        
        
        for i in range(height): 
            for j in range(width): 
                pnt[i, j] = tk.Entry(top, textvariable = vrs[i, j]) 
                pnt[i, j].grid (row=i, column=j)
        
        # Заполнение таблицы значениями
        for i in range(height): 
            for j in range(width): 
                cnt = library.iloc[i, j]
                vrs[i, j].set(str(cnt))

        # Измененные значения можно затем получить из буферов методом get()
        new_users = tk.LabelFrame(self.win_dairy, text="Ввод данных о новой записи")
        new_users.pack(side=tk.TOP)
        
        field_library_card = tk.Entry(new_users, bd=10)
        field_library_card.grid(row=0, column=0)
        
        field_id_book = tk.Entry(new_users, bd=10)
        field_id_book.grid(row=0, column=1)
        
        field_start_date = DateEntry(new_users, bd=10)
        field_start_date.grid(row=0, column=2)
        
        field_end_date = DateEntry(new_users, bd=10)
        field_end_date.grid(row=0, column=3)
        
        btn_save1 = tk.Button(new_users, text='Сохранить', font="Arial 15",
                              bg='#cdd0d1', command=store)
        btn_save1.grid(row=1, column=1)

        btn_exit1 = tk.Button(new_users, text='Выход', font="Arial 15",
                              bg='#cdd0d1', command=self.win_dairy.destroy)
        btn_exit1.grid (row=1, column=2)

    def open_options(self):
        self.win_options = tk.Toplevel(self.root)
        self.win_options.title("Опции")
        self.win_options.resizable(False, False)
        self.win_options.geometry("600x600+800+50")

        lbl1 = tk.Label(self.win_options, width=20, height=2, bg="#cdd0d1",
                    text="Выберите опцию", font="Arial 20")
        lbl1.pack()   
        
        options = Combobox(self.win_options, values=("Доступ по возрастному рейтингу", "Статус книги",
                                                       "Узнать об издательстве", "Книги определенного жанра",
                                                       "Книги определенного автора", "Состояние читательского билета"))
        options.pack(padx=10, pady=10)
        
        btn_save2 = tk.Button(self.win_options, text='Выбрать', font="Arial 10",
                              bg='#cdd0d1')
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
