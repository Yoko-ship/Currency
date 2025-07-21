import currencyapicom
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import ttk

#* Загрузка
load_dotenv()
apiKey = os.environ.get("APIKEY")
client = currencyapicom.Client(apiKey)

def get_currency_rate():
    baseCurrency = baseCurrencyEntry.get().upper()
    currency = currencyEntry.get().upper()
    if not baseCurrency or not currency:
        rate_result_label.config(text="Пожалуста заполните все поля",fg="red")
        return
    try:
        result = client.latest(baseCurrency,currencies=[currency])
        value = round(result['data'][currency]["value"],4)
        rate_result_label.config(text=f"{baseCurrency} = {value} {currency}",fg="black")
    except Exception:
        rate_result_label.config(text="Произошла ошибка при получении курса",fg="red")



def convertCurrencyInto():
    baseCurrency = baseCurrencyConvertEntry.get().upper()
    sum_entry = sumEntry.get()
    currency = currencyConvertEntry.get().upper()
    if not baseCurrency or not sum_entry or not currency:
        convert_result_rate.config(text="Пожалуста заполните все поля",fg="red")
        return
    try:
        amount = float(sum_entry)
        result = client.latest(baseCurrency,currencies=[currency])
        value = result['data'][currency]["value"]
        finalResult = round(amount * value,2)
        convert_result_rate.config(text=f"{amount} {baseCurrency} = {finalResult} {currency}",fg='green')
    except Exception:
        convert_result_rate.config(text="Произошла ошибка при получении курса",fg="red")


#* UI
root = tk.Tk()
root.geometry("400x400")
root.title("Currency")
notebook = ttk.Notebook(root)
notebook.pack(expand=True,fill='both')
currencyRate = ttk.Frame(notebook)
currencyConvert = ttk.Frame(notebook)
notebook.add(currencyRate,text="Узнать курс")
notebook.add(currencyConvert,text="Преобразовать валюту")
FONT = ("Helvetica",14)
padding = 5
##* Курс

tk.Label(currencyRate,text="Базовая валюта",font=FONT).pack(pady=padding)
baseCurrencyEntry = tk.Entry(currencyRate,font=FONT,width=30,bd=2,relief="solid")
baseCurrencyEntry.pack(pady=padding)
tk.Label(currencyRate,text="Курс какой валюты хотите получить",font=FONT).pack(pady=padding)
currencyEntry = tk.Entry(currencyRate,font=FONT,width=30,bd=2,relief="groove")
currencyEntry.pack(pady=padding)
confirmButton = tk.Button(currencyRate,text="Подтвердить",fg="white",bg="green",font=FONT,command=get_currency_rate).pack(pady=padding)
rate_result_label = tk.Label(currencyRate,text="",font=FONT)
rate_result_label.pack(pady=padding)
#* Преобразовать

tk.Label(currencyConvert,text="Базовая валюта",font=FONT).pack(pady=padding)
baseCurrencyConvertEntry = tk.Entry(currencyConvert,font=FONT,width=30,bd=2,relief="groove")
baseCurrencyConvertEntry.pack(pady=padding)
tk.Label(currencyConvert,text="Сумма",font=FONT).pack(pady=padding)
sumEntry = tk.Entry(currencyConvert,font=FONT,width=30,bd=2,relief="groove",validate="key",validatecommand=(currencyConvert.register(lambda s: s.isdigit() or s == ""),"%S"))
sumEntry.pack(pady=padding)
tk.Label(currencyConvert,text="Валюта",font=FONT).pack(pady=padding)
currencyConvertEntry = tk.Entry(currencyConvert,font=FONT,width=30,bd=2,relief="groove")
currencyConvertEntry.pack(pady=padding)
confirmConvertButton = tk.Button(currencyConvert,text="Подтвердить",fg="white",bg="green",font=FONT,command=convertCurrencyInto).pack(pady=padding)
convert_result_rate = tk.Label(currencyConvert,text="",font=FONT)
convert_result_rate.pack(pady=padding)
root.mainloop()

