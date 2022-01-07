from tkinter import Frame, ttk

from window import MainWindow

class ParserWindow(MainWindow):
    
    def __init__(self):
        MainWindow.__init__(self)
        self.frame = Frame(self.mainFrame)
        self.assignUI()
        self.windowLoop()
        
    def assignUI(self):
        self.tree = ttk.Treeview(self.frame, columns=("test", "test2", "test3"))
        self.tree.heading('test', text="Test")
        self.tree.pack()
        self.tabs = ttk.Notebook(self.frame)
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="Tab 1")
        self.tabs.add(self.tab2, text="Tab 2")
        self.tabs.pack()
        self.frame.pack()
        self.mainFrame.pack()
    

if __name__ == "__main__":
    ParserWindow()