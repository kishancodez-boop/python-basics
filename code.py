import tkinter as tk

window = tk.Tk()
search = tk.Tk()
window.title("My App")
search.title("My App")

label = tk.Label(window, text="Hello, Kushal!")
label.pack()

button = tk.Button(window, text="ENTER")
button = tk.Button(search, text="please seacrh")
button.pack()

window.mainloop()
search.mainloop()

