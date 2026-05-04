import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# Paths
data_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\03_Pathology\01_Data\Pathology_Scoring_Data_Full.csv'
output_base = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\06_Prism_Outputs'

# Load data
df = pd.read_csv(data_path)

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

metrics = ["Mesangial_Expansion(0-4)", "Tubular_Injury(0-4)", "Inflammation(0-4)", "Casts(0-4)"]

for path_name, groups in paths.items():
    path_dir = os.path.join(output_base, path_name)
    os.makedirs(path_dir, exist_ok=True)
    
    path_df = df[df['Group'].isin(groups)].copy()
    path_df['Group'] = pd.Categorical(path_df['Group'], categories=groups, ordered=True)
    
    # Save CSV for Prism
    for metric in metrics:
        metric_short = metric.split('(')[0]
        prism_ready = path_df.pivot(index='Sample_ID', columns='Group', values=metric)
        prism_ready.to_csv(os.path.join(path_dir, f"{path_name}_{metric_short}_Prism.csv"))
        
    # Generate Plots
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    fig.suptitle(f"Pathology Analysis - {path_name}", fontsize=16)
    
    for i, metric in enumerate(metrics):
        sns.boxplot(x='Group', y=metric, data=path_df, ax=axes[i], palette="Pastel1")
        sns.stripplot(x='Group', y=metric, data=path_df, ax=axes[i], color=".3", alpha=0.5)
        axes[i].set_title(metric)
        axes[i].set_xlabel("")
        axes[i].set_ylim(0, 4.5)
        
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(os.path.join(path_dir, f"{path_name}_Pathology_Summary.png"))
    plt.close()

print(f"Pathology Prism CSVs and Summary Plots generated in {output_base}")
