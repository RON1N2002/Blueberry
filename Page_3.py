### Page 3 => Image ###

from settings import *

def page_3(root, f_page_3):
    l_Image_header = ctk.CTkLabel(f_page_3, text='Image', font=('Arial', 25, 'bold'), text_color='grey70')
    l_Image_header.pack()

    # showing an big image
    global image
    image = tk.PhotoImage(file=image)
    l_WP = tk.Label(f_page_3, image=image, bg='grey17')
    l_WP.pack(pady=30)