"""Streamlit Session 5: Data Visualization with Plotly.

This module demonstrates interactive data visualization with:
- Streamlit native charts (line_chart)
- Plotly integration for advanced visualizations
- Pie charts for categorical distribution
- Scatter plots for correlation analysis
- Dark theme templates
- Cached data generation

Author: Data Engineering Team
Version: 1.0.0
"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from typing import Dict, Any


def initialize_page() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="ETL Data Analysis",
        page_icon="📊",
        layout="wide"
    )
    st.title("Pipeline Performance Analysis Dashboard")


initialize_page()

@st.cache_data
def get_mock_data() -> pd.DataFrame:
    """Generate mock ETL performance data for visualization.
    
    Returns:
        DataFrame with timestamp, records_processed, latency_ms, and error_type columns.
    """
    dates = pd.date_range(start="2026-11-01", periods=100, freq="h")
    data: Dict[str, Any] = {
        "timestamp": dates,
        "records_processed": np.random.randint(1000, 5000, size=100),
        "latency_ms": np.random.normal(50, 10, size=100),
        "error_type": np.random.choice(["Connection", "Parsing", "Timeout", "None"], size=100)
    }
    return pd.DataFrame(data)


df = get_mock_data()

def render_throughput_charts() -> None:
    """Render throughput line chart and error distribution pie chart."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data Processing Throughput")
        st.line_chart(df, x="timestamp", y="records_processed")
    
    with col2:
        st.subheader("Error Type Distribution")
        fig_pie = px.pie(
            df, 
            names="error_type", 
            title="Error Type Breakdown", 
            hole=0.3
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.divider()


render_throughput_charts()

def render_correlation_analysis() -> None:
    """Render scatter plot showing latency vs records processed correlation."""
    st.subheader("Correlation: Latency vs Data Volume")

    fig_scatter = px.scatter(
        df,
        x="records_processed",
        y="latency_ms",
        color="error_type",
        size="latency_ms",
        hover_data=["timestamp"],
        template="plotly_dark",
        title="Latency Correlation Analysis"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)


render_correlation_analysis()

def render_raw_data() -> None:
    """Render expandable raw data table."""
    with st.expander("Raw Data Log"):
        st.dataframe(df, use_container_width=True)


render_raw_data()
