from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import * 
import	requests
import pytz
from PIL import Image, ImageTk


def ventanaPronostico():
    root=Tk()
    root.title("Servicio Meteorológico")
    root.geometry("890x470+300+200")
    root.config(bg="#57adff")
    root.resizable(0,0)

    ## Icono
    image_icon=PhotoImage(file="Images/logo.png")
    root.iconphoto(False, image_icon)

    homeImg = Image.open("Images/home-clima.jpg")
    homeImg = homeImg.resize((900, 320))
    homeImg = ImageTk.PhotoImage(homeImg)
    labelImgHome = Label(root,image=homeImg)
    labelImgHome.place(x=0, y=0)

    # Boton Volver
    boton_volver = Button(labelImgHome, text = "VOLVER", bg='white' ,fg = "#203243") 
    boton_volver.place(x = 820, y = 20)

    def getWeather():
        ## Toma la entrada (nombre de la ciudad) del usuario y la convierte en longitud y latitud 
        city=textField.get()

        geolocator= Nominatim(user_agent="geoapi-forecast")
        location= geolocator.geocode(city)
        lat=location.latitude
        long=location.longitude

        ## Busca zona horaria con la latitud y long
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=long, lat=lat)
        # timezone.config(text=result)
        # long_lat.config(text=f'{round(lat,4)}°N {round(long,4)}°E')
        home=pytz.timezone(result)
        
        ##Convertirá la zonahoraria en hora.
        local_time=datetime.now(home)
        current_time=local_time.strftime('%H:%M hs')
        clock.config(text=current_time)

        ##Api Clima
        api_key = "646824f2b7b86caffec1d0b16ea77F79"
        api = f'https://api.openweathermap.org/data/2.5/onecall?lat={str(lat)}&lon={str(long)}&units=metric&exclude=hourly&appid={api_key}'
        data = requests.get(api).json()
        
        ##Clima actual
        temp = data["current"]["temp"]
        humidity = data["current"]["humidity"]
        pressure = data["current"]["pressure"]
        wind = data["current"]["wind_speed"]
        description = data["current"]["weather"][0]["description"]

        t.config(text=(f'{temp}°C'))
        h.config(text=(f'{humidity}%'))
        p.config(text=(f'{pressure}hPa'))
        w.config(text=(f'{round((wind * 3.6),2)}km/h'))
        d.config(text=(f'{description}'))


        ## Pronostico extendido

        ## Se traen los nombres de los dias con el modulo de fecha y hora 
        first= datetime.now()
        day1.config(text=first.strftime("%A") )
        day2.config(text=(first+timedelta(days=1)).strftime("%A") )
        day3.config(text=(first+timedelta(days=2)).strftime("%A") )
        day4.config(text=(first+timedelta(days=3)).strftime("%A") )
        day5.config(text=(first+timedelta(days=4)).strftime("%A") )
        day6.config(text=(first+timedelta(days=5)).strftime("%A") )
        day7.config(text=(first+timedelta(days=6)).strftime("%A") )
        
        ##Carga de imagenes en el pronostico extendido
        ##
        imgDay1= data["daily"][0]["weather"][0]["icon"]
        photo1 = ImageTk.PhotoImage(file=f'icon/{imgDay1}@2x.png')
        firstImg.config(image=photo1)
        firstImg.image=photo1  ## Sin esto el G. C. la elimina ## 
        ##
        imgDay2= data["daily"][1]["weather"][0]["icon"]
        img=(Image.open(f'icon/{imgDay2}@2x.png')).resize((50,50))
        photo2 = ImageTk.PhotoImage(img)
        secondImg.config(image=photo2)
        secondImg.image=photo2
        ##
        imgDay3= data["daily"][2]["weather"][0]["icon"]
        img=(Image.open(f'icon/{imgDay3}@2x.png')).resize((50,50))
        photo3 = ImageTk.PhotoImage(img)
        thirdImg.config(image=photo3)
        thirdImg.image=photo3 
        ##
        imgDay4= data["daily"][3]["weather"][0]["icon"]
        img=(Image.open(f'icon/{imgDay4}@2x.png')).resize((50,50))
        photo4 = ImageTk.PhotoImage(img)
        fourthImg.config(image=photo4)
        fourthImg.image=photo4
        ##
        imgDay5= data["daily"][4]["weather"][0]["icon"]
        img=(Image.open(f'icon/{imgDay5}@2x.png')).resize((50,50))
        photo5 = ImageTk.PhotoImage(img)
        fifthImg.config(image=photo5)
        fifthImg.image=photo5
        ##
        imgDay6= data["daily"][5]["weather"][0]["icon"]
        img=(Image.open(f'icon/{imgDay6}@2x.png')).resize((50,50))
        photo6 = ImageTk.PhotoImage(img)
        sixthImg.config(image=photo6)
        sixthImg.image=photo6
        ##
        imgDay7= data["daily"][6]["weather"][0]["icon"]
        img=(Image.open(f'icon/{imgDay7}@2x.png')).resize((50,50))
        photo7 = ImageTk.PhotoImage(img)
        seventhImg.config(image=photo7)
        seventhImg.image=photo7

        ## Temperatura minima y maxima
        min1 = data["daily"][0]["temp"]["min"]
        max1 = data["daily"][0]["temp"]["max"]
        day1Temp.config(text=f'Maxima:{max1}\nMinima:{min1}')

        min2 = data["daily"][0]["temp"]["min"]
        max2 = data["daily"][0]["temp"]["max"]
        day2Temp.config(text=f'Max:{max2}\nMin:{min2}')

        min3 = data["daily"][0]["temp"]["min"]
        max3 = data["daily"][0]["temp"]["max"]
        day3Temp.config(text=f'Max:{max3}\nMin:{min3}')

        min4 = data["daily"][0]["temp"]["min"]
        max4 = data["daily"][0]["temp"]["max"]
        day4Temp.config(text=f'Max:{max4}\nMin:{min4}')

        min5 = data["daily"][0]["temp"]["min"]
        max5 = data["daily"][0]["temp"]["max"]
        day5Temp.config(text=f'Max:{max5}\nMin:{min5}')

        min6 = data["daily"][0]["temp"]["min"]
        max6 = data["daily"][0]["temp"]["max"]
        day6Temp.config(text=f'Max:{max6}\nMin:{min6}')

        min7 = data["daily"][0]["temp"]["min"]
        max7 = data["daily"][0]["temp"]["max"]
        day7Temp.config(text=f'Max:{max7}\nMin:{min7}')

    ## Box de datos de temperatura actuales
    Round_box=PhotoImage(file="Images/roundedBox1.png")
    actualLabel=Label(root, image=Round_box).place(x=30, y=110)

    ## Labels
    label1=Label(root, text="Temperatura", font=("Helvetica",11), fg="white", bg="#203243")
    label1.place(x=40, y=120)

    label2=Label(root, text="Humedad", font=("Helvetica",11), fg="white", bg="#203243")
    label2.place(x=40, y=140)

    label3=Label(root, text="Presión", font=("Helvetica",11), fg="white", bg="#203243")
    label3.place(x=40, y=160)

    label4=Label(root, text="Viento", font=("Helvetica",11), fg="white", bg="#203243")
    label4.place(x=40, y=180)

    label5=Label(root, text="Descripcion", font=("Helvetica",11), fg="white", bg="#203243")
    label5.place(x=40, y=200)

    ##Caja de búsqueda
    search_img=PhotoImage(file="Images/Rounded Rectangle 3.png")
    myimage=Label(root, image=search_img)
    myimage.place(x=270, y=120)

    weat_img=PhotoImage(file="Images/Layer 7.png")
    weatherImg=Label(root, image=weat_img, bg="#203243")
    weatherImg.place(x=290, y=127)

    textField=Entry(root, justify="center", width=15, font=("poppins",25,"bold"), bg="#203243", border=0, fg="white")
    textField.place(x=370, y=130)
    textField.focus()

    search_icon=PhotoImage(file="Images/Layer 6.png")
    myimage_icon=Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather, activebackground="#203243")
    myimage_icon.place(x=645, y=125)

    ## Frame para la temperatura extendida

    frame=Frame(root, width=900, height=160, bg="#212120")
    frame.pack(side=BOTTOM)

    ## Cajas de temp extendida
    box1=PhotoImage(file="Images/Rounded Rectangle 2.png")
    box2=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

    Label(frame,image=box1, bg="#212120").place(x=30, y=10)
    Label(frame,image=box2, bg="#212120").place(x=300, y=20)
    Label(frame,image=box2, bg="#212120").place(x=400, y=20)
    Label(frame,image=box2, bg="#212120").place(x=500, y=20)
    Label(frame,image=box2, bg="#212120").place(x=600, y=20)
    Label(frame,image=box2, bg="#212120").place(x=700, y=20)
    Label(frame,image=box2, bg="#212120").place(x=800, y=20)

    ## Hora 
    clock=Label(root, text="00:00", font=("Helvetica", 30, "bold"), fg="white", bg="#203243")
    clock.place(x=30, y=20)

    '''
    ## zona horaria
    timezone=Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
    timezone.place(x=600, y=20)

    ## latitud y longitud
    long_lat=Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
    long_lat.place(x=700, y=50)
    '''


    ## Valores actuales
    t=Label(root, font=("Helvetica",10), fg="white", bg="#203243")
    t.place(x=135, y=120)
    h=Label(root, font=("Helvetica",10), fg="white", bg="#203243")
    h.place(x=135, y=140)
    p=Label(root, font=("Helvetica",10), fg="white", bg="#203243")
    p.place(x=135, y=160)
    w=Label(root, font=("Helvetica",10), fg="white", bg="#203243")
    w.place(x=135, y=180)
    d=Label(root, font=("Helvetica",10), fg="white", bg="#203243")
    d.place(x=135, y=200)


    ## Datos extendido

    ## Primer día 
    firstFrame=Frame(root, width=230, height=132, bg="#282829")
    firstFrame.place(x=35, y=325)

    day1=Label(firstFrame, font="arial 20", bg="#282829", fg="#fff")
    day1.place(x=75, y=5)

    firstImg=Label(firstFrame, bg="#282829", fg="#fff")
    firstImg.place(x=1,y=35)

    day1Temp = Label(firstFrame, bg="#282829", fg="#57adff", font="arial 12 bold")
    day1Temp.place(x=100, y=50)
    ## Segundo día
    secondFrame=Frame(root, width=70, height=115, bg="#282829")
    secondFrame.place(x=305, y=335)

    day2=Label(secondFrame, bg="#282829", fg="#fff")
    day2.place(x=10, y=5)

    secondImg=Label(secondFrame, bg="#282829", fg="#fff")
    secondImg.place(x=10,y=25)

    day2Temp=Label(secondFrame, bg="#282829", fg="#57adff")
    day2Temp.place(x=10, y=70)
    ## Tercer día

    thirdFrame=Frame(root, width=70, height=115, bg="#282829")
    thirdFrame.place(x=405, y=335)

    day3=Label(thirdFrame, bg="#282829", fg="#fff")
    day3.place(x=10, y=5)

    thirdImg=Label(thirdFrame, bg="#282829", fg="#fff")
    thirdImg.place(x=10,y=25)

    day3Temp = Label(thirdFrame, bg="#282829", fg="#57adff")
    day3Temp.place(x=10, y=70)
    ##Cuarto día
    fourthFrame=Frame(root, width=70, height=115, bg="#282829")
    fourthFrame.place(x=505, y=335)

    day4=Label(fourthFrame, bg="#282829", fg="#fff")
    day4.place(x=10, y=5)

    fourthImg=Label(fourthFrame, bg="#282829", fg="#fff")
    fourthImg.place(x=10,y=25)

    day4Temp = Label(fourthFrame, bg="#282829", fg="#57adff")
    day4Temp.place(x=10, y=70)
    ##Quinto día
    fifthFrame=Frame(root, width=70, height=115, bg="#282829")
    fifthFrame.place(x=605, y=335)

    day5=Label(fifthFrame, bg="#282829", fg="#fff")
    day5.place(x=10, y=5)

    fifthImg=Label(fifthFrame, bg="#282829", fg="#fff")
    fifthImg.place(x=10,y=25)

    day5Temp = Label(fifthFrame, bg="#282829", fg="#57adff")
    day5Temp.place(x=10, y=70)
    ##Sexto día
    sixthFrame=Frame(root, width=70, height=115, bg="#282829")
    sixthFrame.place(x=705, y=335)

    day6=Label(sixthFrame, bg="#282829", fg="#fff")
    day6.place(x=10, y=5)

    sixthImg=Label(sixthFrame, bg="#282829", fg="#fff")
    sixthImg.place(x=10,y=25)

    day6Temp = Label(sixthFrame, bg="#282829", fg="#57adff")
    day6Temp.place(x=10, y=70)
    ##Septimo día
    seventhFrame=Frame(root, width=70, height=115, bg="#282829")
    seventhFrame.place(x=805, y=335)

    day7=Label(seventhFrame, bg="#282829", fg="#fff")
    day7.place(x=10, y=5)

    seventhImg=Label(seventhFrame, bg="#282829", fg="#fff")
    seventhImg.place(x=10,y=25)

    day7Temp = Label(seventhFrame, bg="#282829", fg="#57adff")
    day7Temp.place(x=10, y=70)

    root.mainloop()