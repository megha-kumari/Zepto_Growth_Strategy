import pandas as pd
import numpy as np

# Constants and initial values
initial_capital = 15e6  # INR
initial_customers = 1.02e6
marketing_baseline = 5e6  # INR
profit_margin = 0.20
aov = 300  # INR
days = 30

# Results storage
results = []

# Initialize variables
capital_available = initial_capital
customers = initial_customers

# Helper functions
def calculate_probability(mi):
    return 0.8 * (1.25 - np.exp(-mi / 5))

def calculate_growth(probability, marketing_spend, marketing_baseline):
    return (38 / 40) + (1 / 40) * ((0.45 + probability) ** 0.30 + ((marketing_spend / marketing_baseline) + 1) ** 0.05)

# Strategy: Allocate a fixed percentage initially to delivery and marketing improvement
delivery_percent = 0.60  # 60% of daily budget to delivery improvement
marketing_percent = 0.40  # 40% to marketing

# Iterate through each day
for day in range(1, days + 1):
    # Daily budget allocation
    mi = delivery_percent * capital_available
    mi = min(mi, capital_available)  # Ensure we don't overspend
    
    marketing_spend = marketing_percent * capital_available
    marketing_spend = min(marketing_spend, capital_available - mi)  # Ensure valid spending
    
    # Calculate probability and growth
    probability = calculate_probability(mi)
    growth = calculate_growth(probability, marketing_spend, marketing_baseline)
    
    # Update customer count and total orders
    new_customers = customers * growth
    total_orders = new_customers * 4  # Assuming an order frequency of 4 per week
    
    # Calculate profit and capital for the day
    daily_revenue = total_orders * aov
    daily_profit = daily_revenue * profit_margin
    capital_end = capital_available - (mi + marketing_spend) + daily_profit
    
    # Append results
    results.append({
        "Day": day,
        "Capital Start": capital_available,
        "C_i-1": customers,
        "mi": mi,
        "p": probability,
        "M_i": marketing_spend,
        "G": growth,
        "C_i": new_customers,
        "Total Orders": total_orders,
        "Capital End": capital_end
    })
    
    # Update for next day
    capital_available = capital_end
    customers = new_customers

# Convert results to DataFrame
df_results = pd.DataFrame(results)

# Save to CSV for submission
df_results.to_csv("results/Zepto_Growth_Strategy.csv", index=False)
