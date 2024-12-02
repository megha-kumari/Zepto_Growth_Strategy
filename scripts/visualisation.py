import pandas as pd
import matplotlib.pyplot as plt

# Load the results CSV (assuming you have already generated the CSV file)
df_results = pd.read_csv('results/Zepto_Growth_Strategy.csv')

# Set up the figure and axis for multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Capital Available vs Capital End
axs[0, 0].plot(df_results['Day'], df_results['Capital Start'], label='Capital Start', color='blue', marker='o')
axs[0, 0].plot(df_results['Day'], df_results['Capital End'], label='Capital End', color='green', marker='x')
axs[0, 0].set_title('Capital Available vs Capital End')
axs[0, 0].set_xlabel('Day')
axs[0, 0].set_ylabel('Capital (INR)')
axs[0, 0].legend()

# Customer Growth (C_i)
axs[0, 1].plot(df_results['Day'], df_results['C_i'], label='Customer Growth (C_i)', color='orange', marker='s')
axs[0, 1].set_title('Customer Growth Over 30 Days')
axs[0, 1].set_xlabel('Day')
axs[0, 1].set_ylabel('Customers')
axs[0, 1].legend()

# Total Orders Over 30 Days
axs[1, 0].plot(df_results['Day'], df_results['Total Orders'], label='Total Orders', color='red', marker='d')
axs[1, 0].set_title('Total Orders Over 30 Days')
axs[1, 0].set_xlabel('Day')
axs[1, 0].set_ylabel('Total Orders')
axs[1, 0].legend()

# Marketing and Delivery Spending Trends
axs[1, 1].plot(df_results['Day'], df_results['M_i'], label='Marketing Spend (M_i)', color='purple', marker='^')
axs[1, 1].plot(df_results['Day'], df_results['mi'], label='Delivery Spend (mi)', color='brown', marker='v')
axs[1, 1].set_title('Marketing and Delivery Spending Trends')
axs[1, 1].set_xlabel('Day')
axs[1, 1].set_ylabel('Spending (INR)')
axs[1, 1].legend()

plt.tight_layout()

# Save the visualizations as PNG
plt.savefig('visuals/zepto_growth_strategy_plots.png')

# Show the plot
plt.show()
