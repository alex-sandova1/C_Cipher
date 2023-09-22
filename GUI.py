import datetime
import tkinter as tk
import coder_decoder

def create_window():
    def on_click():
        current = datetime.datetime.now()
        day = current.day #stores the day
        input_ = entry.get()
        result.config(text=coder_decoder.coder(f"{input_}",day))

    #window is created
    window = tk.Tk()
    window.title('my window')
    window.geometry('200x200')

    #creates a label
    label = tk.Label(window, text ="Enter Message")
    label.pack()

    #creates the text box
    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text = "Send", command=on_click)
    button.pack()


    result = tk.Label(window, text="")
    result.pack()
    window.mainloop()

    