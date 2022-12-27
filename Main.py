import tkinter as tk
from Cliente.Guia import Frame, Top_Menu


def main():
    root = tk.Tk()
    root.title("Inventario")
    #root.resizable(False, False)
    #root.iconbitmap()
    Top_Menu(root)
    app = Frame(root)

    app.mainloop()


if __name__ == "__main__":
    main()