import tkinter as tk
import requests

HEIGHT =500
WIDTH =600

def test_function(entry):
    print("This is the entry: ", entry)

#cfe3b6ec5054916590a018157fe473ff
#http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
    


def get_weather(city):
        weather_key = 'cfe3b6ec5054916590a018157fe473ff'
        url='http://api.openweathermap.org/data/2.5/forecast'
        params={'APPID': weather_key, 'q': city, 'units': 'metric'}
        response = requests.get(url, params=params)
        print(response.json())





root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()






frame = tk.Frame(root, bg='#D2AF34', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)



button = tk.Button(frame, text="Get Weather", font='20', bg="gray", fg="blue", command=lambda:get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#2167a1", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()