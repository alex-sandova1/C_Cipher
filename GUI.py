import datetime
import tkinter as tk
import coder_decoder

def coder_window():
    def on_click():
        current = datetime.datetime.now()
        day = current.day #stores the day
        input_ = entry.get()
        result.config(text=coder_decoder.coder(f"{input_}",day))

    #window is created
    window = tk.Tk()
    window.title('coder')
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

def decoder_window():



    def on_click():
        current = datetime.datetime.now()
        day = current.day #stores the day
        input_ = entry.get()
        result.config(text=coder_decoder.decoder(f"{input_}",day))

    #window is created
    window = tk.Tk()
    window.title('decoder')
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

def start_window():

    #window is created
    window = tk.Tk()
    window.title('Start window')
    window.geometry('500x300')

    #create code button
    code_button = tk.Button(window, text = "Code", command=coder_window)
    code_button.pack()

    #create decode button
    decode_button = tk.Button(window, text = "Decode", command=decoder_window)
    decode_button.pack()

    window.mainloop()

