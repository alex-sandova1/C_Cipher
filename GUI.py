import datetime
import tkinter as tk
import coder_decoder

def start_window():

    def code(key):


        #encodes the message amd displays in a text box under buttons
        message = entry.get()
        coded_message = coder_decoder.coder(message, key)
        label = tk.Label(window, text = coded_message)
        label.place(x=150, y=100)
    
    def decode(key):
        #decodes the message amd displays in a text box under buttons
        message = entry.get()
        decoded_message = coder_decoder.decoder(message, key)
        label = tk.Label(window, text = decoded_message)
        label.place(x=150, y=100)



    #window is created
    window = tk.Tk()
    window.title('Start window')
    window.geometry('400x200')

    #creates a label
    label = tk.Label(window, text ="encrypt or decrypt a message")
    label.place(x=200, y=10, anchor="center")

    label = tk.Label(window, text = "Enter key:")

    #creates the text box
    entry = tk.Entry(window)
    entry.place(x= 100, y=20)


    #create code button
    code_button = tk.Button(window, text = "Code", command = code)
    code_button.place(x=100, y=50)

    #create decode button
    decode_button = tk.Button(window, text = "Decode", command = decode )
    decode_button.place(x=200, y=50)

    #create close button
    close_button = tk.Button(window, text = "Close", command= window.destroy)
    close_button.place(x=150, y=160)

    window.mainloop()

