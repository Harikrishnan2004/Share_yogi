from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
import os
import socket


root=Tk()
root.title("SHARE YOGI")
root.geometry("900x720")
root.configure(bg="#f4fefe")
root.resizable("false","false")

def sample():
    sample=Toplevel(send)
    

def send():
    window=Toplevel(root)
    window.title("SEND")
    window.geometry("900x720")
    window.configure(bg="#f4fefe")
    window.resizable("false","false")

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select image file',
                                            filetype=(('file_type','*.txt'),('all files','*.*')))

    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("waiting for internal connections")
        conn,addr=s.accept()
        file=open(filename,'rb')
        data=file.read(1024)
        conn.send(data)
        print("data has been transmitted successfully ... ")
        file.close()
        
        
    
    #icon
    image_icon=PhotoImage(file="IMAGES/send.icon.png")
    window.iconphoto("false",image_icon)
    
    
    Sbackground=PhotoImage(file="IMAGES/sendbackground.png")
    Label(window,image=Sbackground).place(x=-2,y=-25)
    Mbackground=PhotoImage(file="IMAGES/send.logo1.png")
    Label(window,image=Mbackground,bg="#f4fdfe").place(x=320,y=350)

    host=socket.gethostname()
    Label(window,text=f' ID: {host}',font=('Javanese Text',7),bg='white',fg='black').place(x=490,y=375)

    Button(window,text="+ Add File",width=10,height=2,font="arial 14 bold",bg="#fff",fg="#000",command=select_file).place(x=700,y=200)
    Button(window,text="Send File",width=10,height=2,font="arial 14 bold",bg="#000",fg="#fff",command=sender).place(x=550,y=200)
    Button(window,text="sample",width=10,height=2,font="arial 14 bold",bg="#fff",fg="#000",command=sample).place(x=200,y=200)

    window.mainloop()

    
    
def receive():
    main=Toplevel(root)
    main.title("RECEIVE")
    main.geometry("900x720")
    main.configure(bg="#f4fefe")
    main.resizable("false","false")

    def receiver():
        ID=sender_id.get()
        filename1=file_name.get()
        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wp')
        data=s.recv(1024)
        file.write(data)
        file.close()
        print("file has been received succesfully....")
        
        
    
    #icon
    image_icon=PhotoImage(file="IMAGES/receive.icon.png")
    main.iconphoto("false",image_icon)

    sbackground=PhotoImage(file="IMAGES/receive.background.png")
    Label(main,image=sbackground).place(x=-2,y=-25)

    Label(main,text="Input sender ID",font=('arial',15,'bold'),bg="#f4fdfe").place(x=20,y=300)
    sender_id=Entry(main,width=30,fg="black",border=2,bg='white',font=('arial',15))
    sender_id.place(x=20,y=350)
    sender_id.focus()

    Label(main,text="File name Incoming File",font=('arial',15,'bold'),bg="#f4fdfe").place(x=20,y=400)
    file_name=Entry(main,width=30,fg="black",border=2,bg='white',font=('arial',15))
    file_name.place(x=20,y=450)
    file_name.focus()

    Rec=Button(main,text="Receive",compound=LEFT,height=1,width=20,font=('arial',20,'bold'),bg="#eefa0c",fg='#000',command=receiver)
    Rec.place(x=20,y=550)

    

    main.mainloop()

#icon
image_icon=PhotoImage(file="IMAGES/yogilogo.png")
root.iconphoto("false",image_icon)

Label(root,text="FILE SHARING APPLICATION",font=('Javanese Text',20),bg="#f4fdfe").place(x=75,y=20)
Frame(root,width=800,height=2,bg="#000000").place(x=25,y=80)

send_image=PhotoImage(file="IMAGES/send.icon.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=send)
send.place(x=100,y=100)

receive_image=PhotoImage(file="IMAGES/receive.icon.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=receive)
receive.place(x=544,y=100)

Label(root,text="Send",font=('Acumin Variable Concept',20),bg="#f3fdfe").place(x=220,y=320)
Label(root,text="Receive",font=('Acumin Variable Concept',20),bg="#f3fdfe").place(x=640,y=320)

Background=PhotoImage(file="IMAGES/background.png")
Label(root,image=Background).place(x=35,y=400)







