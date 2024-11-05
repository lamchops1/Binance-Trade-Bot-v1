import tkinter as tk

from binance_bot.app_manager.app_initialiser import AppInitialiser

def main():
    root = tk.Tk()
    AppInitialiser(root)
    root.mainloop()

if __name__ == '__main__':
    main()
