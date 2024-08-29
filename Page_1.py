### Page 1 => Matrixrechner ###

from settings import *

# Note: Matrizen werden Spaltenwise eingelesen
def page_1(root, f_page_1):
    # Einträge der Eingabefelder M1 in Ganzzahlen umwandeln
    def get_Matrix1():
        global M1_1x1, M1_1x2, M1_1x3, M1_1x4
        global M1_2x1, M1_2x2, M1_2x3, M1_2x4
        global M1_3x1, M1_3x2, M1_3x3, M1_3x4
        global M1_4x1, M1_4x2, M1_4x3, M1_4x4

        M1_1x1 = int(e_M1_1x1.get()) if e_M1_1x1.get() else 0
        M1_1x2 = int(e_M1_1x2.get()) if e_M1_1x2.get() else 0
        M1_1x3 = int(e_M1_1x3.get()) if e_M1_1x3.get() else 0
        M1_1x4 = int(e_M1_1x4.get()) if e_M1_1x4.get() else 0
        M1_2x1 = int(e_M1_2x1.get()) if e_M1_2x1.get() else 0
        M1_2x2 = int(e_M1_2x2.get()) if e_M1_2x2.get() else 0
        M1_2x3 = int(e_M1_2x3.get()) if e_M1_2x3.get() else 0
        M1_2x4 = int(e_M1_2x4.get()) if e_M1_2x4.get() else 0
        M1_3x1 = int(e_M1_3x1.get()) if e_M1_3x1.get() else 0
        M1_3x2 = int(e_M1_3x2.get()) if e_M1_3x2.get() else 0
        M1_3x3 = int(e_M1_3x3.get()) if e_M1_3x3.get() else 0
        M1_3x4 = int(e_M1_3x4.get()) if e_M1_3x4.get() else 0
        M1_4x1 = int(e_M1_4x1.get()) if e_M1_4x1.get() else 0
        M1_4x2 = int(e_M1_4x2.get()) if e_M1_4x2.get() else 0
        M1_4x3 = int(e_M1_4x3.get()) if e_M1_4x3.get() else 0
        M1_4x4 = int(e_M1_4x4.get()) if e_M1_4x4.get() else 0

    # Einträge der Eingabefelder M2 in Ganzzahlen umwandeln
    def get_Matrix2():
        global M2_1x1, M2_1x2, M2_1x3, M2_1x4
        global M2_2x1, M2_2x2, M2_2x3, M2_2x4
        global M2_3x1, M2_3x2, M2_3x3, M2_3x4
        global M2_4x1, M2_4x2, M2_4x3, M2_4x4

        M2_1x1 = int(e_M2_1x1.get()) if e_M2_1x1.get() else 0
        M2_1x2 = int(e_M2_1x2.get()) if e_M2_1x2.get() else 0
        M2_1x3 = int(e_M2_1x3.get()) if e_M2_1x3.get() else 0
        M2_1x4 = int(e_M2_1x4.get()) if e_M2_1x4.get() else 0
        M2_2x1 = int(e_M2_2x1.get()) if e_M2_2x1.get() else 0
        M2_2x2 = int(e_M2_2x2.get()) if e_M2_2x2.get() else 0
        M2_2x3 = int(e_M2_2x3.get()) if e_M2_2x3.get() else 0
        M2_2x4 = int(e_M2_2x4.get()) if e_M2_2x4.get() else 0
        M2_3x1 = int(e_M2_3x1.get()) if e_M2_3x1.get() else 0
        M2_3x2 = int(e_M2_3x2.get()) if e_M2_3x2.get() else 0
        M2_3x3 = int(e_M2_3x3.get()) if e_M2_3x3.get() else 0
        M2_3x4 = int(e_M2_3x4.get()) if e_M2_3x4.get() else 0
        M2_4x1 = int(e_M2_4x1.get()) if e_M2_4x1.get() else 0
        M2_4x2 = int(e_M2_4x2.get()) if e_M2_4x2.get() else 0
        M2_4x3 = int(e_M2_4x3.get()) if e_M2_4x3.get() else 0
        M2_4x4 = int(e_M2_4x4.get()) if e_M2_4x4.get() else 0

    # Einträge des Vektors M2 in globale Ganzzahlen umwandeln
    def get_Vekor():
        global V1, V2, V3, V4

        V1 = int(e_V1.get()) if e_V1.get() else 0
        V2 = int(e_V2.get()) if e_V2.get() else 0
        V3 = int(e_V3.get()) if e_V3.get() else 0
        V4 = int(e_V4.get()) if e_V4.get() else 0

    # long Button
    def rechnungen(value):
    # Determinantenberechnung M1
        if value == 'Determinante Matrix-1':
            clear_MatrixX()

            # VersuchenZahlen aus M1 zu holen
            try:
                get_Matrix1()
            except:
                l_Ausgabe_Zahl.configure(text='Fehler')

            # Determinante verbleibender 3x3 Matrix (=> ohne 1. Zeile und 1. Spalte) * M1_1x1
            Md_1x1 = M1_1x1*(M1_2x2*M1_3x3*M1_4x4 + M1_3x2*M1_4x3*M1_2x4 + M1_4x2*M1_2x3*M1_3x4
                            - M1_2x4*M1_3x3*M1_4x2 - M1_3x4*M1_4x3*M1_2x2 - M1_4x4*M1_2x3*M1_3x2)
            # Determinante verbleibender 3x3 Matrix (=> ohne 1. Zeile und 2. Spalte) * M1_2x1
            Md_2x1 = M1_2x1*(M1_1x2*M1_3x3*M1_4x4 + M1_3x2*M1_4x3*M1_1x4 + M1_4x2*M1_1x3*M1_3x4
                            - M1_1x4*M1_3x3*M1_4x2 - M1_3x4*M1_4x3*M1_1x2 - M1_4x4*M1_1x3*M1_3x2)
            # Determinante verbleibender 3x3 Matrix (=> ohne 1. Zeile und 3. Spalte) * M1_#3x1
            Md_3x1 = M1_3x1*(M1_1x2*M1_2x3*M1_4x4 + M1_2x2*M1_4x3*M1_1x4 + M1_4x2*M1_1x3*M1_2x4
                            - M1_1x4*M1_2x3*M1_4x2 - M1_2x4*M1_4x3*M1_1x2 - M1_4x4*M1_1x3*M1_2x2)
            # Determinante verbleibender 3x3 Matrix (=> ohne 1. Zeile und 4. Spalte) * M1_4x1
            Md_4x1 = M1_4x1*(M1_1x2*M1_2x3*M1_3x4 + M1_2x2*M1_3x3*M1_1x4 + M1_3x2*M1_1x3*M1_2x4
                            - M1_1x4*M1_2x3*M1_3x2 - M1_2x4*M1_3x3*M1_1x2 - M1_3x4*M1_1x3*M1_2x2)
            
            # Einzelne Determinanten zusammenrechnen (+/- Netz beachten)
            global Ergbnis_Determinate
            Ergbnis_Determinate = Md_1x1 - Md_2x1 + Md_3x1 - Md_4x1

            # Ausgabe
            l_Ausgabe_Zahl.configure(text=Ergbnis_Determinate)

    # Matrizenmultiplikation M1 und M2
        if value == 'Matrix-1 x Matrix-2':
            clear_MatrixX()

            # VersuchenZahlen aus M1 und M2 holen
            try:
                get_Matrix1()
                get_Matrix2()
            except:
                l_Ausgabe_Zahl.configure(text='Fehler')

            # Mx_Spalte1 = Alle Reihen_M1 * Spalte1_M2
            Mx_1x1 = M1_1x1 * M2_1x1 + M1_2x1 * M2_1x2 + M1_3x1 * M2_1x3 + M1_4x1 * M2_1x4
            Mx_1x2 = M1_1x2 * M2_1x1 + M1_2x2 * M2_1x2 + M1_3x2 * M2_1x3 + M1_4x2 * M2_1x4
            Mx_1x3 = M1_1x3 * M2_1x1 + M1_2x3 * M2_1x2 + M1_3x3 * M2_1x3 + M1_4x3 * M2_1x4
            Mx_1x4 = M1_1x4 * M2_1x1 + M1_2x4 * M2_1x2 + M1_3x4 * M2_1x3 + M1_4x4 * M2_1x4

            #Mx_Spalte2 = Alle Reihen_M1 * Spalte2_M2
            Mx_2x1 = M1_1x1 * M2_2x1 + M1_2x1 * M2_2x2 + M1_3x1 * M2_2x3 + M1_4x1 * M2_2x4
            Mx_2x2 = M1_1x2 * M2_2x1 + M1_2x2 * M2_2x2 + M1_3x2 * M2_2x3 + M1_4x2 * M2_2x4
            Mx_2x3 = M1_1x3 * M2_2x1 + M1_2x3 * M2_2x2 + M1_3x3 * M2_2x3 + M1_4x3 * M2_2x4
            Mx_2x4 = M1_1x4 * M2_2x1 + M1_2x4 * M2_2x2 + M1_3x4 * M2_2x3 + M1_4x4 * M2_2x4

            # Mx_Spalte3 = Alle Reihen_M1 * Spalte3_M2
            Mx_3x1 = M1_1x1 * M2_3x1 + M1_2x1 * M2_3x2 + M1_3x1 * M2_3x3 + M1_4x1 * M2_3x4
            Mx_3x2 = M1_1x2 * M2_3x1 + M1_2x2 * M2_3x2 + M1_3x2 * M2_3x3 + M1_4x2 * M2_3x4
            Mx_3x3 = M1_1x3 * M2_3x1 + M1_2x3 * M2_3x2 + M1_3x3 * M2_3x3 + M1_4x3 * M2_3x4
            Mx_3x4 = M1_1x4 * M2_3x1 + M1_2x4 * M2_3x2 + M1_3x4 * M2_3x3 + M1_4x4 * M2_3x4

            # Mx_Spalte4 = Alle Reihen_M1 * Spalte4_M2
            Mx_4x1 = M1_1x1 * M2_4x1 + M1_2x1 * M2_4x2 + M1_3x1 * M2_4x3 + M1_4x1 * M2_4x4
            Mx_4x2 = M1_1x2 * M2_4x1 + M1_2x2 * M2_4x2 + M1_3x2 * M2_4x3 + M1_4x2 * M2_4x4
            Mx_4x3 = M1_1x3 * M2_4x1 + M1_2x3 * M2_4x2 + M1_3x3 * M2_4x3 + M1_4x3 * M2_4x4
            Mx_4x4 = M1_1x4 * M2_4x1 + M1_2x4 * M2_4x2 + M1_3x4 * M2_4x3 + M1_4x4 * M2_4x4

            # Ausgabe
            l_Mx_1x1.configure(text=Mx_1x1)
            l_Mx_1x2.configure(text=Mx_1x2)
            l_Mx_1x3.configure(text=Mx_1x3)
            l_Mx_1x4.configure(text=Mx_1x4)

            l_Mx_2x1.configure(text=Mx_2x1)
            l_Mx_2x2.configure(text=Mx_2x2)
            l_Mx_2x3.configure(text=Mx_2x3)
            l_Mx_2x4.configure(text=Mx_2x4)

            l_Mx_3x1.configure(text=Mx_3x1)
            l_Mx_3x2.configure(text=Mx_3x2)
            l_Mx_3x3.configure(text=Mx_3x3)
            l_Mx_3x4.configure(text=Mx_3x4)

            l_Mx_4x1.configure(text=Mx_4x1)
            l_Mx_4x2.configure(text=Mx_4x2)
            l_Mx_4x3.configure(text=Mx_4x3)
            l_Mx_4x4.configure(text=Mx_4x4)

    # M1 mit Vektor multiplizieren
        if value == 'Matrix-1 x Vektor':
            clear_MatrixX()

            # VersuchenZahlen aus M1 und V holen
            try:
                get_Matrix1()
                get_Vekor()
            except:
                l_Ausgabe_Zahl.configure(text='Fehler')

            # Spaltenweise Matrix-1 * Vektor
            Vx1 = M1_1x1 * V1 + M1_2x1 * V2 + M1_3x1 * V3 + M1_4x1 * V4
            Vx2 = M1_1x2 * V1 + M1_2x2 * V2 + M1_3x2 * V3 + M1_4x2 * V4
            Vx3 = M1_1x3 * V1 + M1_2x3 * V2 + M1_3x3 * V3 + M1_4x3 * V4
            Vx4 = M1_1x4 * V1 + M1_2x4 * V2 + M1_3x4 * V3 + M1_4x4 * V4

            # Ausgabe
            l_Mx_2x1.configure(text=Vx1)
            l_Mx_2x2.configure(text=Vx2)
            l_Mx_2x3.configure(text=Vx3)
            l_Mx_2x4.configure(text=Vx4)

    # Eingabefelder aus M1 leeren
    def clear_Matrix1():
        e_M1_1x1.delete(0,99)
        e_M1_1x2.delete(0,99)
        e_M1_1x3.delete(0,99)
        e_M1_1x4.delete(0,99)

        e_M1_2x1.delete(0,99)
        e_M1_2x2.delete(0,99)
        e_M1_2x3.delete(0,99)
        e_M1_2x4.delete(0,99)

        e_M1_3x1.delete(0,99)
        e_M1_3x2.delete(0,99)
        e_M1_3x3.delete(0,99)
        e_M1_3x4.delete(0,99)

        e_M1_4x1.delete(0,99)
        e_M1_4x2.delete(0,99)
        e_M1_4x3.delete(0,99)
        e_M1_4x4.delete(0,99)

        e_M1_1x1.configure(placeholder_text=0)
        e_M1_1x2.configure(placeholder_text=0)
        e_M1_1x3.configure(placeholder_text=0)
        e_M1_1x4.configure(placeholder_text=0)

        e_M1_2x1.configure(placeholder_text=0)
        e_M1_2x2.configure(placeholder_text=0)
        e_M1_2x3.configure(placeholder_text=0)
        e_M1_2x4.configure(placeholder_text=0)

        e_M1_3x1.configure(placeholder_text=0)
        e_M1_3x2.configure(placeholder_text=0)
        e_M1_3x3.configure(placeholder_text=0)
        e_M1_3x4.configure(placeholder_text=0)

        e_M1_4x1.configure(placeholder_text=0)
        e_M1_4x2.configure(placeholder_text=0)
        e_M1_4x3.configure(placeholder_text=0)
        e_M1_4x4.configure(placeholder_text=0)

    # Eingabefelder aus M2 leeren    
    def clear_Matrix2():
        e_M2_1x1.delete(0,99)
        e_M2_1x2.delete(0,99)
        e_M2_1x3.delete(0,99)
        e_M2_1x4.delete(0,99)

        e_M2_2x1.delete(0,99)
        e_M2_2x2.delete(0,99)
        e_M2_2x3.delete(0,99)
        e_M2_2x4.delete(0,99)

        e_M2_3x1.delete(0,99)
        e_M2_3x2.delete(0,99)
        e_M2_3x3.delete(0,99)
        e_M2_3x4.delete(0,99)

        e_M2_4x1.delete(0,99)
        e_M2_4x2.delete(0,99)
        e_M2_4x3.delete(0,99)
        e_M2_4x4.delete(0,99)

        e_M2_1x1.configure(placeholder_text=0)
        e_M2_1x2.configure(placeholder_text=0)
        e_M2_1x3.configure(placeholder_text=0)
        e_M2_1x4.configure(placeholder_text=0)

        e_M2_2x1.configure(placeholder_text=0)
        e_M2_2x2.configure(placeholder_text=0)
        e_M2_2x3.configure(placeholder_text=0)
        e_M2_2x4.configure(placeholder_text=0)

        e_M2_3x1.configure(placeholder_text=0)
        e_M2_3x2.configure(placeholder_text=0)
        e_M2_3x3.configure(placeholder_text=0)
        e_M2_3x4.configure(placeholder_text=0)

        e_M2_4x1.configure(placeholder_text=0)
        e_M2_4x2.configure(placeholder_text=0)
        e_M2_4x3.configure(placeholder_text=0)
        e_M2_4x4.configure(placeholder_text=0)

    # Eingabefelder aus Vektor leeren
    def clear_Vektor():
        e_V1.delete(0,99)
        e_V2.delete(0,99)
        e_V3.delete(0,99)
        e_V4.delete(0,99)

        e_V1.configure(placeholder_text=0)
        e_V2.configure(placeholder_text=0)
        e_V3.configure(placeholder_text=0)
        e_V4.configure(placeholder_text=0)

    # Ausgabe aus Mx leeren
    def clear_MatrixX():
        l_Mx_1x1.configure(text='')
        l_Mx_1x2.configure(text='')
        l_Mx_1x3.configure(text='')
        l_Mx_1x4.configure(text='')

        l_Mx_2x1.configure(text='')
        l_Mx_2x2.configure(text='')
        l_Mx_2x3.configure(text='')
        l_Mx_2x4.configure(text='')

        l_Mx_3x1.configure(text='')
        l_Mx_3x2.configure(text='')
        l_Mx_3x3.configure(text='')
        l_Mx_3x4.configure(text='')

        l_Mx_4x1.configure(text='') 
        l_Mx_4x2.configure(text='')
        l_Mx_4x3.configure(text='')
        l_Mx_4x4.configure(text='')
        
        l_Ausgabe_Zahl.configure(text=' ')

    # Determinantenergebnins in die Zwischenablage kopieren
    def kopieren():
        root.clipboard_clear()
        try:
            root.clipboard_append(Ergbnis_Determinate)
        except:
            pass

    # Hauptüberschrift
    l_Titel = ctk.CTkLabel(f_page_1, text='Matrixrechner', font=('Arial', 25, 'bold'), text_color='grey70')
    l_Titel.pack()
    

    f_Eingaben = ctk.CTkScrollableFrame(f_page_1, width=600, orientation='horizontal')
    f_Eingaben.pack()

    # Überschriften
    l_Matrix1 = ctk.CTkLabel(f_Eingaben,
                            text='Matrix-1',
                            font=('Arial', 20, 'bold','underline'),
                            text_color='grey60',
                            corner_radius=widget_corner_radius
                            )

    l_Matrix2 = ctk.CTkLabel(f_Eingaben,
                            text='Matrix-2',
                            font=('Arial', 20, 'bold','underline'),
                            text_color='grey60',
                            corner_radius=widget_corner_radius
                            )

    l_Ausgabe = ctk.CTkLabel(f_Eingaben,
                            text='Ausgabe',
                            font=('Arial', 20, 'bold','underline'),
                            text_color='grey60',
                            corner_radius=widget_corner_radius
                            )

    l_Vektor = ctk.CTkLabel(f_Eingaben,
                            text='Vektor',
                            font=('Arial', 20, 'bold','underline'),
                            text_color='grey60',
                            corner_radius=widget_corner_radius
                            )

    l_Matrix1.grid(row=0, column=1, pady=5)
    l_Matrix2.grid(row=0, column=3, pady=5)
    l_Ausgabe.grid(row=0, column=2, pady=5)
    l_Vektor.grid(row=0, column=4, pady=5)

    # Matrix1
    f_Matrix1 = ctk.CTkFrame(f_Eingaben)
    f_Matrix1.grid(row=1, column=1)

    e_M1_1x1 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_1x2 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_1x3 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_1x4 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M1_2x1 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_2x2 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_2x3 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_2x4 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M1_3x1 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_3x2 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_3x3 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_3x4 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M1_4x1 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_4x2 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_4x3 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M1_4x4 = ctk.CTkEntry(f_Matrix1, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M1_1x1.grid(row=1, column=1, padx=padx, pady=pady)
    e_M1_1x2.grid(row=2, column=1, padx=padx, pady=pady)
    e_M1_1x3.grid(row=3, column=1, padx=padx, pady=pady)
    e_M1_1x4.grid(row=4, column=1, padx=padx, pady=pady)

    e_M1_2x1.grid(row=1, column=2, padx=padx, pady=pady)
    e_M1_2x2.grid(row=2, column=2, padx=padx, pady=pady)
    e_M1_2x3.grid(row=3, column=2, padx=padx, pady=pady)
    e_M1_2x4.grid(row=4, column=2, padx=padx, pady=pady)

    e_M1_3x1.grid(row=1, column=3, padx=padx, pady=pady)
    e_M1_3x2.grid(row=2, column=3, padx=padx, pady=pady)
    e_M1_3x3.grid(row=3, column=3, padx=padx, pady=pady)
    e_M1_3x4.grid(row=4, column=3, padx=padx, pady=pady)

    e_M1_4x1.grid(row=1, column=4, padx=padx, pady=pady)
    e_M1_4x2.grid(row=2, column=4, padx=padx, pady=pady)
    e_M1_4x3.grid(row=3, column=4, padx=padx, pady=pady)
    e_M1_4x4.grid(row=4, column=4, padx=padx, pady=pady)

    # Matrix2
    f_Matrix2 = ctk.CTkFrame(f_Eingaben)
    f_Matrix2.grid(row=1, column=3)

    e_M2_1x1 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_1x2 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_1x3 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_1x4 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M2_2x1 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_2x2 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_2x3 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_2x4 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M2_3x1 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_3x2 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_3x3 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_3x4 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M2_4x1 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_4x2 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_4x3 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_M2_4x4 = ctk.CTkEntry(f_Matrix2, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_M2_1x1.grid(row=1, column=1, padx=padx, pady=pady)
    e_M2_1x2.grid(row=2, column=1, padx=padx, pady=pady)
    e_M2_1x3.grid(row=3, column=1, padx=padx, pady=pady)
    e_M2_1x4.grid(row=4, column=1, padx=padx, pady=pady)

    e_M2_2x1.grid(row=1, column=2, padx=padx, pady=pady)
    e_M2_2x2.grid(row=2, column=2, padx=padx, pady=pady)
    e_M2_2x3.grid(row=3, column=2, padx=padx, pady=pady)
    e_M2_2x4.grid(row=4, column=2, padx=padx, pady=pady)

    e_M2_3x1.grid(row=1, column=3, padx=padx, pady=pady)
    e_M2_3x2.grid(row=2, column=3, padx=padx, pady=pady)
    e_M2_3x3.grid(row=3, column=3, padx=padx, pady=pady)
    e_M2_3x4.grid(row=4, column=3, padx=padx, pady=pady)

    e_M2_4x1.grid(row=1, column=4, padx=padx, pady=pady)
    e_M2_4x2.grid(row=2, column=4, padx=padx, pady=pady)
    e_M2_4x3.grid(row=3, column=4, padx=padx, pady=pady)
    e_M2_4x4.grid(row=4, column=4, padx=padx, pady=pady)

    # Ausgabematrix
    f_MatrixX = ctk.CTkFrame(f_Eingaben, fg_color='grey10')
    f_MatrixX.grid(row=1, column=2, padx=padx)

    l_Mx_1x1 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_1x2 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_1x3 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_1x4 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)

    l_Mx_2x1 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_2x2 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_2x3 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_2x4 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)

    l_Mx_3x1 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_3x2 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_3x3 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_3x4 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)

    l_Mx_4x1 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_4x2 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_4x3 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)
    l_Mx_4x4 = ctk.CTkLabel(f_MatrixX, text='', font=font, corner_radius=widget_corner_radius, text_color=lightgrey)

    l_Mx_1x1.grid(row=1, column=1, padx=padx, pady=padx)
    l_Mx_1x2.grid(row=2, column=1, padx=padx, pady=padx)
    l_Mx_1x3.grid(row=3, column=1, padx=padx, pady=padx)
    l_Mx_1x4.grid(row=4, column=1, padx=padx, pady=padx)

    l_Mx_2x1.grid(row=1, column=2, padx=padx, pady=padx)
    l_Mx_2x2.grid(row=2, column=2, padx=padx, pady=padx)
    l_Mx_2x3.grid(row=3, column=2, padx=padx, pady=padx)
    l_Mx_2x4.grid(row=4, column=2, padx=padx, pady=padx)

    l_Mx_3x1.grid(row=1, column=3, padx=padx, pady=padx)
    l_Mx_3x2.grid(row=2, column=3, padx=padx, pady=padx)
    l_Mx_3x3.grid(row=3, column=3, padx=padx, pady=padx)
    l_Mx_3x4.grid(row=4, column=3, padx=padx, pady=padx)

    l_Mx_4x1.grid(row=1, column=4, padx=padx, pady=padx)
    l_Mx_4x2.grid(row=2, column=4, padx=padx, pady=padx)
    l_Mx_4x3.grid(row=3, column=4, padx=padx, pady=padx)
    l_Mx_4x4.grid(row=4, column=4, padx=padx, pady=padx)

    # Ausgabe Zahl
    l_Ausgabe_Zahl = ctk.CTkLabel(f_Eingaben, text='', fg_color='grey10', font=font, text_color=lightgrey)
    l_Ausgabe_Zahl.grid(row=1, column=2, padx=padx)

    # Vektor
    f_Vektor = ctk.CTkFrame(f_Eingaben)
    f_Vektor.grid(row=1, column=4)
    e_V1 = ctk.CTkEntry(f_Vektor, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_V2 = ctk.CTkEntry(f_Vektor, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_V3 = ctk.CTkEntry(f_Vektor, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)
    e_V4 = ctk.CTkEntry(f_Vektor, width=entry_widht, font=font, corner_radius=widget_corner_radius, border_width=entry_border_width, placeholder_text=0)

    e_V1.grid(row=1, column=1, padx=padx, pady=padx)
    e_V2.grid(row=2, column=1, padx=padx, pady=padx)
    e_V3.grid(row=3, column=1, padx=padx, pady=padx)
    e_V4.grid(row=4, column=1, padx=padx, pady=padx)

    # Clearbuttons
    b_clear_M1 = ctk.CTkButton(f_Eingaben, text='clear', command=clear_Matrix1, font=font, fg_color='grey50', text_color='black', height=8, width=14)
    b_clear_M1.grid(row=5, column=1, pady=5)

    b_clear_M2 = ctk.CTkButton(f_Eingaben, text='clear', command=clear_Matrix2, font=font, fg_color='grey50', text_color='black', height=8, width=14)
    b_clear_M2.grid(row=5, column=3, pady=5)

    b_clear_Mx = ctk.CTkButton(f_Eingaben, text='clear', command=clear_MatrixX, font=font, fg_color='grey50', text_color='black', height=8, width=14)
    b_clear_Mx.grid(row=5, column=2, pady=5)

    b_clear_V = ctk.CTkButton(f_Eingaben, text='clear', command=clear_MatrixX, font=font, fg_color='grey50', text_color='black', height=8, width=14)
    b_clear_V.grid(row=5, column=4, pady=5)

    # Buttons
    f_Buttons = ctk.CTkFrame(f_page_1)
    f_Buttons.pack()

    sb_rechnungen = ctk.CTkSegmentedButton(f_Buttons, 
                                            values=['Determinante Matrix-1', 'Matrix-1 x Matrix-2', 'Matrix-1 x Vektor'], 
                                            command=rechnungen,
                                            font=font, 
                                            corner_radius=widget_corner_radius,
                                            text_color=black,
                                    )

    b_kopieren = ctk.CTkButton(f_Buttons, 
                                    text='Determinante kopieren', 
                                    command=kopieren,
                                    font=font, 
                                    corner_radius=widget_corner_radius,
                                    text_color=black,
                                    )

    sb_rechnungen.grid(row=1, column=1, padx=padx, pady=pady)
    b_kopieren.grid(row=2, column=1, padx=padx, pady=pady)

    clear_MatrixX()