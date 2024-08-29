# imports
import customtkinter as ctk # type: ignore
import tkinter as tk
import time
import sys
import random
import os

# Settings
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
ctk.set_widget_scaling(1.6) #choose '2.0' for 1920x1080
ctk.set_window_scaling(1)

# custom settings
font = ('Arial', 18, 'bold')
black = ('#000000')
lightgrey = 'grey90'
entry_widht = 50
widget_corner_radius = 5 
entry_border_width = 2
gap_x = 2
gap_y = 3
pady = 2
padx = 2

# files
filepath = os.path.dirname(os.path.abspath(__file__))

logo = filepath + '/Images/logo.png' #48px
logo_big = filepath + '/Images/logo_big.png' #128px
image = filepath + '/Images/image.png'

notes = filepath + '/Blueberry_Notizen.txt'