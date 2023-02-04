from tkinter import *
from requests import get
##########################
#this  par window
###########################
window=Tk()
window.geometry('300x300+500+100')
window.resizable(0,0)
window.title('               >> My IP <<')
window.configure(bg='#d9b500')
#############################
#this par for programming
############################
#get('https://www.ipify.org/').text كودات الصفة html ,css,javascript 
#get('https://www.ipify.org/') response
ip=get('https://api.ipify.org/').text
print(ip)
def ipify():
    var.set(ip)



#############################
#this par for Design
############################
var=StringVar()

ent=Entry(window,state='readonly',font=('arial',16,'italic','bold'),textvariable=var,justify='center')
ent.place(x=36,y=50)
btn=Button(window,text='===GET===',bg='black',fg='red',activebackground='green',font=('arial',16,'italic','bold'),command=ipify)
btn.place(x=85,y=100)

window.mainloop()



   









window.mainloop()
