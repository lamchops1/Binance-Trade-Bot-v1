from binance_bot.views.dashboard.dashboard_view import DashboardView

class AppController():
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
        
    def dashboard(self):
        DashboardView(self.root, 
                      self.binance, 
                      self.logo,
                      self.name,
                      self.api,
                      self.secret,
                      self.login_frame)

app_controller = None

def run_app_controller(root, 
                       binance, 
                       logo,
                       name,
                       api,
                       secret,
                       login_frame): 
    global app_controller
    if app_controller is None:
        print('being executed')
        app_controller = AppController(root,
                                       binance, 
                                       logo,
                                       name,
                                       api,
                                       secret,
                                       login_frame)
        return app_controller
    
        
        
        
        