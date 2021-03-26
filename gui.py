import tkinter as tk
from tkinter import ttk
from BDAccess import BDAccess
import sys

class MainGui:
    def __init__(self, window):
        self.objDB = BDAccess()

        self.labelCode = tk.Label(window, text='Product code')
        self.labelName = tk.Label(window, text='Product name')
        self.labelPrice = tk.Label(window, text='Price')

        self.textCode = tk.Entry(bd=3)
        self.textName = tk.Entry()
        self.textPrice = tk.Entry()

        self.buttonRegister = tk.Button(window, text='Register', command=self.insertProduct)
        self.buttonUpdate = tk.Button(window, text='Update', command=self.updateProduct)
        self.buttonDelete = tk.Button(window, text='Delete', command=self.deleteProduct)
        self.buttonClear = tk.Button(window, text='Clear', command=self.clearInputs)

        self.columnData = ("Code", "Name", "Price")
        self.treeProducts = ttk.Treeview(window, columns=self.columnData, selectmode='browse')
        self.scrollbar = ttk.Scrollbar(window, orient='vertical', command=self.treeProducts.yview)
        self.scrollbar.pack(side='right', fill='x')

        self.treeProducts.configure(yscrollcommand=self.scrollbar.set)
        self.treeProducts.heading('Code', text='Code')
        self.treeProducts.heading('Name', text='Name')
        self.treeProducts.heading('Price', text='Price')
        self.treeProducts.column('Code', minwidth=0, width=100)
        self.treeProducts.column('Name', minwidth=0, width=100)
        self.treeProducts.column('Price', minwidth=0, width=100)

        self.treeProducts.pack(padx=10, pady=10)
        self.treeProducts.bind("<<TreeviewSelect>>", self.showSelectedRegisters)

        self.labelCode.place(x=100, y=50)
        self.textCode.place(x=250, y=50)

        self.labelName.place(x=100, y=100)
        self.textName.place(x=250, y=100)

        self.labelPrice.place(x=100, y=150)
        self.textPrice.place(x=250, y=150)

        self.buttonRegister.place(x=100, y=200)
        self.buttonUpdate.place(x=200, y=200)
        self.buttonDelete.place(x=300, y=200)
        self.buttonClear.place(x=400, y=200)

        self.treeProducts.place(x=100, y=300)
        self.scrollbar.place(x=805, y=300, height=225)

        self.loadFirstData()

    def showSelectedRegisters(self, event):
        self.clearInputs()
        for selection in self.treeProducts.selection():
            item = self.treeProducts.item(selection)
            code, name, price = item['values'][0:3]
            self.textCode.insert(0, code)
            self.textName.insert(0, name)
            self.textPrice.insert(0, price)

    def loadFirstData(self):
        try:
            self.id = 0
            self.iid = 0
            registers = self.objDB.selectData()
            for item in registers:
                code = item[0]
                name = item[1]
                price = item[2]

                self.treeProducts.insert('', 'end', iid=self.iid, values=(code, name, price))

                self.iid = self.iid + 1
                self.id = self.id + 1

            print("Base data")

        except:
            print("No data to show")

    def readFields(self):

        try:
            code = int(self.textCode.get())
            name = self.textName.get()
            price = float(self.textPrice.get())

        except:
            print("Couldn't read data")

        return code, name, price

    def insertProduct(self):
        try:
            code, name, price = self.readFields()
            self.objDB.insertData(code, name, price)
            self.treeProducts.insert('oi', 'end', iid=self.iid, values=(code, name, price))

            self.iid = self.iid + 1
            self.id = self.id + 1
            self.clearInputs()

        except:
            print("Couldn't save data")

    def updateProduct(self):
        try:
            code, name, price = self.readFields()
            self.objDB.updateData(code, name, price)
            self.treeProducts.delete(*self.treeProducts.get_children())
            self.loadFirstData()

            self.clearInputs()

        except:
            print("Couldn't update data")

    def deleteProduct(self):
        try:
            code, name, price = self.readFields()
            self.objDB.deleteData(code)
            self.treeProducts.delete(*self.treeProducts.get_children())
            self.loadFirstData()

            self.clearInputs()

        except (RuntimeError, TypeError, NameError, Exception):
            print(sys.exc_info()[1])

    def clearInputs(self):
        try:
            self.textCode.delete(0, tk.END)
            self.textName.delete(0, tk.END)
            self.textPrice.delete(0, tk.END)
            print('Clear data')

        except:
            print("Couldn't clear data")
