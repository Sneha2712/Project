from tkinter import *
import requests 
import os
from datetime import datetime


def getcity():

    print("YOU CLICKED BUTTON")
    global city 
    city = entry.get()

    user_api = '68880300df28252dd2e8adadb6a25df8'
    location = city
 
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location+"&appid="+user_api
 
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod']=='404':
        print("Invalid city")
    else:
        temp_city = ((api_data['main']['temp']) - 273.15) #temp in kelvin - 273.15gives temp in degree
        weather_desc = api_data['weather'][0]['description'] #weather in that 0(first) element in that weather. in doc  
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")#string format for date and time 
    l2 =Label(window,
                font=('Arial',15),
                text=weather_desc)
    l2.place(x=180,y=200)

    l3 =Label(window,
                font=('Arial',15),
                text=temp_city)
    l3.place(x=180,y=230)

    l4 =Label(window,
                font=('Arial',15),
                text=hmdt)
    l4.place(x=180,y=260)

    l5 =Label(window,
                font=('Arial',15),
                text=date_time)
    l5.place(x=180, y=290)

    l6 =Label(window,
                font=('Arial',20),
                text=wind_spd)
    l6.place(x=180,y=320)



window = Tk() 
window.geometry("500x500")
window.title("Project 3")

window.config(background='pink')

label = Label(window,text= "Weather app ",
                    font=('Arial',40),
                     fg='black',
                     bg='pink',
                     padx=20,
                     pady=20,
                    ) 
label.pack()

entry = Entry(window,
            font =('Arial',20),
)
entry.pack()



button = Button(window,
                text= "ENTER",
                command = getcity,
                fg='green',#make fg and activefg same to not to flash button
                bg = 'black',
                #activeforeground='blue',
                #activebackground='yellow',
                state=ACTIVE)
button.pack()

window.mainloop()