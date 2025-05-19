import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# --------------------------
# Step 1: Load Connectivity Matrices
# --------------------------

patient_matrix = pd.read_csv("patient_connectivity_matrix.csv", header=None).values
control_matrix = pd.read_csv("control_average.csv", header=None).values

# --------------------------
# Step 2: Build Graphs
# --------------------------

G_patient = nx.from_numpy_array(patient_matrix)
G_control = nx.from_numpy_array(control_matrix)

# --------------------------
# Step 3: Compute Degree Centrality
# --------------------------

deg_patient = nx.degree_centrality(G_patient)
deg_control = nx.degree_centrality(G_control)

# --------------------------
# Step 4: Detect Abnormal Nodes
# --------------------------

threshold = 0.05  # Sensitivity level
abnormal_nodes = [
    i for i in deg_patient
    if abs(deg_patient[i] - deg_control[i]) > threshold
]

print(f"Abnormal regions (by node index): {abnormal_nodes}")

# --------------------------
# Step 5: Visualize
# --------------------------

plt.figure(figsize=(12, 9))
pos = nx.spring_layout(G_patient, seed=42)  # Layout for visualization

# Draw full patient graph
nx.draw_networkx_edges(G_patient, pos, alpha=0.3)
nx.draw_networkx_nodes(G_patient, pos, node_color="skyblue", node_size=300)

# Highlight abnormal nodes
nx.draw_networkx_nodes(G_patient, pos, nodelist=abnormal_nodes, node_color="red", node_size=300, label="Abnormal Nodes")

# Label nodes
nx.draw_networkx_labels(G_patient, pos, font_size=8)

plt.title("Tumor Zone Mapper: Abnormal Connectivity Highlighted")
plt.legend()
plt.tight_layout()
plt.show()
