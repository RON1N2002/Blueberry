### Page 0 => Home ###

from settings import *

def page_0(root, f_page_0):

    # big scrollabel frame
    sf_welcome = ctk.CTkScrollableFrame(f_page_0, orientation='vertical', width=500, height=400)
    sf_welcome.pack()

    f_greetings = ctk.CTkFrame(sf_welcome)
    f_greetings.pack(pady=40)

    # welcome label
    l_welcome = ctk.CTkLabel(f_greetings, text='Welcome to', font=('Arial', 30, 'bold'), text_color='grey70')
    l_header = ctk.CTkLabel(f_greetings, text='Blueberry', font=('Arial', 40, 'bold', 'underline'), text_color='grey70')
    l_welcome.pack()
    l_header.pack()

    # logo in big format
    global logo_big
    logo_big = tk.PhotoImage(file=logo_big)
    l_logo_big = tk.Label(sf_welcome, image=logo_big, bg='grey20')
    l_logo_big.pack(pady=40)

    # welcome text
    l_text = ctk.CTkLabel(sf_welcome,
                          text='',
                          font=font,
                          text_color='grey70')
    l_text.pack()