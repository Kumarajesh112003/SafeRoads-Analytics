# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Traffic accidents by time of occurrence 2001-2014.csv")

X = data.iloc[18,:].values

accident_time = {1:X[3],2:X[4],3:X[5],4:X[6],5:X[7],6:X[8],7:X[9],8:X[10]}
label = ['0-3Hrs','3-6Hrs','6-9Hrs','9-12Hrs','12-15Hrs','15-18Hrs','18-21Hrs','21-24Hrs']

plt.figure(figsize=(10,5))
plt.bar(list(accident_time.keys()), accident_time.values())
plt.xticks([1,2,3,4,5,6,7,8], label)
plt.xlabel('Time (3-hour period)')
plt.ylabel('Total deaths')
plt.title("India: Accidents by Time of Day")
plt.show()
