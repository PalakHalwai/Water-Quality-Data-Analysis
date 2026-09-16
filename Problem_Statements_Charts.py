import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("water_community_data.csv")
sns.set_theme(style="whitegrid")

# -------------------------------------------------------------
# CHART 1: Grouped Bar Chart (Water Source vs Perceived Quality)
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
ct_source_qual = pd.crosstab(df["Primary_Water_Source"], df["Perceived_Quality"])
ct_source_qual.plot(kind="bar", figsize=(10, 6), colormap="Set2", edgecolor="black")
plt.title(
    "Problem Statement 1: Water Quality Perception by Source",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Primary Water Source", fontsize=10)
plt.ylabel("Number of Households", fontsize=10)
plt.xticks(rotation=0)
plt.legend(title="Perceived Quality")
plt.tight_layout()
plt.savefig("ps1_source_vs_quality_bar.png", dpi=300)
plt.close()
print("[INFO] Saved 'ps1_source_vs_quality_bar.png'")

# -------------------------------------------------------------
# CHART 2: Stacked Bar Chart (Purification vs Health Complaints)
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
ct_pur_health = (
    pd.crosstab(
        df["Purification_Method"], df["Reported_Health_Complaint"], normalize="index"
    )
    * 100
)
ct_pur_health.plot(
    kind="bar", stacked=True, figsize=(10, 6), colormap="Spectral", edgecolor="black"
)
plt.title(
    "Problem Statement 2: Health Complaint Proportions by Purification Method",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Purification Method Used", fontsize=10)
plt.ylabel("Percentage (%)", fontsize=10)
plt.xticks(rotation=0)
plt.legend(title="Health Complaint", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig("ps2_purification_vs_health_stacked.png", dpi=300)
plt.close()
print("[INFO] Saved 'ps2_purification_vs_health_stacked.png'")

# -------------------------------------------------------------
# CHART 3: Heatmap (Age Group vs Reported Health Complaint)
# -------------------------------------------------------------
plt.figure(figsize=(9, 5.5))
ct_age_health = pd.crosstab(df["Age_Group"], df["Reported_Health_Complaint"])
sns.heatmap(ct_age_health, annot=True, fmt="d", cmap="YlOrRd", cbar=True)
plt.title(
    "Problem Statement 3: Age Group vs. Reported Health Complaints",
    fontsize=12,
    fontweight="bold",
)
plt.xlabel("Reported Health Complaint", fontsize=10)
plt.ylabel("Age Group", fontsize=10)
plt.tight_layout()
plt.savefig("ps3_age_vs_health_heatmap.png", dpi=300)
plt.close()
print("[INFO] Saved 'ps3_age_vs_health_heatmap.png'")

# -------------------------------------------------------------
# CHART 4: Pie Chart (Overall Perceived Quality Breakdown)
# -------------------------------------------------------------
plt.figure(figsize=(7, 7))
quality_counts = df["Perceived_Quality"].value_counts()
colors = ["#66b3ff", "#ff9999", "#99ff99", "#ffcc99"]
plt.pie(
    quality_counts,
    labels=quality_counts.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    wedgeprops={"edgecolor": "black"},
)
plt.title(
    "Problem Statement 5: Overall Community Water Quality Perception",
    fontsize=12,
    fontweight="bold",
)
plt.tight_layout()
plt.savefig("ps5_quality_perception_pie.png", dpi=300)
plt.close()
print("[INFO] Saved 'ps5_quality_perception_pie.png'")

print("\nAll Problem Statement charts generated and saved successfully!")
