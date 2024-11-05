import configparser

config = configparser.ConfigParser()
config.read('binance_bot/app_manager/config.ini')

width_scale = config.getfloat('parameters', 'width_scale')
height_scale = config.getfloat('parameters', 'height_scale')

class User():
    def __init__(self, root):
        self.root = root
        self.get_window_size()
        self.get_ip_address()
        
    def get_window_size(self):
        self.width = int(width_scale * self.root.winfo_screenwidth())
        self.height = int(width_scale * self.root.winfo_screenheight())
    
    def get_ip_address(self):
        pass