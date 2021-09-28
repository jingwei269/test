import tkinter as tk 

root = tk.Tk()




def show():
    t1.replace("insert"," tkinter")
   
b1 = tk.Button(root,text="Click me", command=show)
b1.grid(row=0,column=0)

t1=tk.Text(root,height=1,width=20)
t1.grid(row=1,column=0)



root.mainloop()