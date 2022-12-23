from datetime import datetime
from playsound import playsound
from tkinter import *

root = Tk()
 
root.geometry("400x250")


def alarm():
    # time = input('Enter the time in format (HH:MM:SS AM/PM): ')
    time = f'{hour.get()}:{minute.get()}:{second.get()} {period.get()}'
    if len(time) != 11:
        vali = 'Incorrect format'
    elif int(time[:2]) > 12 and int(time[:2])<0:
        vali = 'Incorrect format'
    elif int(time[3:5]) >= 60 and int(time[3:5]) < 0:
        vali = 'Incorrect format'
    elif int(time[6:8]) >= 60 and int(time[6:8]) < 0:
        vali = 'Incorrect format'
    elif time[9:11].lower() != 'am' and time[9:11].lower() != 'pm':
        vali = 'Incorrect format'
    else:
        vali = 'ok'
    
    w = Label(root, text=vali,font=("Helvetica 10 bold"),fg="red")

    if vali != 'ok':
        # print(vali)
        # print(time)
        w.pack()
    else:
        print(f'Alarm set for {time}')
        Label(root, text=f'Alarm set for {time}',font=("Helvetica 10 bold"),fg="red").pack()
        while True:
            # print('sleep')
            now = datetime.now()
            if int(time[:2]) == int(now.strftime('%I')) and int(time[3:5]) == int(now.strftime('%M')) and int(time[6:8]) == int(now.strftime('%S')) and time[9:11].upper() == now.strftime('%p'):
                # print('Wake Up!')
                Label(root, text=f'Wake Up!',font=("Helvetica 10 bold"),fg="red").pack()
                playsound('alarm_classic.mp3')
                break


Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
 
frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12')
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

period = StringVar(root)
periods = ('AM', 'PM')
period.set(periods[0])
per = OptionMenu(frame, period, *periods)
per.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=alarm).pack(pady=20)
root.mainloop()