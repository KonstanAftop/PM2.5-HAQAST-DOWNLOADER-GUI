import requests
import pandas as pd
from datetime import datetime

def download_func(start_date, lon0, lon1, lat0, lat1, end_date):
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
        print(url)
        print(date_str)

    access_token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6InJpZGhhZmF0b255MDAiLCJleHAiOjE3NDAzMTc1NjcsImlhdCI6MTczNTEzMzU2NywiaXNzIjoiaHR0cHM6Ly91cnMuZWFydGhkYXRhLm5hc2EuZ292IiwiaWRlbnRpdHlfcHJvdmlkZXIiOiJlZGxfb3BzIiwiYWNyIjoiZWRsIiwiYXNzdXJhbmNlX2xldmVsIjozfQ.hZGSE1jf9gNSRMQf2MoR8Y4WvAmLhrxUzWqaBivcGddmfVZ0A0hL94qfV--60Cd45T6f5QxWwvM3XzSpTRhvMxBXez4KBzZhSqk9pUKGJBsqtffYF26NY_JumPVNxJO6_KZ133zekJlFjHXP_yIE6k8oR_4NJ5ZfuOhnzk5MNCXuLu4MbvpTVlmyyW9NXgtWIAP-N7RO9fKH9h17sREER5LEIsC8nDb8oFBg8Y1i7sv6tn-svMBYjP0uoi4W5wgpDuA-J4_xqDC_SNDAnoHnPDTu0Jnm1rEoHodARpo7RqOpShvfF4exm17wSVVmC3iXF5jZKEIVdZQ6puPM8KvOGw"  # Replace with a valid token

    headers = {'Authorization': f'Bearer {access_token}'}


    for url, date_str in urls:
        filename = f"MERRA2_HAQAST_CNN_L4_V1.{date_str}.nc"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            try:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded: {filename}")
            except IOError as e:
                print(f"Error saving {filename}: {e}")
        else:
            print(f"Failed to download {filename}: Status code {response.status_code}")
            print("Server response:", response.text)


