from binance_bot.views.dashboard.dashboard_widgets import *

class DashboardView():
    def __init__(self, 
                 root, 
                 binance,
                 logo,
                 name,
                 api,
                 secret, 
                 login_frame):
        self.root = root
        self.binance = binance
        self.logo = logo
        self.name = name
        self.api = api
        self.secret = secret
        self.login_frame = login_frame
        self.destroy_login_view()
        self.configure_dashboard_view()
        
    def destroy_login_view(self):
        self.logo.logo_frame.destroy()
        self.name.name_frame.destroy()
        self.api.api_key_frame.destroy()
        self.secret.secret_key_frame.destroy()
        self.login_frame.destroy()
        
    def configure_dashboard_view(self):
        ConfigureBalance(self.root, self.binance)