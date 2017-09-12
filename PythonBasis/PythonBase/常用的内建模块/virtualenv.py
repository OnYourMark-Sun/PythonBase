from tkinter import *
#label 显示
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.creteui()
    def creteui(self):
        self.hellolabel = Label(self)
        self.hellolabel.pack()
        self.quitbutton = Button(self,text='jhkajg',command=self.quit)
        self.quitbutton.pack()

#app = Application()
#app.master.title('Label显示')
#app.mainloop()

#输入框

import tkinter.messagebox as messagebox
class Applications(Frame):
    def __init__(self,mester = None):
        Frame.__init__(self,mester)
        self.pack()
        self.createui()
    def createui(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alerButton = Button(self,text='Hellode',command=self.hello)
        self.alerButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'word'
        messagebox.showinfo('Message',name)

app = Applications()
app.master.title('输入框')
app.mainloop()