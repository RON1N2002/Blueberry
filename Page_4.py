### Page 4 => Notes ###

from settings import *

def page_4(root, f_page_4):
    def speichern():
        # Notizen in entspechender .txt speichern
        text = t_textbox.get('0.0', 'end')

        file = open(notes, "a")
        file.write(time.strftime('%d.%m.%Y'))
        file.write(' | ')
        file.write(time.strftime('%H:%M'))
        file.write('\n')
        file.write(text)
        file.write('\n')
        file.close()

        # Speicherinformation
        l_confirm.configure(text='Gespeichert')
        l_confirm.update_idletasks()
        time.sleep(1.0)
        l_confirm.configure(text='')

    l_header = ctk.CTkLabel(f_page_4, text='Notes', font=('Arial', 25, 'bold'), text_color='grey70')

    t_textbox = ctk.CTkTextbox(f_page_4, activate_scrollbars=True, font=('Arial', 16, 'bold'), width=600, height=250)

    l_confirm = ctk.CTkLabel(f_page_4, text='', font=('Arial', 10, 'bold'), text_color='grey70')

    b_save = ctk.CTkButton(f_page_4, text='Speichern', command=speichern, font=font, text_color='black')

    l_header.pack()
    t_textbox.pack()
    l_confirm.pack()
    b_save.pack()