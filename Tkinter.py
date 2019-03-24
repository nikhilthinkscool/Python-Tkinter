from tkinter import Tk
from tkinter import Label
from tkinter import Button

class SimpleTkinterGUI:
    def __init__(self,master):
        self.master = master
        master.title("Simple Gui")
        
        self.label=Label(master,text="python Gui ")
        self.label.pack()
        
        self.helloButton = Button(master, text="Say Hello", command=self.sayHello)
        self.helloButton.pack()
        
        self.closeButton = Button(master, text="close", command=master.quit)
        self.closeButton.pack()
        
    def sayHello(self):
        print("hello")
    
  
if __name__ == "__main__":
    root = Tk()
    mgui = SimpleTkinterGUI(root)
    root.mainloop()
        
