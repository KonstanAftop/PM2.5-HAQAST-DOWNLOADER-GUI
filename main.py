import tkinter as tk
from downloader import download_func
from conversion import lat_converter_to_idx, lon_converter_to_idx
from tkinter import ttk
import threading

window = tk.Tk()
window.title("M2H-PM25 Downloader")
window.geometry("450x350")  # Increased height for better layout
window.resizable(False, False)

# Configure grid to center elements
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Header
header = tk.Label(window, text="M2H-PM25 Downloader", font=("TkDefaultFont", 14, "bold"))
header.grid(row=0, column=0, columnspan=3, pady=10)

# Progress Bar Variable
progress_var = tk.DoubleVar()

def download():
    start = startdate.get()
    end = enddate.get()
    lon_0 = lon_converter_to_idx(int(lon_init.get()))
    lon_1 = lon_converter_to_idx(int(lon_end.get()))
    lat_0 = lat_converter_to_idx(int(lat_init.get()))
    lat_1 = lat_converter_to_idx(int(lat_end.get()))
    
    def threaded_download():
        total_files = (int(end) - int(start)) + 1  # Number of files expected
        progress_var.set(0)  # Reset progress

        def update_progress(completed):
            progress_var.set((completed / total_files) * 100)
            window.update_idletasks()

        download_func(start, lon_0, lon_1, lat_0, lat_1, end, update_progress)
        status_label.config(text="COMPLETE!", fg="green")

    threading.Thread(target=threaded_download, daemon=True).start()  # Run in a separate thread

# Start Date
startdate_label = tk.Label(window, text="Waktu awal (YYYYMMDD):")
startdate_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
startdate = tk.Entry(window, width=12)
startdate.grid(row=1, column=1, padx=5, pady=5)

# End Date
enddate_label = tk.Label(window, text="Waktu akhir (YYYYMMDD):")
enddate_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
enddate = tk.Entry(window, width=12)
enddate.grid(row=2, column=1, padx=5, pady=5)

# Longitude Inputs
lon_label = tk.Label(window, text="Longitude (Min / Max):")
lon_label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
lon_init = tk.Entry(window, width=6)
lon_init.grid(row=3, column=1, padx=2, pady=5, sticky="e")
lon_end = tk.Entry(window, width=6)
lon_end.grid(row=3, column=2, padx=2, pady=5, sticky="w")

# Latitude Inputs
lat_label = tk.Label(window, text="Latitude (Min / Max):")
lat_label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
lat_init = tk.Entry(window, width=6)
lat_init.grid(row=4, column=1, padx=2, pady=5, sticky="e")
lat_end = tk.Entry(window, width=6)
lat_end.grid(row=4, column=2, padx=2, pady=5, sticky="w")

# Progress Bar
progress = ttk.Progressbar(window, variable=progress_var, maximum=100, length=300)
progress.grid(row=5, column=0, columnspan=3, pady=5)

# Status Label
status_label = tk.Label(window, text="", font=("TkDefaultFont", 10, "bold"))
status_label.grid(row=7, column=0, columnspan=3, pady=5)

# Download Button
download_btn = tk.Button(window, text="Download", command=download, width=12, bg="lightblue")
download_btn.grid(row=6, column=0, columnspan=3)

# Feedback
feedback_label=tk.Label(window, text='contact : konstanaftopds@gmail.com' )
feedback_label.grid(row=8, column=0, columnspan=3)

# credit
credit_label=tk.Label(window, text='Data source : Goddard Earth Sciences Data and Information Services Center' )
credit_label.grid(row=9, column=0, columnspan=3)


window.mainloop()
