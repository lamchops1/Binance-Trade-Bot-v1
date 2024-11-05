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
        self.destroy_login()
        self.configure_view()
        
    def destroy_login(self):
        self.logo.logo_frame.destroy()
        self.name.name_frame.destroy()
        self.api.api_key_frame.destroy()
        self.secret.secret_key_frame.destroy()
        self.login_frame.destroy()
        
    def configure_view(self):
        pass