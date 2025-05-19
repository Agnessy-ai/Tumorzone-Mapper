import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Tumor Zone Mapper", layout="wide")
st.title("🧠 Tumor Zone Mapper App")

# --- Upload files ---
patient_file = st.file_uploader("Upload Patient Connectivity Matrix (.csv)", type="csv")
control_file = st.file_uploader("Upload Control Average Matrix (.csv)", type="csv")
label_file = st.file_uploader("Upload AAL Region Labels (.txt or .csv)", type=["txt", "csv"])

if patient_file and control_file and label_file:
    patient = pd.read_csv(patient_file, header=None).values
    control = pd.read_csv(control_file, header=None).values
    labels = pd.read_csv(label_file, header=None).iloc[:, 0].tolist()

    if len(patient) != len(control) or len(labels) != len(patient):
        st.error("⚠️ Mismatched matrix or label dimensions.")
    else:
        # Build graphs
        G_patient = nx.from_numpy_array(patient)
        G_control = nx.from_numpy_array(control)

        # Compute degree centrality
        deg_p = nx.degree_centrality(G_patient)
        deg_c = nx.degree_centrality(G_control)

        # Detect abnormalities
        threshold = st.slider("Sensitivity Threshold", 0.01, 0.2, 0.05, 0.01)
        abnormal_nodes = [i for i in deg_p if abs(deg_p[i] - deg_c[i]) > threshold]

        # Display list
        st.subheader("🧠 Abnormal Brain Regions")
        abnormal_regions = [labels[i] for i in abnormal_nodes]
        st.write(abnormal_regions)

        # Visualize graph
        pos = nx.spring_layout(G_patient, seed=42)
        fig, ax = plt.subplots(figsize=(10, 8))
        nx.draw(G_patient, pos, node_color="skyblue", node_size=300, ax=ax, edge_color="gray")
        nx.draw_networkx_nodes(G_patient, pos, nodelist=abnormal_nodes, node_color="red", node_size=300, ax=ax)
        nx.draw_networkx_labels(G_patient, pos, labels={i: labels[i] for i in range(len(labels))}, font_size=6, ax=ax)
        ax.set_title("Tumor Zone Mapper Visualization", fontsize=14)
        st.pyplot(fig)

        # Export centrality table
        if st.button("📥 Download Centrality Metrics as Excel"):
            df_export = pd.DataFrame({
                "Region": labels,
                "Degree_Centrality_Patient": [deg_p[i] for i in range(len(labels))],
                "Degree_Centrality_Control": [deg_c[i] for i in range(len(labels))],
                "Difference": [deg_p[i] - deg_c[i] for i in range(len(labels))]
            })
            excel_buf = io.BytesIO()
            with pd.ExcelWriter(excel_buf, engine="xlsxwriter") as writer:
                df_export.to_excel(writer, index=False, sheet_name="Centrality")
            st.download_button("Download Excel", excel_buf.getvalue(), file_name="centrality_metrics.xlsx")
