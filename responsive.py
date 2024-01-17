import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self,start_size):
        super().__init__()
        self.title("Responsive layout")
        self.geometry(f'{start_size[0]}x{start_size[1]}')
        
        SizeNotifier(self,{600:self.create_small_layout, 300:self.create_medium_layout})
        
        self.mainloop()
    
    def create_small_layout(self):
        print("small layout")    

    def create_medium_layout(self):
        print("medium layout")    


class SizeNotifier:
    def __init__(self,window,size_dict):
        self.window =window
        self.size_dict={key: value for key, value in sorted(size_dict.items())}    
        self.current_min_size = None
        
        self.window.update()
        
        min_height =self.window.winfo_width()
        print(min_height)
        min_width= list(self.size_dict)[0]
        self.window.min_size(min_width,min_height)
        
        self.window.bind('<Configure>', self.check_size)
    
    def check_size(self,event):
        window_width = event.window_width
        check_size= None
        
        
        for min_size in self.size_dict:
            delta =window_width - min_size
            if delta >= 0:
                checked_size = min_size
        
        if checked_size != self.current_min_size:
            self.current_min_size=checked_size
            self.size_dict[self.current_min_size]()    

App((400,600))