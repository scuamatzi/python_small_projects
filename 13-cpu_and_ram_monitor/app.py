import tkinter as tk, psutil

root = tk.Tk()
root.title("CPU & RAM Monitor")
root.geometry("500x300")
root.configure(bg="black")

lbl = tk.Label(root, font=("Arial", 20, "bold"), bg="black", fg="lime")
lbl.pack(expand=True)


def update():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    lbl.config(text=f"CPU Usage: {cpu}%\n RAM Usage: {ram}% ")
    root.after(1000, update)


update()

root.mainloop()
