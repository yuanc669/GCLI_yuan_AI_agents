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

output_base = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\06_Prism_Outputs'

# Define 7 Specific Comparison Paths
paths = {
    "Path1_Aging": ["Sham", "Sham10W"],
    "Path2_Acute_Induction": ["Sham", "HS2W"],
    "Path3_DN_Establishment": ["Sham10W", "HS10W"],
    "Path4_Disease_Progression": ["Sham", "HS2W", "HS6W", "HS10W"],
    "Path5_Driver_Dissection": ["Sham10W", "SS10W", "HFD10W", "HS10W"],
    "Path6_Efficacy_Evaluation": ["Sham10W", "HS10W", "HS10WGaE9", "HS10WGaE10"],
    "Path7_Global_Integration": ["Sham10W", "SS10W", "HFD10W", "HS10W", "HS10WGaE9", "HS10WGaE10"]
}

metrics = ["BUN", "CRE", "AC", "TG", "BodyWeight (g)"]

for path_name, groups in paths.items():
    path_dir = os.path.join(output_base, path_name)
    os.makedirs(path_dir, exist_ok=True)
    
    path_df = df[df['Group'].isin(groups)].copy()
    path_df['Group'] = pd.Categorical(path_df['Group'], categories=groups, ordered=True)
    
    # Save CSV for Prism
    for metric in metrics:
        metric_short = metric.split(' ')[0]
        prism_ready = path_df.pivot(index='SampleID', columns='Group', values=metric)
        prism_ready.to_csv(os.path.join(path_dir, f"{path_name}_{metric_short}_Prism.csv"))
        
    # Generate Plots
    fig, axes = plt.subplots(1, 5, figsize=(25, 5))
    fig.suptitle(f"Biochemical Analysis - {path_name}", fontsize=16)
    
    for i, metric in enumerate(metrics):
        sns.boxplot(x='Group', y=metric, data=path_df, ax=axes[i], palette="Set2")
        sns.stripplot(x='Group', y=metric, data=path_df, ax=axes[i], color=".3", alpha=0.5)
        axes[i].set_title(metric)
        axes[i].set_xlabel("")
        
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(os.path.join(path_dir, f"{path_name}_Biochem_Summary.png"))
    plt.close()

print("Prism-ready CSVs and Summary Plots generated in 100_Research/02_Active/DN_GaExo/02_Analysis/Prism_Reports")
