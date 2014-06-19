Code snippet examples
=====================

1. Using comprehensions to save work of creating GUI elements in tkinter. An example of conciseness and readability in Python. 

![GUI element toy](images/guicomp.png)

```Python 

from tkinter import *

class app:
    def __init__(self):
        self.root=Tk()
        self.root.title("Example")

        F=Frame(self.root)
        F.pack()
        
        self.listofwords=["Hey","I","am","a","list","of","words"]
        self.listofcolors=["blue","red","grey","white","yellow","green","brown"]
        #The labelgroup records all the IDs of each label
        self.LabelGroup=[Label(F,text=word,fg=color, bg="black", width=30) for word,color in zip(self.listofwords,self.listofcolors)]
        for label in self.LabelGroup: label.pack()
        
        functionlist=[self.reversetext,self.reversecolor]
        buttontext=["Reverse text", "Reverse color"]
        #The buttongroup just starts all the buttons,
        #since we won't alter the buttons themselves, so no need to keep their IDs
        ButtonGroup=[Button(F,width=14, text=words, command=func).pack(side=LEFT) for func,words in zip(functionlist, buttontext)]
        
        self.root.mainloop()

    def reversetext(self):
        self.listofwords.reverse()
        for label,word in zip(self.LabelGroup,self.listofwords):
            #Widgets configuration can be accessed like dicts!
            label["text"]=word

    def reversecolor(self):
        self.listofcolors.reverse()
        for label,word in zip(self.LabelGroup,self.listofcolors):
            label["fg"]=word


example=app()

```