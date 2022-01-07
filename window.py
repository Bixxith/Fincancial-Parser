from tkinter import Tk, Frame

class MainWindow():
    
    def __init__(self):
        self.window = Tk()
        self.mainFrame = Frame(self.window)
        self.setupWindow()
        
    def setupWindow(self):
        self.window.geometry("800x800")
        self.window.title("Financial Parser")
    
    def windowLoop(self):
        self.window.mainloop()

