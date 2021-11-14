import os
from tkinter import *  

root = Tk()

label= Label(root, text= "Algorithm to JavaScript", font= ('Helvetica', 25))
label.pack(pady=20)
Label(root, text= "Code"+"\t"*7 +"       Output", font= ('Helvetica 15')).pack(pady=20, side= TOP, anchor="w")

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


text1 = Text(root, width=80, height=30)
text2 = Text(root,width=80,height=30)
scrollbar = Scrollbar(root)
scrollbar.config(command=text1.yview)
text1.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=top, side=RIGHT, fill=Y)
text1.pack(in_=top, side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=text2.yview)
text2.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=top, side=LEFT, fill=Y)
text2.pack(in_=top, side=RIGHT, fill=BOTH, expand=True)

def rst():
    text1.delete(1.0, "end")
    text2.delete(1.0, "end")

def compile():
    text2.delete(1.0, "end")
    inp = text1.get(1.0,"end")
    f = open("in.txt","w")
    f.write(inp)
    f.close()
    os.system('ATOJS < in.txt > out.txt')
    f = open("out.txt","r")
    out = f.read()
    f.close()
    text2.insert("end-1c", str(out))



compilebtn = Button(root, text="Compile", width=10, height=2,fg="green",command=compile)
resetbtn = Button(root, text="Reset", width=10, height=2,fg='red',command=rst)
compilebtn.pack(in_=bottom, side=LEFT)
resetbtn.pack(in_=bottom, side=LEFT)

root.mainloop()