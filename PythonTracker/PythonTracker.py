import tkinter as tk
import matplotlib.pyplot as plt
import requests

root = tk.Tk()
root.geometry("1000x600")
root.title('Pollution Tracker Project')
root.configure(bg='#FFFFFF')
name_var = tk.StringVar()

canvas = tk.Canvas(
    root,
    bg="#ffffff",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

def submit():
    city = Name_Entry.get() 
    url = 'http://api.waqi.info/feed/' + city + '/?token=' 
    api_key = '37f96394ffe8b6cca1110af3d8270604c711c688' 
    main_url = url + api_key 
    r = requests.get(main_url)
    data = r.json()['data']
    aqi = data['aqi']
    iaqi = data['iaqi'] 

    del iaqi['p']

    temperature = iaqi.get('t', 'Not Available')
    humidity = iaqi.get('h', 'Not Available')
    dew = iaqi.get('dew', 'Not Available')
    no2 = iaqi.get('no2', 'Not Available')
    o3 = iaqi.get('o3', 'Not Available')
    so2 = iaqi.get('so2', 'Not Available')
    pm10 = iaqi.get('pm10', 'Not Available')
    pm25 = iaqi.get('pm25', 'Not Available')

    list1.insert(1, f'{city.upper()} AQI :{aqi} µg/m³')
    list1.insert(2, 'Individual Air quality')
    list1.insert(3, f'Dew :{dew}')
    list1.insert(4, f'NO2 :{no2} µg/m³')
    list1.insert(5, f'Ozone :{o3} µg/m³')
    list1.insert(6, f'Sulphur :{so2} µg/m³')
    degree_sign = u"\N{DEGREE SIGN}"
    list1.insert(7, f'Temperature :{temperature} {degree_sign}C ')
    list1.insert(8, f'Humidity :{humidity} g/kg')
    list1.insert(9, f'pm10 :{pm10}g/m³')
    list1.insert(10, f'pm25 :{pm25}g/m³')

    pollutants = [i for i in iaqi]
    values = [i['v'] for i in iaqi.values()]

    explode = [0 for i in pollutants]
    mx = values.index(max(values))
    explode[mx] = 0.1

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=pollutants, explode=explode, autopct='%1.1f%%', shadow=True)


    level = 0
    plt.title('Air pollutants and their probable amount in atmosphere of {} and the pollution level is {}'.format(city.upper(), level)) 

    plt.axis('equal')
    plt.show() 
    name_var.set("")


background_img = tk.PhotoImage(file=f"background.png")
background = canvas.create_image(465.5, 300.0,image=background_img)

Name_Entryimg = tk.PhotoImage(file=f"img_textBox1.png")
Name_Entrybg = canvas.create_image(749.0, 198.0,image=Name_Entryimg)
Name_Entry = tk.Entry(root,bd=0,bg="#e9e9e9",textvariable=name_var,highlightthickness=0)
Name_Entry.place(x=581.0, y=171, width=336.0, height=52)
	
Listbox_img = tk.PhotoImage(file=f"img_textBox0.png")
ListBox_bg = canvas.create_image(749.0, 432.0,image=Listbox_img)
list1 = tk.Listbox(bd=0,bg="#e9e9e9",highlightthickness=0)
list1.place(x=581.0, y=332,width=336.0,height=198)

btn = tk.PhotoImage(file=f"img0.png")
sub_btn = tk.Button(root,text='Submit', command=submit, image=btn, borderwidth=0, highlightthickness=0, relief="flat")
sub_btn.place(x=674, y=241, width=150, height=47)


root.resizable(False, False)
root.mainloop()


