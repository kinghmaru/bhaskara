from tkinter import Tk
from Bhaskara import Bhaskara

class Principal:
    if __name__ == '__main__':
        janela = Tk()
        janela.geometry("300x300+100+100")

        b = Bhaskara(janela)
        janela.mainloop()