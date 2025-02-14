import requests

def download_func(d, m, y):
    # Format tanggal
    date_str = f"{y}{m:02d}{d:02d}"  # Pastikan bulan dan hari memiliki dua digit

    # Url data yang akan didownload 
    url = f"https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/MERRA2_CNN_HAQAST_PM25.1/{y}/MERRA2_HAQAST_CNN_L4_V1.{date_str}.nc4.dap.nc?dap4.ce=/lat[135:1:150];/lon[180:1:275];/time[0:1:23];/MERRA2_CNN_Surface_PM25[0:1:23][135:1:150][180:1:275]"

    # Nama file keluaran
    filename = f"MERRA2_PM25_{date_str}.nc"

    # NASA Earthdata Authentication Token
    access_token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6InJpZGhhZmF0b255MDAiLCJleHAiOjE3NDAzMTc1NjcsImlhdCI6MTczNTEzMzU2NywiaXNzIjoiaHR0cHM6Ly91cnMuZWFydGhkYXRhLm5hc2EuZ292IiwiaWRlbnRpdHlfcHJvdmlkZXIiOiJlZGxfb3BzIiwiYWNyIjoiZWRsIiwiYXNzdXJhbmNlX2xldmVsIjozfQ.hZGSE1jf9gNSRMQf2MoR8Y4WvAmLhrxUzWqaBivcGddmfVZ0A0hL94qfV--60Cd45T6f5QxWwvM3XzSpTRhvMxBXez4KBzZhSqk9pUKGJBsqtffYF26NY_JumPVNxJO6_KZ133zekJlFjHXP_yIE6k8oR_4NJ5ZfuOhnzk5MNCXuLu4MbvpTVlmyyW9NXgtWIAP-N7RO9fKH9h17sREER5LEIsC8nDb8oFBg8Y1i7sv6tn-svMBYjP0uoi4W5wgpDuA-J4_xqDC_SNDAnoHnPDTu0Jnm1rEoHodARpo7RqOpShvfF4exm17wSVVmC3iXF5jZKEIVdZQ6puPM8KvOGw"  # Replace with a valid token

    headers = {'Authorization': f'Bearer {access_token}'}

    # Kirim request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded: {filename}')
        except IOError as e:
            print(f'Error saving {filename}: {e}')
    else:
        print(f'Failed to download {filename}: Status code {response.status_code}')
