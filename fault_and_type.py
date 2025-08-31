# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

FaultType = pd.read_csv("datafile_4.csv")
FaultType = FaultType.drop(FaultType.index[[34,37]])

faulttype = {
    "Driver's Fault": FaultType.loc[36,'Fault of Driver-Total No. of Road Accidents - 2014'],
    "Cyclist's Fault": FaultType.loc[36,'Fault of Cyclist-Total No. of Road Accidents - 2014'],
    "Vehicle Condition": FaultType.loc[36,'Defect in Condition of Motor Vehicle-Total No. of Road Accidents - 2014'],
    "Road Condition": FaultType.loc[36,'Defect in Road Condition-Total No. of Road Accidents - 2014'],
    "Weather Condition": FaultType.loc[36,'Weather Condition-Total No. of Road Accidents - 2014'],
    "Passenger's Fault": FaultType.loc[36,'Fault of Passenger-Total No. of Road Accidents - 2014'],
    "Poor Light": FaultType.loc[36,'Poor light-Total No. of Road Accidents - 2014'],
    "Stray Animals": FaultType.loc[36,'Stray animals-Total No. of Road Accidents - 2014'],
    "Others": FaultType.loc[36,'Other causes/ Causes not known-Total No. of Road Accidents - 2014']
}

plt.figure(figsize=(10,8))
plt.pie(list(faulttype.values()), labels=list(faulttype.keys()), autopct='%1.2f%%')
plt.title("Causes of Road Accidents (2014)")
plt.show()

RoadUserDf = pd.read_csv("datafile_4.csv")

vehicletype = {
    "2-Wheeler": RoadUserDf.loc[36,'Motor Cycle/ Scooter - Number of Road Accidents - Total - 2016'] + 
                 RoadUserDf.loc[36,'Moped/Scootty - Number of Road Accidents - Total - 2016'],
    "3-Wheeler": RoadUserDf.loc[36,'Auto rickshaw - Number of Road Accidents - Total - 2016'] + 
                 RoadUserDf.loc[36,'Tempo - Number of Road Accidents - Total - 2016'] + 
                 RoadUserDf.loc[36,'E-Rickshaw - Number of Road Accidents - Total - 2016'],
    "4-Wheeler": RoadUserDf.loc[36,'Motor Car - Number of Road Accidents - Total - 2016'] + 
                 RoadUserDf.loc[36,'Jeep - Number of Road Accidents - Total - 2016'] + 
                 RoadUserDf.loc[36,'Taxi - Number of Road Accidents - Total - 2016'],
    "Heavy Vehicle": RoadUserDf.loc[36,'Bus - Number of Road Accidents - Total - 2016'] + 
                     RoadUserDf.loc[36,'Truck/Lorry - Number of Road Accidents - Total - 2016'] + 
                     RoadUserDf.loc[36,'Articulated Vehicle/Trolly - Number of Road Accidents - Fatal - 2016'] + 
                     RoadUserDf.loc[36,'Tractor - Number of Road Accidents - Total - 2016'],
    "Other Vehicle": RoadUserDf.loc[36,'Other Motor Vehicles - Number of Road Accidents - Total - 2016']
}

plt.figure(figsize=(10,8))
plt.pie(list(vehicletype.values()), labels=list(vehicletype.keys()), autopct='%1.2f%%')
plt.title("Types of Vehicles Involved in Accidents (2016)")
plt.show()