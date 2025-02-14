import tkinter as tk
from tkinter import messagebox, filedialog
import datetime
import time
import threading
import winsound

alarms = []

def play_alarm(sound_file):
    if sound_file:
        winsound.PlaySound(sound_file, winsound.SND_FILENAME)
    else:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

def check_alarm():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for alarm in alarms:
            if now == alarm["time"]:
                play_alarm(alarm["sound"])
                response = messagebox.askyesno("Alarm", "Time to wake up! Snooze?")
                if response:
                    snooze_time = int(alarm["snooze"])
                    alarms.append({"time": (datetime.datetime.now() + datetime.timedelta(minutes=snooze_time)).strftime("%H:%M"), "sound": alarm["sound"], "snooze": snooze_time})
                alarms.remove(alarm)
        time.sleep(30)

def set_alarm():
    alarm_details = {"time": alarm_time.get(), "sound": alarm_sound.get(), "snooze": snooze_time.get()}
    alarms.append(alarm_details)
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.get()}")

def choose_sound():
    file_path = filedialog.askopenfilename(filetypes=[("WAV Files", "*.wav")])
    if file_path:
        alarm_sound.set(file_path)

# GUI Setup
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("350x200")

tk.Label(root, text="Enter Alarm Time (HH:MM):").pack(pady=5)
alarm_time = tk.StringVar()
tk.Entry(root, textvariable=alarm_time, width=10).pack(pady=5)

tk.Label(root, text="Snooze Time (minutes):").pack(pady=5)
snooze_time = tk.StringVar(value="5")
tk.Entry(root, textvariable=snooze_time, width=10).pack(pady=5)

tk.Label(root, text="Select Alarm Sound:").pack(pady=5)
alarm_sound = tk.StringVar()
tk.Button(root, text="Choose Sound", command=choose_sound).pack(pady=5)

tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=10)

threading.Thread(target=check_alarm, daemon=True).start()

root.mainloop()
