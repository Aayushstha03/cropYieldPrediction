import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Provided data
data = {
    "Crop": ["BARLEY", "BARLEY", "BARLEY", "MAIZE", "MAIZE", "MAIZE", 
            "MILLET", "MILLET", "MILLET", "PADDY", "PADDY", "PADDY", 
            "WHEAT", "WHEAT", "WHEAT"],
    "Model": ["Linear Regression", "Random Forest", "SVR", 
            "Linear Regression", "Random Forest", "SVR",
            "Linear Regression", "Random Forest", "SVR", 
            "Linear Regression", "Random Forest", "SVR",
            "Linear Regression", "Random Forest", "SVR"],
    "R-squared": [0.86, 0.88, 0.86, 0.89, 0.91, 0.77, 0.96, 0.96, 0.95, 
                0.88, 0.89, 0.75, 0.87, 0.91, 0.81]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the plot style
sns.set(style="whitegrid")

# Set up figure size for A4 paper (in inches: 8.27 x 11.69)
a4_width, a4_height = 16,9  # landscape orientation

# Create the plot again with high resolution
plt.figure(figsize=(a4_width, a4_height), dpi=300)
ax = sns.barplot(data=df, x="Crop", y="R-squared", hue="Model", palette="Greens")

plt.xticks( fontsize=14)
plt.yticks( fontsize=14)


# Customize plot
plt.title("Model Performance (R-squared) Across Crops", fontsize=18, pad=20)
plt.ylim(0.7, 1.0)
plt.ylabel("R-squared", fontsize=16,labelpad=10)
plt.xlabel("Crop", fontsize=16,labelpad=10)
plt.legend(title="Model", fontsize=14, title_fontsize=16)
plt.tight_layout()

# Save the figure
# output_path = "/mnt/data/Model_Performance_A4_HighRes.png"
output_path = "D:/Git/cropYieldPrediction/Model_Performance_A4_HighRes.png"
plt.savefig(output_path, format='png', dpi=300)
# Show the plot
plt.close()


# New dataset
heatmap_data = {
    "Barley": {"Summer\nRainfall": 0.8, "Winter\nRainfall": 0.7, "Spring\nWind": 0.6},
    "Maize": {"Spring\nHumidity": 0.75, "Summer\nRainfall": 0.85, "Spring\nWind": 0.65},
    "Millet": {"Summer\nHumidity": 0.7, "Winter\nTemp": 0.6, "Winter\nWind": 0.65},
    "Paddy": {"Summer\nWind": 0.85, "Summer\nHumidity": 0.9, "Summer\nRainfall": 0.95},
    "Wheat": {"Spring\nHumidity": 0.8, "Summer\nHumidity": 0.75, "Autumn\nWind": 0.7},
}

# Convert to DataFrame
heatmap_df = pd.DataFrame(heatmap_data).T.fillna(0)

# Plot the heatmap
plt.figure(figsize=(16, 9))  # A4 landscape
sns.heatmap(heatmap_df, annot=True, cmap="Greens", linewidths=0, linecolor='gray', cbar_kws={'label': 'Correlation'})

# Set horizontal labels safely
plt.xticks(rotation=0, fontsize=14)
plt.yticks(rotation=0, fontsize=14)


# Customize plot
plt.title("Correlation of Climatic Factors with Crop Yield", fontsize=18, pad=20)
plt.xlabel("Climatic Factor", fontsize=16,labelpad=10)
plt.ylabel("Crop", fontsize=16, labelpad=10)
plt.tight_layout()

# Save high-resolution image
heatmap_output_path = "D:/Git/cropYieldPrediction/Crop_Climate_Correlation_Heatmap_A4_Greens.png"
plt.savefig(heatmap_output_path, dpi=300)
# plt.show()
plt.close()
