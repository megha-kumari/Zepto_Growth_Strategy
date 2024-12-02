import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the results CSV (assuming you have already generated the CSV file)
df_results = pd.read_csv('results/Zepto_Growth_Strategy.csv')

# Sensitivity Analysis: Explore different allocations for marketing and delivery improvement
allocations = [(0.50, 0.50), (0.60, 0.40), (0.70, 0.30)]
results_by_allocation = {}

for alloc in allocations:
    delivery_percent, marketing_percent = alloc
    capital_available = 15e6  # Starting capital
    customers = 1.02e6  # Starting customers
    results = []

    for day in range(1, 31):
        mi = delivery_percent * capital_available
        marketing_spend = marketing_percent * capital_available
        probability = 0.8 * (1.25 - np.exp(-mi / 5))
        growth = (38 / 40) + (1 / 40) * ((0.45 + probability) ** 0.30 + ((marketing_spend / 5e6) + 1) ** 0.05)
        new_customers = customers * growth
        total_orders = new_customers * 4  # Assuming order frequency is 4 per week
        
        daily_revenue = total_orders * 300
        daily_profit = daily_revenue * 0.20
        capital_end = capital_available - (mi + marketing_spend) + daily_profit
        
        results.append({
            "Day": day,
            "Capital Start": capital_available,
            "C_i-1": customers,
            "mi": mi,
            "M_i": marketing_spend,
            "G": growth,
            "C_i": new_customers,
            "Total Orders": total_orders,
            "Capital End": capital_end
        })
        
        capital_available = capital_end
        customers = new_customers
    
    # Save the results for each allocation strategy
    df_alloc = pd.DataFrame(results)
    results_by_allocation[alloc] = df_alloc
    
    # Plot the Sensitivity Analysis
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_alloc['Day'], df_alloc['C_i'], label=f'Customer Growth {delivery_percent*100}-{marketing_percent*100}', marker='o')
    ax.set_title('Sensitivity Analysis - Customer Growth with Different Allocations')
    ax.set_xlabel('Day')
    ax.set_ylabel('Customers')
    ax.legend()
    # Save as PNG
    fig.savefig(f'visuals/Sensitivity_Analysis_{delivery_percent*100}_{marketing_percent*100}.png')
    plt.close(fig)
