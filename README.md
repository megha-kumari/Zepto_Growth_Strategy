# Zepto_Growth_Strategy
Case study

# Zepto Growth Strategy

This project focuses on optimizing Zepto's growth strategy over a 30-day period. The goal is to determine the best allocation of capital between marketing spend and delivery improvements in order to maximize customer acquisition, order volume, and long-term profits.

## Project Overview

The Zepto Growth Strategy simulation tracks how marketing spend and delivery improvements affect the growth of Zepto's customer base and order volume over a 30-day period. The key objective is to determine the optimal capital allocation between marketing and delivery improvements to maximize profits while maintaining efficient capital utilization.

### Key Components:

1. **Simulation**: The main Python script (`growth_strategy.py`) simulates customer growth and capital usage over 30 days.
2. **Visualization**: The `visualization.py` script generates visualizations (e.g., customer growth, capital utilization, total orders).
3. **Sensitivity Analysis**: The `analysis.py` script performs sensitivity analysis to explore the effects of different capital allocation strategies (e.g., 50-50, 60-40, 70-30).

### Folder Structure:
/Zepto_Growth_Strategy ├── scripts/ # Contains Python scripts (growth_strategy.py, visualization.py, analysis.py) ├── results/ # Stores generated output files (Zepto_Growth_Strategy.csv) ├── visuals/ # Stores PNG images of visualizations (Capital_Utilization.png, Customer_Growth.png, etc.) ├── docs/ # Contains documentation files (README.md, analysis_report.pdf)

## How to Run the Code

1. **Clone the repository**:
git clone https://github.com/yourusername/Zepto_Growth_Strategy.git


2. **Install the required libraries**:
The project requires the following Python libraries:
- pandas
- matplotlib

To install them, run:
pip install pandas matplotlib


3. **Run the simulation**:
Run the `growth_strategy.py` script to simulate the growth strategy over 30 days:
python scripts/growth_strategy.py


This will generate the file `Zepto_Growth_Strategy.csv` in the `results/` folder.


4. **Generate visualizations**:
Run the `visualisation.py` script to generate visualizations (e.g., Capital Utilization, Customer Growth):
python scripts/visualisation.py


This will create PNG files in the `visuals/` folder.

5. **Run the sensitivity analysis**:
Run the `analysis.py` script to perform sensitivity analysis on different capital allocation strategies:

python scripts/analysis.py


This will create additional PNG files in the `visuals/` folder.

## Files Included

- **Python Scripts**:
- `growth_strategy.py`: Simulates the growth strategy over 30 days.
- `visualization.py`: Generates visualizations of key metrics (e.g., capital available, customer growth).
- `analysis.py`: Performs sensitivity analysis on different allocation strategies.

- **Results**:
- `Zepto_Growth_Strategy.csv`: Contains the day-wise results of the simulation.

- **Visualizations**:
- `Capital_Utilization.png`: Capital Available vs Capital End over 30 days.
- `Customer_Growth.png`: Customer growth over 30 days.
- `Total_Orders.png`: Total orders over 30 days.
- `Spending_Comparison.png`: Comparison of marketing and delivery spending.

- **Documentation**:
- `analysis_report.pdf`: Detailed report summarizing the findings, insights, and recommendations.








