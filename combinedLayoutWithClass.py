import tkinter as tk
from tkinter import ttk


def create_segment(parent,label_text,button_text):
    frame = ttk.Frame(parent)
    
    #grid layout
    frame.rowconfigure(0,weight=1)
    frame.columnconfigure((0,1,2), weight=1,uniform='a')
    #
    ttk.Label(frame,text=label_text).grid(row=0,column=0)
    ttk.Button(frame,text=button_text).grid(row=0,column=1,sticky='nsew')
    
    return frame



class Segment(ttk.Frame):
    def __init__(self,parent,label_text,button_text):
        super().__init__(master=parent)
        
        #grid layout
        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1,2), weight=1,uniform='a')
        
        ttk.Label(self,text=label_text).grid(row=0,column=0, sticky="nsew")
        ttk.Button(self,text=button_text).grid(row=0,column=1, sticky="nsew")
        
        self.create_exercise_box("go").grid(row=0,column=2, sticky="nsew")
        
        self.pack(expand=True,fill="both",padx=10,pady=10)
    
    def create_exercise_box(self,text):
        frame = ttk.Frame(self)
        
        entry = ttk.Entry(frame).pack(expand=True,fill="both")
        button= ttk.Button(frame,text=text).pack(expand=True,fill="both")
        
        return frame


#window
window = tk.Tk()
window.title("Widgets and return")
window.geometry("400x600")

#widgets 
Segment(window,"Ben Kuyu","Chier")
Segment(window,"Ben Kuyu","Parler")
Segment(window,"Ben Kuyu","Courrir")
Segment(window,"Ben Kuyu","Dormir")

# create_segment(window,"Effectuer le Payement","Envoyer").pack(pady=(100,20))
# create_segment(window,"retirer le solde","Envoyer").pack(pady=(40,20))
# create_segment(window,"tranferer de l'argent","Envoyer").pack(pady=(40,20))
# create_segment(window,"Effectuer le Payement","Envoyer").pack(pady=(40,20))



window.mainloop()