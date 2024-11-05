import tkinter as tk

from binance_bot.binance_api.binance_login import BinanceLogin
from binance_bot.app_manager.app_controller import run_app_controller, app_controller

class ConfigureLogo():
    def __init__(self, root):
        self.root = root
        self.initialise_logo()
        
    def initialise_logo(self):
        self.logo_frame = tk.Frame(self.root)
        self.logo_frame.grid(row=7, 
                        column=2, 
                        rowspan=3, 
                        columnspan=6, 
                        sticky='nsew')
        logo_label = tk.Label(self.logo_frame, 
                              text="Binance Bot Trader v1", 
                              font=('Courier', 20), 
                              bg='green', 
                              fg='yellow', 
                              anchor='center')
        logo_label.pack(fill='both', expand=True)

class ConfigureNameEntry():
    def __init__(self, root):
        self.root = root
        self.initialise_name_entry()
        
    def initialise_name_entry(self):
        self.name_frame = tk.Frame(self.root, bg='red')                  
        self.name_frame.grid(row=10, 
                        column=3, 
                        rowspan=1, 
                        columnspan=4, 
                        sticky='nsew')
        self.name = tk.StringVar(value="Enter name")
        name_entry = tk.Entry(self.name_frame, 
                              textvariable=self.name, 
                              width=1, 
                              bg='blue', 
                              font=('Courier', 12))
        name_entry.pack(fill='both', expand=True)
        name_entry.bind("<FocusIn>", lambda event: self.clear_entry(self.name, "Enter name"))
        name_entry.bind("<FocusOut>", lambda event: self.set_entry(self.name, "Enter name"))
        
    def clear_entry(self, entry_var, placeholder):
        if entry_var.get() == placeholder:
            entry_var.set("")  

    def set_entry(self, entry_var, placeholder):
        if entry_var.get() == "":
            entry_var.set(placeholder) 

class ConfigureApiKeyEntry():
    def __init__(self, root):
        self.root = root
        self.initialise_api_key_entry()
        
    def initialise_api_key_entry(self):
        self.api_key_frame = tk.Frame(self.root, bg='green')
        self.api_key_frame.grid(row=11, 
                           column=3, 
                           rowspan=1, 
                           columnspan=4, 
                           sticky='nsew')
        self.api_key = tk.StringVar(value="Enter api key")
        api_key_entry = tk.Entry(self.api_key_frame, 
                                 textvariable=self.api_key, 
                                 width=1, 
                                 bg='blue', 
                                 font=('Courier', 12))
        api_key_entry.pack(fill='both', expand=True)
        api_key_entry.bind("<FocusIn>", lambda event: self.clear_entry(self.api_key, "Enter api key"))
        api_key_entry.bind("<FocusOut>", lambda event: self.set_entry(self.api_key, "Enter api key"))
        
    def clear_entry(self, entry_var, placeholder):
        if entry_var.get() == placeholder:
            entry_var.set("")  

    def set_entry(self, entry_var, placeholder):
        if entry_var.get() == "":
            entry_var.set(placeholder) 

        
class ConfigureSecurityKeyEntry():
    def __init__(self, root):
        self.root = root
        self.initialise_secret_key_entry()
        
    def initialise_secret_key_entry(self):
        self.secret_key_frame = tk.Frame(self.root, bg='pink')
        self.secret_key_frame.grid(row=12, 
                                column=3, 
                                rowspan=1, 
                                columnspan=4, 
                                sticky='nsew')
        self.secret_key = tk.StringVar(value="Enter security key")
        secret_key_entry = tk.Entry(self.secret_key_frame, 
                                      textvariable=self.secret_key, 
                                      width=1, 
                                      bg='blue', 
                                      font=('Courier', 12))
        secret_key_entry.pack(fill='both', expand=True)
        secret_key_entry.bind("<FocusIn>", lambda event: self.clear_entry(self.secret_key, "Enter security key"))
        secret_key_entry.bind("<FocusOut>", lambda event: self.set_entry(self.secret_key, "Enter security key"))
    
    def clear_entry(self, entry_var, placeholder):
        if entry_var.get() == placeholder:
            entry_var.set("")  

    def set_entry(self, entry_var, placeholder):
        if entry_var.get() == "":
            entry_var.set(placeholder) 
        
class ConfigureLoginButton():
    def __init__(self, root, logo, name, api, secret):
        self.root = root
        self.logo = logo
        self.name = name
        self.api = api
        self.secret = secret
        self.initialise_login_button()
        
    def initialise_login_button(self):
        self.login_frame = tk.Frame(self.root, bg='purple')
        self.login_frame.grid(row=13, 
                         column=4, 
                         rowspan=1, 
                         columnspan=2, 
                         sticky='nsew')
        login_button = tk.Button(self.login_frame, 
                                 text="Login", 
                                 font=('Courier', 8), 
                                 command=self.cb_login)
        login_button.pack(fill='both', expand=True)
        
    def cb_login(self):
        self.binance = BinanceLogin(self.api.api_key.get(), self.secret.secret_key.get())
        if self.binance.authenticated:
            app_controller = run_app_controller(self.root, 
                               self.binance, 
                               self.logo,
                               self.name,
                               self.api,
                               self.secret,
                               self.login_frame)
            app_controller.dashboard()
            
            print("welcome")
        

        