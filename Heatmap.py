import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Input the annotation file 
somatic = pd.read_csv("annotation_file")

# Pivot the table to create the desired format
somatic_mutation_table = somatic.pivot_table(index='Patient ID', columns='Gene', aggfunc='size', fill_value=0)

# Reset the index and rename the columns
somatic_mutation_table = somatic_mutation_table.reset_index()
somatic_mutation_table.columns.name = None

# Give column from which the data will be indexed
somatic_mutation_table.set_index("Patient ID", inplace=True)

# Ouput frequency file 
somatic_mutation_table.to_csv("freq.csv")

# Create a heatmap
plt.figure(figsize=(20, 12))
sns.heatmap(somatic_mutation_table, fmt=".2f")

# Set labels for the axes
plt.xlabel("Genes")
plt.ylabel("Patients")

# Set the title
plt.title("Mutation Frequency in HRR Genes Across Somatic Patient Cohort")

# Show the heatmap
plt.show()