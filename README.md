🧠 TumorZone-Mapper: A Network-Based Glioblastoma Visualization Tool
TumorZone-Mapper is a neuroimaging and data science application that leverages network science to visualize and analyze disruptions in brain connectivity caused by glioblastoma. This tool processes functional MRI (fMRI) data, constructs brain networks, and identifies tumor-impacted regions using graph theory metrics such as centrality, connectivity, and modularity.

🚀 Key Features
🧠 fMRI-Based Network Construction: Converts time-series fMRI data into functional brain networks using correlation matrices.

🌐 Tumor Zone Identification: Maps disruptions in network hubs and connectivity patterns to locate regions affected by glioblastoma.

🏷️ AAL Brain Region Labeling: Integrates Automated Anatomical Labeling (AAL) for meaningful interpretation of brain regions.

📊 Centrality Metrics Export: Outputs node-level statistics (e.g., degree, betweenness) to Excel or CSV for further clinical analysis.

🖼️ Interactive Visualization: Visualizes brain graphs with color-coded hubs and abnormal zones.

📁 User-Friendly GUI: Upload neuroimaging data and analyze tumor impact via an intuitive interface.

⚙️ Technologies Used
Python

NetworkX / Braphy / Nilearn

Pandas / NumPy

Matplotlib / Plotly

Streamlit (for GUI)

Excel Export (via OpenPyXL or Pandas)

🎯 Ideal For
Neuroscientists and clinicians seeking to understand functional disruptions in glioblastoma patients

Researchers in brain network analysis and neural modeling

Students exploring the intersection of machine learning, brain imaging, and graph theory

