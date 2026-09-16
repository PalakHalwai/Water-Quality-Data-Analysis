import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the generated Option B dataset
df = pd.read_csv("water_community_data.csv")

print("==========================================")
print("     SUMMARY STATISTICS & FREQUENCIES     ")
print("==========================================")

# Frequency distributions
print("\n1. Primary Water Source Distribution (%):")
print((df["Primary_Water_Source"].value_counts(normalize=True) * 100).round(2))

print("\n2. Purification Method Distribution (%):")
print((df["Purification_Method"].value_counts(normalize=True) * 100).round(2))

print("\n3. Perceived Water Quality Distribution (%):")
print((df["Perceived_Quality"].value_counts(normalize=True) * 100).round(2))

print("\n4. Reported Health Complaint Distribution (%):")
print((df["Reported_Health_Complaint"].value_counts(normalize=True) * 100).round(2))

# 2. Cross-Tabulations
ct_treatment_health = pd.crosstab(
    df["Purification_Method"], df["Reported_Health_Complaint"]
)
ct_source_quality = pd.crosstab(df["Primary_Water_Source"], df["Perceived_Quality"])

print("\n==========================================")
print("     CROSS-TABULATION TABLES (COUNTS)     ")
print("==========================================")
print("\nPurification Method vs. Reported Health Complaints:")
print(ct_treatment_health)

print("\nPrimary Water Source vs. Perceived Water Quality:")
print(ct_source_quality)

# 3. Generate and Save Visualisations
sns.set_theme(style="whitegrid")

# Heatmap 1: Purification Method vs Reported Health Complaints
plt.figure(figsize=(9, 5.5))
sns.heatmap(ct_treatment_health, annot=True, fmt="d", cmap="YlGnBu", cbar=True)
plt.title(
    "Water Purification Method vs. Reported Health Complaints",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Reported Health Complaint", fontsize=10)
plt.ylabel("Water Purification Method Used", fontsize=10)
plt.tight_layout()
plt.savefig("treatment_vs_health_heatmap.png", dpi=300)
print("\n[INFO] Saved 'treatment_vs_health_heatmap.png'")
plt.show()

# Heatmap 2: Primary Water Source vs Perceived Water Quality
plt.figure(figsize=(9, 5.5))
sns.heatmap(ct_source_quality, annot=True, fmt="d", cmap="Oranges", cbar=True)
plt.title(
    "Primary Water Source vs. Perceived Water Quality", fontsize=12, fontweight="bold"
)
plt.xlabel("Perceived Water Quality", fontsize=10)
plt.ylabel("Primary Water Source", fontsize=10)
plt.tight_layout()
plt.savefig("source_vs_quality_heatmap.png", dpi=300)
print("[INFO] Saved 'source_vs_quality_heatmap.png'")
plt.show()
