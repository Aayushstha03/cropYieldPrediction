import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    "Crop": ["BARLEY", "BARLEY", "BARLEY", "MAIZE", "MAIZE", "MAIZE", "MILLET", "MILLET", "MILLET", "PADDY", "PADDY", "PADDY", "WHEAT", "WHEAT", "WHEAT"],
    "Model": ["Linear Regression", "Random Forest", "SVR", "Linear Regression", "Random Forest", "SVR",
              "Linear Regression", "Random Forest", "SVR", "Linear Regression", "Random Forest", "SVR",
              "Linear Regression", "Random Forest", "SVR"],
    "R-squared": [0.86,0.88,0.86,0.89,0.91,0.77,0.96,0.96,0.95,0.88,0.89,0.75,0.87,0.91,0.81]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(26, 16), facecolor='none')
sns.set(style="whitegrid")
sns.barplot(x="Crop", y="R-squared", hue="Model", data=df, palette="Greens")

# Labels and Title
plt.xlabel("Crop", fontsize=26)
plt.ylabel("R-squared (Coefficient of Determination)", fontsize=26)
plt.title("Comparison of Model Performance (Higher is Better)", fontsize=34)
plt.legend(title="Model", fontsize=26)

# Save Plot with Higher Resolution
# plt.savefig("model_performance_comparison.png", dpi=300)

# Show Plot
plt.show()



# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Define crops and their top contributing factors with arbitrary importance values
# data = {
#     "Barley": {"Summer Rainfall": 0.8, "Winter Rainfall": 0.7, "Spring Wind Speed": 0.6},
#     "Maize": {"Spring Humidity": 0.75, "Summer Rainfall": 0.85, "Spring Wind Speed": 0.65},
#     "Millet": {"Summer Humidity": 0.7, "Winter Temperature": 0.6, "Winter Wind Speed": 0.65},
#     "Paddy": {"Summer Wind Speed": 0.85, "Summer Humidity": 0.9, "Summer Rainfall": 0.95},
#     "Wheat": {"Spring Humidity": 0.8, "Summer Humidity": 0.75, "Autumn Wind Speed": 0.7},
# }

# # Convert to DataFrame
# df = pd.DataFrame(data).T  # Transpose for better heatmap format

# # Plot heatmap
# plt.figure(figsize=(18, 8))
# sns.heatmap(df, annot=True, cmap="Greens", linewidths=0.5, fmt=".2f")

# # Labels and title
# # plt.xlabel("Factors")
# # plt.ylabel("Crops")
# plt.title("Heatmap of Top Contributing Factors for Each Crop", fontsize=20)
# plt.xticks(rotation=45, ha='right', fontsize=13)
# plt.yticks(fontsize=13)

# # Show plot
# plt.savefig("heatmap.png", dpi=600)
# plt.show()

