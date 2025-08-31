# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

dataset = pd.read_csv("Accidents0515.csv")

time = dataset['Time'].dropna().astype(str).str[0:2].astype(int)

x = [math.ceil(i/3) for i in time]

accident_time = {}
for i in x:
    accident_time[i] = accident_time.get(i, 0) + 1

if 0 in accident_time:
    accident_time[1] = accident_time.get(1, 0) + accident_time[0]
    del accident_time[0]

plt.figure(figsize=(10,5))
label = ['12am-3am','3am-6am','6am-9am','9am-12pm','12pm-3pm','3pm-6pm','6pm-9pm','9pm-12am']
plt.bar(list(accident_time.keys()), accident_time.values())
plt.xticks([1,2,3,4,5,6,7,8], label)
plt.xlabel('Time (3-hour period)')
plt.ylabel('Total Accidents')
plt.title("UK: Accidents by Time of Day")
plt.show()

day_of_week = dataset['Day_of_Week'].dropna().astype(int)
day_freq = day_of_week.value_counts().to_dict()

labels = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
sizes = [day_freq.get(i,0) for i in range(1,8)]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("UK: Accidents by Day of Week")
plt.show()
