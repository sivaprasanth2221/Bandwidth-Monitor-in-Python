import time
import psutil

last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:
    byte_received = psutil.net_io_counters().bytes_recv
    byte_sent = psutil.net_io_counters().bytes_sent
    byte_total = byte_received + byte_sent
    
    new_received = byte_received - last_received
    new_sent = byte_sent - last_sent
    new_total = byte_total - last_total
    
    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024
    
    print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")
    
    
    last_received = byte_received
    last_sent = byte_sent
    last_total = byte_total
    
    
    time.sleep(1)
    