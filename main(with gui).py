from tkinter import*
import random
import os
import requests
# import weather_variant6

global useri
my_apikey="b601c6a0a6fbd1707581c325e123b285"

def getjson(place):
    link=f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={my_apikey}&units=metric"
    request_api=requests.get(link)
    weatherdatajson=request_api.json()
    return weatherdatajson

def temperature(place):
        temperaturejson=getjson(place)
        txt.insert(END,"\n"+"Bot->"+f"temperature at {place} is "+f"{temperaturejson['main']['temp']}")
        # print(f"\ntemperature at {place} is ",temperaturejson['main']['temp'])
def justinput():
    pass
def weather(place):
    weatherjson=getjson(place)
    txt.insert(END,"\n"+"Bot->\n"+f"\ttemperature at {place} is "+f"{weatherjson['main']['temp']}")
    txt.insert(END,"\n"+f"\thumidity at {place} is "+f"{weatherjson['main']['humidity']}")
    txt.insert(END,"\n"+f"\tMax temperature at {place} is "+f"{weatherjson['main']['temp_max']}")
    txt.insert(END,"\n"+f"\tWindspeed at {place} is "+f"{weatherjson['wind']['speed']}")
    txt.insert(END,"\n"+f"\t{weatherjson['weather'][0]['description']}")

    # print(f"\nTemperature at {place} is ",weatherjson['main']['temp'])
    # print(f"Humidity at {place} is ",weatherjson['main']['humidity'])
    # print(f"Max temperature at {place} is ",weatherjson['main']['temp_max'])
    # print(f"Windspeed at {place} is ",weatherjson['wind']['speed'])
    # print(weatherjson['weather'][0]['description'],"\n")
def pressure(place):
        pressurejson=getjson(place)
        print(f"\nPressure at {place} is ",pressurejson['main']['pressure'],"\n")

def humidity(place):
        humidityjson=getjson(place)
        print(f"humidity at {place} is ",humidityjson['main']['humidity'],"\n")

def visibility(place):
        visibilityjson=getjson(place)
        print(f"visibility at {place} is ",visibilityjson['visibility'],"\n")

def windspeed(place):
        windspeedjson=getjson(place)
        print(f"windspeed at {place} is ",windspeedjson['wind']['speed'],"\n")

def sunrise(place):
        sunrisejson=getjson(place)
        print(f"sunrise at {place} is ",sunrisejson['sys']['sunrise'],"\n")

def sunset(place):
        sunsetjson=getjson(place)
        print(f"sunset at {place} is ",sunsetjson['sys']['sunset'],"\n")
    
greet=['hi','hello','ola','hello you','hello there','hey bot','hey','good morning','good afternoon','good evening','hiiii']
bot_greet=['hi there','Hello','hey!','Nice to see you ']
randomgreet=random.randint(0,len(bot_greet)-1)
# print(randomgreet)
goodbye=['bye','goodbye','bye bot','goodbye!','see you next time','see you again','thankyou']
bot_goodbye=['Bye!Hope to see you again','Goodbye','see you next time','Thank you! Hope I helped you']
randomgoodbye=random.randint(0,len(bot_goodbye)-1)
temp=['what is the temperature','tell me the weather','hows the weather','whats the max temperature?','temperature near me']
weat=['what is the weather','what is weather','weather']
pres=['what is the pressure','what is pressure','pressure']
humi=['what is the humidity','what is humidity','humidity']
visibi=['what is the visibilty','what is visibility','visibility']
windspeed=['what is the windspeed','what is windspeed','windspeed']
sunri=['sunrise']
sunse=['sunset']
temp_1=['what is the temperature in','what is the temperature at']
weat_1=['what is weather in','what is the weather at','how is the climate in','how is the weather in','what is the weather in']

root=Tk()
# root.configure(background='black')

def send():
    userinput=e.get()
    print(userinput)
    txt.insert(END,"\n"+"User->"+userinput)
    loweruserinput=userinput.lower()
    wordslist=[]
    wordslist=userinput.split(" ")
    if('in' in wordslist):
        a=""
        j=0
        while(j!=(len(wordslist)-1)):
            if(wordslist[j]=='in'):
                break
            a=a+wordslist[j]+" "
            j=j+1
        a=a+"in"
    elif('at' in wordslist):
        a=""
        j=0
        while(j!=(len(wordslist)-1)):
            if(wordslist[j]=='at'):
                break
            a=a+wordslist[j]+" "
            j=j+1
        a=a+"at"
    if(loweruserinput in greet):
        # print(bot_greet[randomgreet])
        txt.insert(END,"\n"+"Bot->"+bot_greet[randomgreet])

    elif(loweruserinput in goodbye):
        # print(bot_goodbye[randomgoodbye])
        txt.insert(END,"\n"+"Bot->"+bot_goodbye[randomgoodbye])
        e.delete(0,END)
        root.quit()
    
    elif(loweruserinput in temp):
        txt.insert(END,"\n"+"Bot->"+"Which place?")
        e.delete(0,END)
        # sendi=Button(root,text="Send",command=send).grid(row=1,column=1)
        justinput()
    elif(loweruserinput in pres):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        pressure(useri)
    elif(loweruserinput in humi):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        humidity(useri)
    elif(loweruserinput in visibi):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        visibility(useri)
    elif(loweruserinput in windspeed):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        windspeed(useri)
    elif(loweruserinput in sunri):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        sunrise(useri)
    elif(loweruserinput in sunse):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        sunset(useri)
    elif(loweruserinput in weat):
        print("\nWhich place?\n")
        print("\t\t\t",end=" ")
        useri=input("")
        weather(useri)
    elif(a in temp_1):
        temperature(wordslist[-1])
        # temperature(place)
    elif(a in weat_1):
        weather(wordslist[-1])
    else:
        print("I don't understand what you are saying")
    
    # if(e.get()=="hi"):
    #     txt.insert(END,"\n"+"BOT->Hi how may I help you?")
    e.delete(0,END)    
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2) 
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Weather Chatbot")
root.mainloop()
