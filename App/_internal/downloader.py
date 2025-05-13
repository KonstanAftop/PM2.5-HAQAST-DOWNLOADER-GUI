import requests
import pandas as pd
from datetime import datetime
import os

def download_func(start_date, lon0, lon1, lat0, lat1, end_date, progress_callback):
    start_date = datetime.strptime(start_date, "%Y%m%d")
    end_date = datetime.strptime(end_date, "%Y%m%d")

    base_url = "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/MERRA2_CNN_HAQAST_PM25.1/{y}/MERRA2_HAQAST_CNN_L4_V1.{date_str}.nc4.dap.nc?dap4.ce=/lat[{lat0}:1:{lat1}];/lon[{lon0}:1:{lon1}];/time[0:1:23];/MERRA2_CNN_Surface_PM25[0:1:23][{lat0}:1:{lat1}][{lon0}:1:{lon1}]"

    urls = []
    date_range = pd.date_range(start=start_date, end=end_date)
    
    for date in date_range:
        y, m, d = date.year, date.month, date.day
        date_str = f"{y}{m:02d}{d:02d}"
        url = base_url.format(y=y, date_str=date_str, lon0=lon0, lon1=lon1, lat0=lat0, lat1=lat1)
        urls.append((url, date_str)) 

    access_token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6IjEyODIyMDU4aXRiIiwiZXhwIjoxNzUyMDQ0NjU3LCJpYXQiOjE3NDY4NjA2NTcsImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiIsImlkZW50aXR5X3Byb3ZpZGVyIjoiZWRsX29wcyIsImFjciI6ImVkbCIsImFzc3VyYW5jZV9sZXZlbCI6M30.I2IKWzlojkcAenbqvsLU5oFOgAsINz1r5LaVZyosJjGSfz2uIqeKEGi7fea3NDkVyCoPux6dAbEuBDuyF-wYrjqNBlHIvwb3tyJEo1ykCIPv475DMBy-vedGowo-Kw4dX_gd-Qc6oe2Th9HCDSqO5QnJ0jnuU7DTdpK93ZtIcJAuaK-H8dSRynSOxz3JMl7oZajZ03Xq5A6tTziaf6leWXfyjgg_nE7Em_x69ERpeWaZVdyNl0_LoIs_ecJqmjRPHUJvAzyV62Y31yVv0APMSIPRJE-dXdSIwlcQk3vHO-HNgL7-O-bb8lK6OU2CiBvhmD2hK0q50j9OEHcFIP4DNQ"  # Replace with a valid token
    headers = {'Authorization': f'Bearer {access_token}'}

    save_dir = "downloads"  # Default directory
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # Create folder if not exist

    total_files = len(urls)
    completed_files = 0  # Track downloaded files

    for url, date_str in urls:
        filename = f"MERRA2_HAQAST_CNN_L4_V1.{date_str}.nc"
        file_path = os.path.join(save_dir, filename)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            try:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded: {filename}")
                completed_files += 1
                progress_callback(completed_files)  # Update progress bar
            except IOError as e:
                print(f"Error saving {filename}: {e}")
        else:
            print(f"Failed to download {filename}: Status code {response.status_code}")
            print("Server response:", response.text)
