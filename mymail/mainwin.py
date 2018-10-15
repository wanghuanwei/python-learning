from tkinter import *
import sendmail
import tkinter.messagebox as messagebox
import logging

class SendTheMail(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.newWindow()
        logging.info('init windows finished')

    def send(self):
        sender_var=self.sender_entry.get()  or 'testtttt'
        reciever_var=self.reciever_entry.get()
        pwd_var=self.pwd_entry.get()
        title_var=self.title_entry.get()
        subject_var=self.subject_entry.get('1.0',END)
        sendmail.sendmail(sender_var,reciever_var,pwd_var,title_var,subject_var)
        logging.info('send mail success')
        '''
        弹窗告警邮件发送成功
        点击确定后，清空所有输入框
        '''
        messagebox.showinfo('发送成功', '邮件发送成功')
        self.sender_entry.delete(0,END)
        self.reciever_entry.delete(0,END)
        self.pwd_entry.delete(0,END)
        self.title_entry.delete(0,END)
        self.subject_entry.delete('1.0', END)
        logging.info('clear input success')

    def newWindow(self):
        self.sender_label=Label(text='发件人:')
        self.sender_label.place(x=30,y=20,width=60,height=30)
        self.sender_entry=Entry(bd=3,relief='sunken',highlightcolor='red')
        self.sender_entry.pack(side='right')
        self.sender_entry.place(x=100,y=20,height=30)

        self.reciever_label=Label(text='收件人:')
        self.reciever_label.place(x=30,y=70,width=60,height=30)
        self.reciever_entry=Entry(bd=3,relief='sunken', highlightcolor='red')
        self.reciever_entry.pack(side='right')
        self.reciever_entry.place(x=100,y=70,height=30,width=360)

        self.pwd_label=Label(text='SMTP密码:')
        self.pwd_label.place(x=30,y=120,width=60,height=30)
        self.pwd_entry=Entry(bd=3,show='*')
        self.pwd_entry.pack(side='right')
        self.pwd_entry.place(x=100,y=120,height=30)

        self.title_label=Label(text='邮件标题:')
        self.title_label.place(x=30,y=180,width=60,height=30)
        self.title_entry=Entry(bd=3,relief='sunken',highlightcolor='red')
        self.title_entry.pack(side='right')
        self.title_entry.place(x=100,y=180,height=30,width=360)

        self.subject_label=Label(text='邮件正文:')
        self.subject_label.place(x=30,y=230,width=60,height=30)
        self.subject_entry=Text(bd=3,relief='sunken', highlightcolor='red')
        self.subject_entry.pack(side='right')
        self.subject_entry.place(x=30,y=280,height=250,width=540)

        self.send_button = Button(text='发送', command=self.send)
        self.send_button.place(x=270,y=550,height=30,width=60)

logging.basicConfig(level= logging.INFO)

mywin=SendTheMail()
mywin.master.title('自定义的邮件发送端')
mywin.master.minsize(600,600)
mywin.mainloop()
