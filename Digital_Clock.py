import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)
root.configure(bg="black")

# Label to show time
label = tk.Label(root, font=("Helvetica", 40), background="black", foreground="green")
label.pack(anchor="center", pady=20)

def update_time():
    time_string = strftime("%I:%M:%S %p")  # e.g., 07:45:23 PM
    label.config(text=time_string)
    label.after(1000, update_time)  # call update_time() every 1 second

# Start the clock
update_time()

# Run the app
root.mainloop()
