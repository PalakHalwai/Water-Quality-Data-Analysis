import numpy as np
import pandas as pd

# Set seed for reproducible survey data
np.random.seed(42)
num_samples = 150

data = {
    "Respondent_ID": [f"R{i+1:03d}" for i in range(num_samples)],
    "Age_Group": np.random.choice(
        ["Below 18", "18–25", "26–40", "41–60", "Above 60"],
        size=num_samples,
        p=[0.10, 0.30, 0.30, 0.20, 0.10]
    ),
    "Primary_Water_Source": np.random.choice(
        ["Municipal Pipe", "Borewell", "Water Tanker", "Public Standpost"],
        size=num_samples,
        p=[0.45, 0.25, 0.15, 0.15]
    ),
    "Purification_Method": np.random.choice(
        ["RO/UV Filter", "Boiling", "Candle Filter", "None"],
        size=num_samples,
        p=[0.35, 0.30, 0.15, 0.20]
    ),
    "Perceived_Quality": np.random.choice(
        ["Clear", "Turbid/Cloudy", "Bad Odor", "Foul Taste"],
        size=num_samples,
        p=[0.55, 0.20, 0.15, 0.10]
    ),
    "Reported_Health_Complaint": np.random.choice(
        ["None", "Digestive/Stomach Issues", "Skin Complaints", "Fever/Typhoid"],
        size=num_samples,
        p=[0.45, 0.30, 0.15, 0.10]
    )
}

df = pd.DataFrame(data)
df.to_csv("water_community_data.csv", index=False)
print("File successfully created: water_community_data.csv")
