### Page 2 => Bubblesort ###

from settings import *

def page_2(root, f_page_2):
    # Sortierschleife
    def sortieren():
        # Tickspeed (dient nur zur Anschauung)
        ti = c_Tickspeed.get()

        if ti == 'Schnell':
            tickspeed = 0.0
        if ti == 'Normal':
            tickspeed = 0.2
        if ti == 'Langsam':
            tickspeed = 1.5

        # Liste welche sortiert werden soll
        eingabe = []

        li = c_Listenlänge.get()

        if li == 'Listenlänge 5':
            for i in range(5):
                eingabe.append(random.randint(0,99))
        if li == 'Listenlänge 10':
            for i in range(10):
                eingabe.append(random.randint(0,99))
        if li == 'Listenlänge 20':
            for i in range(20):
                eingabe.append(random.randint(0,99))

        # Liste wie sie aussehen soll, wenn sie sortiert ist
        sortiert = sorted(eingabe)

        # Länge der Liste feststellen
        listenlänge = int(len(eingabe))
        listenlänge_b = listenlänge

        # Pointer auf ersten beiden Listenelemente zuweisen
        pointer_1 = 0
        pointer_2 = 1

        l_Ausgabe2.configure(text=f'unsortierte Liste:\n{eingabe}')
        f_page_2.update()

        # Zähler für Durchläufe der Liste (dient nur zur Anschauung)
        zähler = 0

        # Sortierschleife
        while True:
            liste = eingabe

            time.sleep(tickspeed)

            # prüfen ob Liste sortiert ist
            if liste == sortiert:
                break

            # Durchlaufzähler
            zähler = zähler+1

            # Elemente aus den Pointern auslesen
            elemtent_1 = liste[pointer_1]
            elemtent_2 = liste[pointer_2]

            # Elemente tauschen falls Element in Pointer 1 größer als Element in Pointer 2
            if elemtent_1 > elemtent_2:
                liste[pointer_1] = elemtent_2
                liste[pointer_2] = elemtent_1
                l_Ausgabe.configure(text=f'{zähler}. Vergleich | {pointer_1+1}. Element und {pointer_2+1}. Element werden verglichen:\nElemente [{elemtent_1}] und [{elemtent_2}] tauschen:\n{liste}')
                f_page_2.update()

            # Elemente nicht tauschen falls Element in Pointer 1 kleiner oder gleich als Element in Pointer 2
            else:
                l_Ausgabe.configure(text=f'{zähler}. Vergleich | {pointer_1+1}. Element und {pointer_2+1}. Element werden verglichen:\nElemente [{elemtent_1}] und [{elemtent_2}] nicht tauschen:\n{liste}')
                f_page_2.update()

            # Pointer hochzählen
            pointer_1 = pointer_1+1
            pointer_2 = pointer_2+1

            # Bei erreichen des Listenendes -> Pointer wieder auf ersten beide Listenelemente setzen
            if pointer_2 == listenlänge:
                # kürzen der Länge der Elemente welche verglichen werden müssen
                listenlänge = listenlänge-1
                time.sleep(tickspeed)
                # Ausgabe, das ein neuer Listendurchlauf gestartet wird
                l_Ausgabe.configure(text=f'\nNeuer Listendurchlauf\n{liste}')
                f_page_2.update()
                # Pointer wieder auf ersten beide Elemete setzen
                pointer_1 = 0
                pointer_2 = 1

            time.sleep(tickspeed)
        
        l_Ausgabe.configure(text=f'sortierte Liste:\n{liste}\nVergleiche: {zähler} | Listenlänge: {listenlänge_b}')

    # Widgets
    l_Überschrift = ctk.CTkLabel(f_page_2, text='Bubblesort', font=('Arial', 25, 'bold'), text_color='grey70')

    l_Ausgabe = ctk.CTkLabel(f_page_2, text='', font=font, corner_radius=45)

    l_Ausgabe2 = ctk.CTkLabel(f_page_2, text='', font=font, corner_radius=45)

    f_Auswahl = ctk.CTkFrame(f_page_2)

    b_Sortieren = ctk.CTkButton(f_Auswahl, text='Sortieren', command=sortieren, font=font, text_color='black')

    c_Listenlänge = ctk.CTkComboBox(f_Auswahl, values=('Listenlänge 5', 'Listenlänge 10', 'Listenlänge 20'))
    c_Listenlänge.set(value='Listenlänge 10')

    c_Tickspeed = ctk.CTkComboBox(f_Auswahl, values=('Schnell', 'Normal', 'Langsam'))
    c_Tickspeed.set(value='Normal')

    l_Überschrift.pack(pady=pady)
    l_Ausgabe2.pack()
    l_Ausgabe.pack(pady=pady)

    f_Auswahl.pack(side='bottom', pady=20)
    c_Listenlänge.grid(row=1, column=1)
    c_Tickspeed.grid(row=2, column=1)
    b_Sortieren.grid(row=3, column=1)