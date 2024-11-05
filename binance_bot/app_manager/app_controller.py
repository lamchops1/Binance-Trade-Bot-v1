from binance_bot.views.dashboard.dashboard_view import DashboardView

class AppController():
    def __init__(self, root, binance):
        self.root = root
        self.binance = binance
        self.dashboard()
        
    def dashboard(self):
        DashboardView(self.root, self.binance)
        
        
        
        