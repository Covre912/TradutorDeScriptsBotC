from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
import os
import tradutor

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def findFile(*args):
	filename = filedialog.askopenfilename()
	cenario_ingles.set(filename)

def tradutorBotC(*args):
	f = open(resource_path("ptbr/all.json"), encoding="utf-8")
	todos = tradutor.getTodos(f)
	try:
		filename = cenario_ingles.get()
		arquivo = open(filename, encoding="utf-8")
		cenario = tradutor.montaJson(arquivo, todos)
		if type(cenario) != type("String"):
			raise cenario
		cenario_traduzido.set("Script Traduzido com Sucesso")
		filenamePortugues = filedialog.asksaveasfilename(defaultextension=".json", initialfile=filename[filename.rindex('/')+1:])
		f = open(filenamePortugues, "w", encoding="utf-8")
		f.write(cenario)
		f.close()
	except Exception as erro:
		cenario_traduzido.set(erro)
		

root = Tk()
root.title("Tradutor de Cenários")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Selecione o Cenário que deseja traduzir:").grid(column=1, row=1, sticky=W)

cenario_ingles = StringVar()
cenario_ingles_entry = ttk.Entry(mainframe, width=64, textvariable=cenario_ingles)
cenario_ingles_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Procure", command=findFile).grid(column=3, row=1, sticky=W)

cenario_traduzido = StringVar()
ttk.Label(mainframe, textvariable=cenario_traduzido).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Traduzir", command=tradutorBotC).grid(column=3, row=2, sticky=W)

root.bind("<Return>", tradutorBotC)

root.mainloop()