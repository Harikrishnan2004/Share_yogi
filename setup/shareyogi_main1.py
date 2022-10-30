import pickle
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
import os
import socket
import tqdm

dict={}
ga=' '
ba=' '
start=Tk()
start.title("SHARE YOGI")
start.geometry("900x720")
start.configure(bg="#6ee7ff")
start.resizable("false","true")

def g_avatar():
    global ga
    ga="true"
    Label(start,text="Avatar selected",font=('Acumin Variable Concept',10,'bold'),bg='#6ee7ff',
          fg='#fff').place(x=780,y=40)
    
def b_avatar():
    global ba
    ba="true"
    Label(start,text="Avatar selected",font=('Acumin Variable Concept',10,'bold'),bg='#6ee7ff',
          fg='#fff').place(x=780,y=40)
    

def avatar():
    avatar=Toplevel(start)
    avatar.title("AVATAR")
    avatar.geometry("500x500")
    avatar.configure(bg="#a7e7fa")
    avatar.resizable("false","true")

    girl_avatar=PhotoImage(file="IMAGES/girl.avatar.png")
    Label(avatar,image=girl_avatar).place(x=50,y=100)
    boy_avatar=PhotoImage(file="IMAGES/boy.avatar.png")
    Label(avatar,image=boy_avatar,bg="#f4fdfe").place(x=250,y=100)

    Button(avatar,text="GIRL",width=8,height=1,font=("Acumin Variable Concept",10),bg="#1fcbff",fg="#fff",relief='ridge',
       command=g_avatar).place(x=110,y=225)
    Button(avatar,text="BOY",width=8,height=1,font=("Acumin Variable Concept",10),bg="#1fcbff",fg="#fff",relief='ridge',
       command=b_avatar).place(x=310,y=225)

    avatar.mainloop()

def dup():
    file=open(os.getcwd() + '\\' + "user_database.txt",'rb')
    
    while True:
        try:
            data = pickle.load(file)
            for username in data:
                if username == user_id.get():
                    return 1  
        except EOFError:
            break
    file.close()
    

def sign_up():

    d=dup()
    if(d==1):
        Label(start,text="User already exist",font=('Acumin Variable Concept',10,'bold'),bg='#6ee7ff',
              fg='#f51616').place(x=310,y=670)
        
    else:
        file=open(os.getcwd() + '\\' + "user_database.txt",'ab')
        dict[user_id.get()]={}
        dict[user_id.get()]['pass']=password.get()
        if(ga=="true"):
            dict[user_id.get()]['sex']="female"
        elif(ba=="true"):
            dict[user_id.get()]['sex']="male"
        else:
            dict[user_id.get()]['sex']="none"

        pickle.dump(dict,file)
        file.close()
        Label(start,text="Succesfully signed in",font=('Acumin Variable Concept',10,'bold'),bg='#6ee7ff',
              fg='#fff').place(x=310,y=670)

    

def root():
    file=open(os.getcwd() + '\\' + "user_database.txt",'rb')
    data = {}
    while True:
        try:
            d = pickle.load(file)
            for username in d:
                data[username] = d[username]
        except EOFError:
            break
    file.close()
    for i in data:
        
        if(i==user_id.get()):
            if(data[i]['pass']==password.get()):
                root1=Toplevel(start)
                root1.title("SHARE YOGI")
                root1.geometry("900x720")
                root1.configure(bg="#f4fefe")
                root1.resizable("false","false")
                
                #icon
                image_icon=PhotoImage(file="IMAGES/yogilogo.png")
                root1.iconphoto("false",image_icon)
                
                if(data[user_id.get()]['sex']=="female"):
                    account_logo=PhotoImage(file="IMAGES/g.avatar1.png")
                    Label(root1,image=account_logo).place(x=680,y=0)
                elif(data[user_id.get()]['sex']=="male"):
                    account_logo=PhotoImage(file="IMAGES/boy.avatar1.png")
                    Label(root1,image=account_logo).place(x=680,y=0)
                else:
                    account_logo=PhotoImage(file="IMAGES/account.logo.png")
                    Label(root1,image=account_logo).place(x=680,y=0)

                Label(root1,text=f'@{user_id.get()}',font=('Javanese Text',10),bg='#f4fdfe').place(x=750,y=35)

                Label(root1,text="FILE SHARING APPLICATION",font=('Javanese Text',20),bg="#f4fdfe").place(x=75,y=20)
                Frame(root1,width=800,height=2,bg="#000000").place(x=25,y=80)

                send_image=PhotoImage(file="IMAGES/send.icon.png")
                Button(root1,image=send_image,bg="#f4fdfe",bd=0,command=send1).place(x=100,y=100)
                

                receive_image=PhotoImage(file="IMAGES/receive.icon.png")
                Button(root1,image=receive_image,bg="#f4fdfe",bd=0,command=receive1).place(x=544,y=100)
                

                Label(root1,text="Send",font=('Acumin Variable Concept',20),bg="#f3fdfe").place(x=220,y=320)
                Label(root1,text="Receive",font=('Acumin Variable Concept',20),bg="#f3fdfe").place(x=640,y=320)

                Background=PhotoImage(file="IMAGES/background.png")
                Label(root1,image=Background).place(x=35,y=400)
                root1.mainloop()
            else:
                Label(start,text="Incorrect password or username",font=('Acumin Variable Concept',10),bg='#6ee7ff',
                  fg='#f51616').place(x=310,y=670)


def send1():
    window=Toplevel(start)
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
        port=9999
        s.bind((host,port))
        s.listen()
        print(host)
        print("waiting for internal connections")
        conn,addr=s.accept()
        file=open(filename,'rb')
        while True:
            data=file.read(1024)
            if not data:
                break
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

    window.mainloop()

def receive1():
    main=Toplevel(start)
    main.title("RECEIVE")
    main.geometry("900x720")
    main.configure(bg="#f4fefe")
    main.resizable("false","false")

    def receiver():
        ID=sender_id.get()
        filename1=file_name.get()
        s=socket.socket()
        port=9999
        s.connect((ID,port))
        file=open(filename1,'wb')
        while True:
            data=s.recv(1024)
            if not data:
                break
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
start.iconphoto("false",image_icon)

Background=PhotoImage(file="IMAGES/yogilogo.png")
Label(start,image=Background).place(x=190,y=20)

Label(start,text="Enter your user name",font="arial 15 bold",bg="#6ee7ff",fg='#fff').place(x=190,y=550)
user_id=Entry(start,width=30,fg="black",border=2,bg='white',font=('arial',10),justify=CENTER,relief='ridge')
user_id.place(x=190,y=580)
Label(start,text="Enter your user password",font="arial 15 bold",bg="#6ee7ff",fg='#fff').place(x=490,y=550)
password=Entry(start,width=30,fg="black",show='*',border=2,bg='white',font=('arial',10),justify=CENTER,relief='ridge')
password.place(x=490,y=580)


Button(start,text="LOGIN",width=8,height=1,font="arial 17 bold",bg="#fff",fg="#1fcbff",relief='ridge',
       command=root).place(x=300,y=620)

Button(start,text="SIGN UP",width=8,height=1,font="arial 17 bold",bg="#fff",fg="#000",relief='ridge',
       command=sign_up).place(x=460,y=620)

Button(start,text="AVATAR",width=8,height=1,font=("Acumin Variable Concept",10),bg="#1fcbff",fg="#fff",relief='ridge',
       command=avatar).place(x=800,y=10)

mainloop()



    












