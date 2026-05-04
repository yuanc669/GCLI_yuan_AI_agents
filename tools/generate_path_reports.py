import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # For Traditional Chinese
plt.rcParams['axes.unicode_minus'] = False

# Load data
df = pd.read_csv(r'100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Cleaned_Data.csv')

output_dir = r'100_Research\02_Active\DN_GaExo\02_Analysis\Prism_Reports'
os.makedirs(output_dir, exist_ok=True)

# Define Paths
paths = {
    "Path1_Aging": ["Sham", "Sham10W"],
    "Path2_Acute": ["Sham", "HS2W"],
    "Path3_Late": ["Sham", "HS10W"],
    "Path4_Progression": ["Sham", "HS2W", "HS6W", "HS10W"],
    "Path5_Drivers": ["Sham10W", "HFD10W", "HS10W"],
    "Path6_Therapy": ["HS10W", "HS10WGaE9", "HS10WGaE10"]
}

metrics = ["BUN", "CRE", "AC", "TG", "BodyWeight (g)"]

for path_name, groups in paths.items():
    path_df = df[df['Group'].isin(groups)].copy()
    
    # Ensure categorical order for plotting
    path_df['Group'] = pd.Categorical(path_df['Group'], categories=groups, ordered=True)
    
    # Save CSV for Prism
    for metric in metrics:
        prism_ready = path_df.pivot(columns='Group', values=metric)
        # Clean up column names for Prism
        prism_ready.to_csv(os.path.join(output_dir, f"{path_name}_{metric.split(' ')[0]}_Prism.csv"))
        
    # Generate Plots
    fig, axes = plt.subplots(1, 5, figsize=(25, 5))
    fig.suptitle(f"Biochemical Analysis - {path_name}", fontsize=16)
    
    for i, metric in enumerate(metrics):
        sns.boxplot(x='Group', y=metric, data=path_df, ax=axes[i], palette="Set2")
        sns.stripplot(x='Group', y=metric, data=path_df, ax=axes[i], color=".3", alpha=0.5)
        axes[i].set_title(metric)
        axes[i].set_xlabel("")
        
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(os.path.join(output_dir, f"{path_name}_Biochem_Summary.png"))
    plt.close()

print("Prism-ready CSVs and Summary Plots generated in 100_Research/02_Active/DN_GaExo/02_Analysis/Prism_Reports")
