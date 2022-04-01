import math
import speedtest
def bytesToMb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"

wifi = speedtest.Speedtest()

print("Testing connection...")
download_speed = wifi.download()
upload_speed = wifi.upload()

print ("Download speed:", bytesToMb(download_speed))
print("Upload speed:", bytesToMb(upload_speed))