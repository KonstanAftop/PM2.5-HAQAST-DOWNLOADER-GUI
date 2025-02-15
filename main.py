import tkinter as tk
from downloader import download_func
from conversion import lat_converter_to_idx, lon_converter_to_idx


window=tk.Tk()
window.title("PM2.5 HAQAST GUI")
window.minsize(400, 300)  # Minimum width: 300px, height: 200px
window.maxsize(800, 600)  # Maximum width: 800px, height: 600px


header=tk.Label(window, text="MERRA-2 PM2.5 HAQAST DATA DOWNLOADER", font=("Arial", 18))
header.grid(row=0, column=1)

def download():
    start=str(startdate.get())
    end=str(enddate.get())
    lon_0, lon_1, lat_0, lat_1 = lon_converter_to_idx(int(lon_init.get())), lon_converter_to_idx(int(lon_end.get())), lat_converter_to_idx(int(lat_init.get())), lat_converter_to_idx(int(lat_end.get()))
    download_func(start,lon_0,lon_1,lat_0,lat_1,end)


startdate_label=tk.Label(window, text='Masukkan waktu awal (YYYYMMDD)')
startdate_label.grid(row=1,column=0, columnspan=1)
startdate=tk.Entry(window, width=10)
startdate.grid(row=1,column=1)

enddate_label=tk.Label(window, text='Masukkan waktu akhir (YYYYMMDD)')
enddate_label.grid(row=2,column=0)
enddate=tk.Entry(window, width=10)
enddate.grid(row=2,column=1)

lon_label=tk.Label(window, text='Masukkan longitude area (AWAL/AKHIR)')
lon_label.grid(row=3,column=0)
lon_init=tk.Entry(window, width=10)
lon_init.grid(row=3,column=1, columnspan=1)
lon_end=tk.Entry(window, width=10)
lon_end.grid(row=3,column=2, columnspan=1)


lat_label=tk.Label(window, text='Masukkan latitude area (AWAL/AKHIR)')
lat_label.grid(row=4,column=0)
lat_init=tk.Entry(window, width=10)
lat_init.grid(row=4,column=1)
lat_end=tk.Entry(window, width=10)
lat_end.grid(row=4,column=2)

# download button
download=tk.Button(window, text= "Download", command=download)
download.grid(row=5, column=1)





window.mainloop()