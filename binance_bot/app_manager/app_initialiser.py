
from binance_bot.user_data.user import User
from binance_bot.views.login.login_view import LoginView


class AppInitialiser():
    def __init__(self, root):
        self.root = root
        self.get_user_data()
        self.load_window()
        self.setup_grid()
        self.login()
        
    def get_user_data(self):
        self.user = User(self.root)
        
    def load_window(self):
        self.root.title("Binance Bot Trader v1")
        self.root.geometry(f"{self.user.width}x{self.user.height}")
        self.root.configure(bg='black', highlightthickness=0, bd=0)
        
    def setup_grid(self):
        for row in range(20):
            self.root.grid_rowconfigure(row, weight=1)
        for col in range(10):
            self.root.grid_columnconfigure(col, weight=1)
        
    def login(self):
        LoginView(self.root) 
