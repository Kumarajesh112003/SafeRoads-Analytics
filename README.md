# 🚦 Road Accident Data Analysis Project

This project analyzes road accident data from **India and the UK** using **Python** and **R**.  
It explores **accident severity, time of day, fault attribution, and vehicle involvement**.  
The goal is to **visualize accident patterns** and build a simple **decision tree model** for accident severity prediction.  

---

## 📂 Project Structure

RoadSafetyProject/

│── Accidents0515.csv  

│── Data_Final.csv  

│── datafile_4.csv  

│── Traffic accidents by time of occurrence 2001-2014.csv  


│── severity.py  

│── timeofdayUK.py  

│── time_of_day_india.py  

│── fault_and_type.py  

│── random_forest_accidents.py  

│── decision_tree_accidents.r  


│── Snapshots/  

│   │── dayoftheweek_alcohol.png  

│   │── faults.png  

│   │── type.png  

│   │── asi.png  

│   │── severity_plot.png  

│   │── timeofday_plot.png  

│   │── fault_donut.png  

│   │── decision_tree_accidents.png  


│── README.md  

│── requirements.txt  

---

## 🔧 Requirements

### 🐍 Python
- Python **3.8 or higher**
- Required libraries:
pip install numpy pandas matplotlib seaborn scikit-learn
📊 R
R (latest version)
Required package:
install.packages("party")
▶️ How to Run
Clone or download this project.
Place all .csv datasets in the same folder as the scripts.
Run Python scripts one by one:
python severity.py
python timeofdayUK.py
python faultandtype.py
Run the R script in RStudio or R console:
source("dt.r")
## 📊 Outputs

### 📌 Accident Severity Analysis (India)
Plots relationships between:
- Severity  
- Light condition  
- Alcohol time  
- Speed zone  
- Gender  

---

### 📌 Time of Day Analysis (UK)
- Bar chart of accidents across 3-hour intervals  
- Pie chart showing accident distribution by day of week  

---

### 📌 Accident Fault & Vehicle Types (India)
Donut & pie charts showing:
- Causes of accidents  
- Types of vehicles involved  

---

### 📌 Decision Tree (R)
- Decision tree predicting accident severity based on **Day of Week** and **Light Condition**  

---

## 📑 Datasets Used
- **Data_Final.csv** → Accident records (India)  
- **datafile_4.csv** → Fault type data (India)  
- **Traffic accidents by time of occurrence 2001-2014.csv** → Time of day accidents (India)  
- **Accidents0515.csv** → Accident records (UK)  

---

## 📈 Sample Insights

### 🔹 Influence of Alcohol Consumption
- Over **61%** of accidents happen over the **weekend (Friday–Sunday)**  
- Suggestion: stricter monitoring near pubs, bars, and restaurants  

---

### 🔹 Vehicle Type & Faults
- **2-Wheelers**: ~35% involvement  
- **Heavy vehicles** (trucks, tractors, lorries): significant share  
- **Driver’s fault** is the leading cause in **>80%** of accidents  
- Suggestion: separate traffic lanes for different vehicles  

---

### 🔹 Accident Severity Index
- Defined as **total deaths per 100 accidents**  
- Noticeable rise from **2014 to 2016**  
- Indicates increasing fatalities despite improved infrastructure  

---

### 🔹 Other Plots
- Clustering of accident-prone areas using **K-Means**  
- Decision Trees for **severity factors**  
- Comparative plots for **yearly accident density**  

---

## 📌 Future Enhancements
- Merge datasets into a unified dashboard  
- Apply **Random Forests / Ensemble Models** for better prediction  
- Build a **web-based dashboard** with **Streamlit or Flask**  

---

## 👨‍💻 Author
- Rajesh Kumar
- 📅 *Created on 31 August 2025*  


