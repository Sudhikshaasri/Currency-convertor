# Currency Converter

import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        
        self.currencies = self.get_currencies()
        self.create_widgets()

    def get_currencies(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        return response.json()['rates']

    def create_widgets(self):
        self.from_currency = ttk.Combobox(self.root, values=list(self.currencies.keys()))
        self.from_currency.grid(column=0, row=0)
        self.from_currency.set("Select Currency")

        self.amount = tk.Entry(self.root)
        self.amount.grid(column=1, row=0)

        self.to_currency = ttk.Combobox(self.root, values=list(self.currencies.keys()))
        self.to_currency.grid(column=2, row=0)
        self.to_currency.set("Select Currency")

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert)
        self.convert_button.grid(column=3, row=0)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(column=0, row=1, columnspan=4)

    def convert(self):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        amount = float(self.amount.get())
        if from_currency in self.currencies and to_currency in self.currencies:
            converted_amount = amount * (self.currencies[to_currency] / self.currencies[from_currency])
            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
