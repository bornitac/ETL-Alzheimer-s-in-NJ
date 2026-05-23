# 📊 ETL & Data Analysis: Alzheimer's Trends in New Jersey

**Alzheimer's Trends NJ** is a Python-based ETL pipeline that extracts public health data from the CDC, transforms and filters it for New Jersey Alzheimer's mortality records, and loads the results into a time-series visualization — uncovering long-term death rate patterns from 1999 to 2017.

---

## 🔍 What It Does

This project follows a full ETL workflow:

- **Extract**: Reads raw mortality data from the CDC's National Center for Health Statistics
- **Transform**: Filters for New Jersey Alzheimer's disease records, computes yearly average death counts, and sorts chronologically
- **Load**: Generates and saves a time-series line graph visualizing trends over time

---

## 📊 Key Findings

- Analyzes **10,000+ mortality records** across the United States
- Isolates **New Jersey-specific** Alzheimer's death data from 1999–2017
- Identifies whether Alzheimer's-related deaths increased, decreased, or plateaued over time

---

## 🛠️ Built With

- **Python** – Core scripting and ETL logic
- **Pandas** – Data extraction, cleaning, and transformation
- **Matplotlib** – Data visualization and trend graphing

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Install dependencies:
  ```bash
  pip install pandas matplotlib
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bornitac/ETL-Alzheimer-s-in-NJ
   ```
2. Download `Leading_Causes_of_Death_US.csv` from the [CDC / NCHS via data.gov](https://catalog.data.gov/dataset/nchs-leading-causes-of-death-united-states) and place it in the same folder as `final.py`

3. Run the script:
   ```bash
   python final.py
   ```

---

## 📈 Output

Generates a line graph saved as `AlzheimersinNJ.jpg` showing yearly average Alzheimer's deaths in New Jersey over time.

---

## 📂 Data Source

**NCHS – Leading Causes of Death: United States**
Published by the Centers for Disease Control and Prevention (CDC) / National Center for Health Statistics (NCHS)
🔗 https://catalog.data.gov/dataset/nchs-leading-causes-of-death-united-states
