from tkinter import *
import math

class Bhaskara(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.interface()

    def interface(self):
        self.labelA = Label(self, text="A =")
        self.labelB = Label(self, text="B =")
        self.labelC = Label(self, text="C =")

        self.entryA = Entry(self)
        self.entryB = Entry(self)
        self.entryC = Entry(self)

        self.calcular = Button(self, text="Calcular", command = self.calcular)

        #Posicionando os elementos

        self.labelA.grid(row=0, column=0)
        self.entryA.grid(row=0, column=1)

        self.labelB.grid(row=1, column=0)
        self.entryB.grid(row=1, column=1)

        self.labelC.grid(row=2, column=0)
        self.entryC.grid(row=2, column=1)

        self.calcular.grid(row=3, column=1)

        self.pack()

    def calcular(self):

        A = int(self.entryA.get())
        B = int(self.entryB.get())
        C = int(self.entryC.get())

        delta = (B * B) - 4 * A * C
        if delta > 0:
            raizd = math.sqrt(delta)
            X1 = ((-B) + raizd) / (2 * A)
            X2 = ((-B) - raizd) / (2 * A)

            self.exibir_resultado(X1, X2)
        else:
            self.exibir_erro()

    def exibir_resultado(self,X1,X2):

        popup = Toplevel(self)

        resultadoX1 = "X1 = " + str(X1)
        resultadoX2 = "X2 = " + str(X2)

        self.labelX1 = Label(popup, text=resultadoX1)
        self.labelX2 = Label(popup, text=resultadoX2)

        self.labelX1.grid(row=4, column=1)
        self.labelX2.grid(row=5, column=1)

        self.pack()
        popup.mainloop()

    def exibir_erro(self):
        self.labelErro = Label(self, text="Erro! Tente novamente.")
        self.labelErro.grid(row=4, column=1)


