import tkinter as tk 
from googletrans import Translator

app = tk.Tk()
app.title("English to Japanese")
app.geometry("300x300+200+200")
app.configure(background ="light blue")


def t():
	type = entry.get()
	translator = Translator(service_urls=["translate.google.com"])
	translation = translator.translate(type,dest ="ja")
	Jap = tk.Label(app, text=f"Japanese : {translation.text}",bg="white")
	Jap.pack(pady=20)

label = tk.Label(app, text="Type in english :",font=("courier",18,"bold italic"))
label.pack(pady=20)

entry =tk.Entry(app)
entry.pack(pady=20)

button = tk.Button(app, text="Translate",font=("courier",18,"bold italic"),command=t)
button.pack(pady=20)

app.mainloop()


