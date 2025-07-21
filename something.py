import currencyapicom
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import ttk
load_dotenv()

apiKey = os.environ.get("APIKEY")
client = currencyapicom.Client(apiKey)

def getCurrencyRate():
    baseCurrency = baseCurrencyEntry.get().upper()
    currency = currencyEntry.get().upper()
    try:
        result = client.latest(baseCurrency,currencies=[currency])
        value = result['data'][currency]["value"]
        if(value):
            tk.Label(currencyRate,text=value,font=("Helteciva",14)).pack(pady=5)
    except Exception:
        tk.Label(currencyRate,text="Пожалуста заполните все поля",fg="red",font=("Helvetica",14)).pack(pady=5)



def convertCurrencyInto():
    baseCurrency = baseCurrencyConvertEntry.get().upper()
    try:
        sum = int(sumEntry.get())
    except ValueError:
        tk.Label(currencyConvert,text="Сумма принимает только число").pack(pady=5)
    currency = currencyConvertEntry.get().upper()
    try:

        result = client.latest(baseCurrency,currencies=[currency])
        value = result['data'][currency]["value"]
        finalResult = sum * value
        tk.Label(currencyConvert,text=finalResult,font=("Helvetica",14)).pack(pady=5)
    except Exception:
        tk.Label(currencyConvert,text="Пожалуста заполните все поля",fg="red",font=("Helvetica",14)).pack(pady=5)

root = tk.Tk()
root.geometry("400x400")
root.title("Currency")
notebook = ttk.Notebook(root)
notebook.pack(expand=True,fill='both')
currencyRate = ttk.Frame(notebook)
currencyConvert = ttk.Frame(notebook)
notebook.add(currencyRate,text="Узнать курс")
notebook.add(currencyConvert,text="Преобразовать валюту")

##* Курс
tk.Label(currencyRate,text="Базовая валюта",font=("Helvetica",14)).pack(pady=5)
baseCurrencyEntry = tk.Entry(currencyRate,font=("Helvetica",14),width=30,bd=2,relief="solid")
baseCurrencyEntry.pack(pady=5)
tk.Label(currencyRate,text="Курс какой валюты хотите получить",font=("Helvetica",14)).pack(pady=5)
currencyEntry = tk.Entry(currencyRate,font=("Helvetica",14),width=30,bd=2,relief="groove")
currencyEntry.pack(pady=5)
confirmButton = tk.Button(currencyRate,text="Подтвердить",fg="white",bg="green",font=("Helvetica", 12),command=getCurrencyRate).pack(pady=5)

#* Преобразовать
tk.Label(currencyConvert,text="Базовая валюта",font=("Helvetica",14)).pack(pady=5)
baseCurrencyConvertEntry = tk.Entry(currencyConvert,font=("Helvetica",14),width=30,bd=2,relief="groove")
baseCurrencyConvertEntry.pack(pady=5)
tk.Label(currencyConvert,text="Сумма",font=("Helvetica",14)).pack(pady=5)
sumEntry = tk.Entry(currencyConvert,font=("Helvetica",14),width=30,bd=2,relief="groove",validate="key",validatecommand=(currencyConvert.register(lambda s: s.isdigit() or s == ""),"%S"))
sumEntry.pack(pady=5)
tk.Label(currencyConvert,text="Валюта",font=("Helvetica",14)).pack(pady=5)
currencyConvertEntry = tk.Entry(currencyConvert,font=("Helvetica",14),width=30,bd=2,relief="groove")
currencyConvertEntry.pack(pady=5)
confirmConvertButton = tk.Button(currencyConvert,text="Подтвердить",fg="white",bg="green",font=("Helvetica",14),command=convertCurrencyInto).pack(pady=5)
root.mainloop()

