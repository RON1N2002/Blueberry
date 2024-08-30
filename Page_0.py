### Page 0 => Home ###

from settings import *

def page_0(root, f_page_0):

    # big scrollabel frame
    f_welcome = ctk.CTkFrame(f_page_0, width=500, height=400)
    f_welcome.pack()

    # welcome label
    l_welcome = ctk.CTkLabel(f_welcome, text='Welcome to', font=('Arial', 30, 'bold'), text_color='grey70')
    l_header = ctk.CTkLabel(f_welcome, text='Blueberry', font=('Arial', 40, 'bold', 'underline'), text_color='grey70')
    l_welcome.pack()
    l_header.pack()

    # logo in big format
    global logo_big
    logo_big = tk.PhotoImage(file=logo_big)
    l_logo_big = tk.Label(f_page_0, image=logo_big, bg='grey17')
    l_logo_big.pack(pady=40)
