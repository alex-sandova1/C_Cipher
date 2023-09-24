import datetime
import tkinter as tk
import coder_decoder

def start_window():

    def code():
        current = datetime.datetime.now()
        day = current.day #stores the day
        input_ = entry.get()
        result.config(text=coder_decoder.coder(f"{input_}",day))

    def decode():
        current = datetime.datetime.now()
        day = current.day #stores the day
        input_ = entry.get()
        result.config(text=coder_decoder.decoder(f"{input_}",day))


    #window is created
    window = tk.Tk()
    window.title('Start window')
    window.geometry('400x200')

    #creates a label
    label = tk.Label(window, text ="Make a choice")
    label.place(x=200, y=10, anchor="center")

    #creates the text box
    entry = tk.Entry(window)
    entry.place(x= 100, y=20)


    #create code button
    code_button = tk.Button(window, text = "Code", command = code)
    code_button.place(x=100, y=50)

    result = tk.Label(window, text="")
    result.place(x=175, y=80)

    #create decode button
    decode_button = tk.Button(window, text = "Decode", command = decode)
    decode_button.place(x=200, y=50)

    result = tk.Label(window, text="")
    result.place(x=175, y=80)
    

    #create close button
    close_button = tk.Button(window, text = "Close", command= window.destroy)
    close_button.place(x=150, y=160)

    window.mainloop()

