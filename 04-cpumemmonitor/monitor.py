import time
import psutil

#print(psutil.cpu_percent())
#print(psutil.virtual_memory().percent)

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percentage=(cpu_usage/100.0)
    cpu_bar='*'*int(cpu_percentage*bars)+'-'*int(bars-int(cpu_percentage*bars))
    mem_percentage=(mem_usage/100.0)
    mem_bar='*'*int(mem_percentage*bars)+'-'*int(bars-int(mem_percentage*bars))

    #print(f"cpu: {cpu_percentage}", end="\n")
    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%", end=" ")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end="\r")


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 40)
    time.sleep(1)
