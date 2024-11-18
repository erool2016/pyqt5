
import tkinter as tk



def show():
    #
    pass

def window():
    # window = tk.Tk()
    # window.geometry('500x300')
    haending = tk.Label(text='склад ',
                        font=100,
                        foreground='green',
                        background='yellow',
                        height=2
                        )
    haending.pack(pady=(10, 0))
    enrty = tk.Entry(width=50)
    enrty.pack(pady=(15, 0))

    button = tk.Button(window, text='Показать    все   ячейки', font=10, command=show)
    button.pack(pady=(15, 0))

    window.mainloop()






# haending = tk.Label(text='склад ',
#                     font=100,
#                     foreground='green',
#                     background='yellow',
#                     height=2
#                     )
# haending.pack(pady=(10,0))
# enrty = tk.Entry(width=50)
# enrty.pack(pady=(15,0))
#
# button = tk.Button(window,text='Показать    все   ячейки',font=10,command=show)
# button.pack(pady=(15,0))
#
#
# window.mainloop()