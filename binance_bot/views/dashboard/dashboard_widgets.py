import tkinter as tk

class ConfigureBalance():
    def __init__(self, root, binance):
        self.root = root
        self.binance = binance
        self.initialise_header()
        self.initialise_balance()
        
    def initialise_header(self):
        self.logo_frame = tk.Frame(self.root, bg='yellow')
        self.logo_frame.grid(row=0, 
                         column=0, 
                         columnspan=1, 
                         sticky='nsew')
        logo_label = tk.Label(self.logo_frame, 
                              text="Binance Bot v1", 
                              font=('Courier', 10), 
                              bg='green', 
                              fg='yellow',
                              anchor='w')
        logo_label.pack(fill='x')
        
        header_empty = tk.Frame(self.root, bg='blue')
        header_empty.grid(row=0, 
                         column=1, 
                         rowspan=1, 
                         columnspan=7, 
                         sticky='nsew')
        
        self.user_frame = tk.Frame(self.root, bg='red')
        self.user_frame.grid(row=0, 
                         column=8, 
                         rowspan=1, 
                         columnspan=2, 
                         sticky='nsew')
        
        
    def initialise_balance(self):
        self.balance_frame = tk.Frame(self.root, bg='purple')
        self.balance_frame.grid(row=1, 
                         column=0, 
                         rowspan=1, 
                         columnspan=1, 
                         sticky='nsew')
        balance_label = tk.Label(self.balance_frame, 
                              text="Money: $30.92", 
                              font=('Courier', 10), 
                              bg='green', 
                              fg='yellow', 
                              anchor='center')
        balance_label.pack(expand=True)