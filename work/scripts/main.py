# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:44:09 2022

@author: vific
"""
import os
from windows import MainWindow
os.chdir("C:/work")

mainWindow = MainWindow(800, 800, "Библиотека", [True, True], "./images/book.ico")
mainWindow.run()
