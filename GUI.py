import tkinter as tk

def on_click():
    input_ = entry.get()
    result.config(text=f"message: {input_}")

#window is created
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#creates a label
label = tk.Label(window, text ="hello world")
label.pack()

#creates the text box
entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text = "Send", command=on_click)
button.pack()


result = tk.Label(window, text="")
result.pack()

window.mainloop()