# microbiome-analyst R Templates

## Step 1 - Preprocessing
```r
library(phyloseq)
library(vegan)
library(ggplot2)
library(microbiome)

# Create phyloseq object
ps <- phyloseq(
  otu_table(otu_mat, taxa_are_rows = FALSE),
  tax_table(tax_mat),
  sample_data(meta_df)
)

# Rarefaction
ps_rare <- rarefy_even_depth(
  ps,
  sample.size = min(sample_sums(ps)),
  rngseed = 42,
  replace = FALSE
)
```

## Step 2 - Alpha Diversity
```r
# Calculate Alpha Diversity
alpha_div <- estimate_richness(
  ps_rare,
  measures = c("Observed","Shannon","Simpson","Chao1")
)

# Merge metadata
alpha_div$Group <- sample_data(ps_rare)$Group

# Visualization
ggplot(alpha_div, aes(x = Group, y = Shannon, fill = Group)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(width = 0.2, size = 2, alpha = 0.7) +
  stat_compare_means(method = "kruskal.test") +
  theme_bw() +
  labs(title = "Shannon Alpha Diversity by Group",
       y = "Shannon Index", x = "Group")
```

## Step 3 - Beta Diversity
```r
# Bray-Curtis distance
bray_dist <- phyloseq::distance(ps_rare, method = "bray")

# PCoA
pcoa_res <- ordinate(ps_rare, method = "PCoA", distance = bray_dist)

# Plot PCoA
plot_ordination(ps_rare, pcoa_res, color = "Group", shape = "Group") +
  geom_point(size = 4, alpha = 0.8) +
  stat_ellipse(type = "t", linetype = 2) +
  theme_bw() +
  labs(title = "PCoA - Bray-Curtis Dissimilarity")

# PERMANOVA
meta_df <- data.frame(sample_data(ps_rare))
adonis2(bray_dist ~ Group, data = meta_df)
```

## Step 4 - Differential Abundance & Correlation
### LEfSe (using microbiomeMarker)
```r
library(microbiomeMarker)
mm_lefse <- run_lefse(
  ps, 
  group = "Group", 
  taxa_rank = "Genus", 
  lda_cutoff = 2.0
)
plot_abundance(mm_lefse, group = "Group")
```

### Phenotype Correlation (Spearman)
```r
# Assume metadata contains clinical markers like 'BUN', 'Cr'
library(microbiome)
library(dplyr)

# Extract core taxa
ps_core <- aggregate_taxa(ps, "Genus") %>% 
           microbiome::core(detection = 0.001, prevalence = 0.5)

# Correlation matrix
cor_res <- associate(
  abundances(ps_core), 
  sample_data(ps)[, c("BUN", "Cr")], 
  method = "spearman"
)
```
