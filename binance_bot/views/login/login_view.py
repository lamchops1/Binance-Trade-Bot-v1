import tkinter as tk

from binance_bot.views.login.login_widgets import *

class LoginView():
    def __init__(self, root):
        self.root = root
        self.configure_view()
        
    def configure_view(self):
        logo = ConfigureLogo(self.root)
        name = ConfigureNameEntry(self.root)
        api = ConfigureApiKeyEntry(self.root)
        secret  = ConfigureSecurityKeyEntry(self.root)
        self.login = ConfigureLoginButton(self.root, 
                                          logo,
                                          name,
                                          api, 
                                          secret)
            
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        