import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("water_community_data.csv")
sns.set_theme(style="whitegrid")

# -------------------------------------------------------------
# CHART 4: Grouped Bar Chart (Age Group vs Purification Method)
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
ct_age_pur = pd.crosstab(df["Age_Group"], df["Purification_Method"])
ct_age_pur.plot(kind="bar", figsize=(10, 6), colormap="Set3", edgecolor="black")

plt.title(
    "Problem Statement 4: Water Purification Method Adoption Across Age Groups",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Age Group", fontsize=10)
plt.ylabel("Number of Households", fontsize=10)
plt.xticks(rotation=0)
plt.legend(title="Purification Method Used")
plt.tight_layout()

# Save chart image
plt.savefig("ps4_age_vs_purification_bar.png", dpi=300)
plt.close()

print("[INFO] Saved 'ps4_age_vs_purification_bar.png' successfully!")
