import tkinter as tk
from downloader import download_func

window=tk.Tk()
window.title("PM2.5 HAQAST GUI")
window.minsize(800, 600)  # Minimum width: 300px, height: 200px
window.maxsize(4000, 3000)  # Maximum width: 800px, height: 600px


header=tk.Label(window, text="Welcome to PM2.5 HAQAST Downloader GUI", font=("Arial", 18)).grid(row=0,column=1)




day_label=tk.Label(window, text='Masukkan hari ')
day_label.grid(row=1,column=0)
day=tk.Entry(window, width=10)
day.grid(row=1,column=2)


month_label=tk.Label(window, text='Masukkan bulan ')
month_label.grid(row=2, column=0)
month=tk.Entry(window, width=10)
month.grid(row=2,column=2)


year_label=tk.Label(window, text='Masukkan tahun ')
year_label.grid(row=3,column=0)
year=tk.Entry(window, width=10)
year.grid(row=3,column=2)

# download button
download=tk.Button(window, text= "Download", command=lambda: download_func(int(day.get()), int(month.get()) , int(year.get())))
download.grid(row=4, column=1)






window.mainloop()