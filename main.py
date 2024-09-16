# Dateien nachladen
from Page_0 import *
from Page_1 import *
from Page_2 import *
from Page_3 import *
from Page_4 import *

# Datum anzeigen
def update_date(): 
    l_date.configure(text=time.strftime('%d.%m.%Y'))
    l_date.after(10000, update_date)

# Zeit anzeigen
def update_time(): 
    l_time.configure(text=time.strftime('%H:%M:%S'))
    l_time.after(250, update_time)

# Fullscreen toggle button
def full():
    if root.overrideredirect() == True:
        root.overrideredirect(False)
        root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.update_idletasks()
    else:
        root.overrideredirect(True)
        root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.update_idletasks()

# Programm schließen
def ende():
    root.destroy()
    sys.exit()

# switch between dark/lightmode
def appearance():
    switch_value = switch_var.get()
    if switch_value == "on":
        s_change_light.configure(text='Dark')
        ctk.set_appearance_mode('dark')
    else:
        s_change_light.configure(text='Light')
        ctk.set_appearance_mode('light')

# mainwindow settings
root = ctk.CTk()
root.title('Blueberry-Software')

# screenscaling
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

scaling = (screen_width/800)

ctk.set_widget_scaling(scaling)
ctk.set_window_scaling(1)

root.geometry('{0}x{1}+0+0'.format(screen_width, screen_height))
root.overrideredirect(True)

# Topbar
f_topbar = ctk.CTkFrame(root)
f_topbar.pack()

f_topbar_oben = ctk.CTkFrame(f_topbar)
f_topbar_oben.pack()

# Logo
logo = tk.PhotoImage(file=logo)
l_logo = tk.Label(f_topbar_oben, image=logo, width=45, height=45, borderwidth=5, bg='grey20')

# Zeit und Datum
l_date = ctk.CTkLabel(f_topbar_oben, font=font, text_color='grey50')
l_time = ctk.CTkLabel(f_topbar_oben, font=font, text_color='grey50')

# Switch dark/light
switch_var = ctk.StringVar(value="on")
s_change_light = ctk.CTkSwitch(master=f_topbar_oben, 
                               text='Dark', 
                               command=appearance, 
                               font=font, 
                               variable=switch_var, 
                               onvalue="on", 
                               offvalue="off")

# Fullscreen o/off
b_full = ctk.CTkButton(f_topbar_oben,
                                 text='Full', 
                                 command=full,
                                 font=font,
                                 corner_radius=widget_corner_radius,
                                 text_color=black,
                                 )

# exit the programm
b_ende = ctk.CTkButton(f_topbar_oben, 
                                 text='Ende', 
                                 command=ende,
                                 font=font, 
                                 corner_radius=widget_corner_radius,
                                 fg_color='#5999FF',
                                 text_color=black,
                                 )

# Platzierung im Topframe
l_logo.grid(row=1, column=1, padx=30)
l_date.grid(row=1, column=2, padx=30)
l_time.grid(row=1, column=3, padx=30)
s_change_light.grid(row=1, column=4, padx=30)
b_full.grid(row=1, column=5, padx=1)  
b_ende.grid(row=1, column=6, padx=1)

# Fensterauswahl
def change(fenster):
    if fenster == 'Home':
        f_page_0.pack(pady=20)
        f_page_1.pack_forget()
        f_page_2.pack_forget()
        f_page_3.pack_forget()
        f_page_4.pack_forget()

    if fenster == 'Matrixrechner':
        f_page_0.pack_forget()
        f_page_1.pack(pady=20)
        f_page_2.pack_forget()
        f_page_3.pack_forget()
        f_page_4.pack_forget()

    if fenster == 'Bubblesort':
        f_page_0.pack_forget()
        f_page_1.pack_forget()
        f_page_2.pack(pady=20)
        f_page_3.pack_forget()
        f_page_4.pack_forget()

    if fenster == 'Image':
        f_page_0.pack_forget()
        f_page_1.pack_forget()
        f_page_2.pack_forget()
        f_page_3.pack(pady=20)
        f_page_4.pack_forget()

    if fenster == 'Notes':
        f_page_0.pack_forget()
        f_page_1.pack_forget()
        f_page_2.pack_forget()
        f_page_3.pack_forget()
        f_page_4.pack(pady=20)

sb_change = ctk.CTkSegmentedButton(f_topbar, 
                                    values=['Home','Matrixrechner', 'Bubblesort', 'Image', 'Notes'], 
                                    command=change,
                                    font=font, 
                                    corner_radius=widget_corner_radius,
                                    text_color=black,
                                 )
sb_change.set('Home')
sb_change.pack()

# Pages Frames bestimmen
f_page_0 = ctk.CTkFrame(root)
f_page_1 = ctk.CTkFrame(root)
f_page_2 = ctk.CTkFrame(root)
f_page_3 = ctk.CTkFrame(root)
f_page_4 = ctk.CTkFrame(root)

# Pages Inhalte nachladen
### Page 0 => Home ###
page_0(root, f_page_0)

### Page 1 => Matrixrechner ###
page_1(root, f_page_1)

### Page 2 => Bubblesort ###
page_2(root, f_page_2)

### Page 3 => Image ###
page_3(root, f_page_3)

### Page 4 => Notes ###
page_4(root, f_page_4)

# zuerst page_0 zeigen
f_page_0.pack(pady=20)
f_page_1.pack_forget()
f_page_2.pack_forget()
f_page_3.pack_forget()
f_page_4.pack_forget()

# Zeit und Datum im Topframe updaten
update_date()
update_time()

root.mainloop()
