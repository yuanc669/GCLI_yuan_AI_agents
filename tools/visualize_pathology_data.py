import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup plotting style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial', 'Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

base_dir = r'100_Research/02_Active/DN_GaExo/02_Analysis/03_Pathology'
paths = ['Path1_Aging', 'Path2_Acute', 'Path3_Establishment', 'Path4_Progression', 'Path5_Driver', 'Path6_Efficacy', 'Path7_Global']
metrics = ['Tubular_Injury_Score', 'Glomerular_Area']

# Order of groups for logical plotting
group_orders = {
    'Path1_Aging': ['Sham', 'Sham-10W'],
    'Path2_Acute': ['Sham', 'HS2W'],
    'Path3_Establishment': ['Sham-10W', 'HS10W'],
    'Path4_Progression': ['Sham', 'HS2W', 'HS6W', 'HS10W'],
    'Path5_Driver': ['Sham-10W', 'SS10W', 'HFD10W', 'HS10W'],
    'Path6_Efficacy': ['Sham-10W', 'HS10W', 'HS10WGaE9', 'HS10WGaE10'],
    'Path7_Global': ['Sham-10W', 'SS10W', 'HFD10W', 'HS10W', 'HS10WGaE9', 'HS10WGaE10']
}

for path_name in paths:
    res_dir = os.path.join(base_dir, path_name, '02_Results')
    if not os.path.exists(res_dir):
        continue
    
    order = group_orders.get(path_name)
    
    for metric in metrics:
        csv_path = os.path.join(res_dir, f'{metric}.csv')
        if not os.path.exists(csv_path):
            continue
            
        # Load data
        df = pd.read_csv(csv_path)
        
        # Melt for seaborn
        df_melted = df.melt(var_name='Group', value_name='Value').dropna()
        
        # Plot
        plt.figure(figsize=(10, 6))
        
        # Bar plot for means and error bars (SEM)
        ax = sns.barplot(data=df_melted, x='Group', y='Value', order=order, 
                         palette='viridis', capsize=.1, errorbar='se', alpha=0.7)
        
        # Scatter plot for individual points
        sns.stripplot(data=df_melted, x='Group', y='Value', order=order, 
                      color='black', alpha=0.6, jitter=0.2, size=7)
        
        # Labels and Title
        title_name = metric.replace('_', ' ')
        plt.title(f'{path_name} - {title_name}', fontsize=16)
        plt.ylabel(title_name, fontsize=14)
        plt.xlabel('Group', fontsize=14)
        
        # Save plot
        plt.tight_layout()
        save_path = os.path.join(res_dir, f'{metric}_Plot.png')
        plt.savefig(save_path, dpi=300)
        plt.close()

print("✅ 所有路徑的數據圖片 (PNG) 已成功生成並存回各組的 02_Results 資料夾！")
