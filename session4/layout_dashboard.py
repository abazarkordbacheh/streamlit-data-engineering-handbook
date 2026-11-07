"""Streamlit Session 4: Layout Containers and Dashboard Design.

This module demonstrates advanced layout patterns with:
- Sidebar configuration and controls
- Multi-column layouts for metrics
- Tab-based content organization
- Fixed-height scrollable containers
- Nested containers with borders

Author: Data Engineering Team
Version: 1.0.0
"""

import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime
from typing import Dict, Any


def initialize_page() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Database Monitoring Dashboard",
        page_icon="🖥️",
        layout="wide"
    )


initialize_page()

def render_sidebar() -> str:
    """Render sidebar controls and return selected cluster.
    
    Returns:
        Selected cluster name.
    """
    with st.sidebar:
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=60)
        st.title("Monitoring Settings")
        st.divider()

        selected_cluster = st.selectbox(
            label="Select Cluster",
            options=["Production - MSSQL CDC", "Analytics - ClickHouse", "NoSQL - MongoDB Replica", "Staging - PostgreSQL"]
        )

        auto_refresh = st.checkbox("Live Auto Update", value=True)
        debug_mode = st.toggle("Debug Mode", value=False)

        st.divider()
        st.caption("Data Engineering Team | Version 1.0.0")
    
    return selected_cluster


selected_cluster = render_sidebar()

def render_header(cluster_name: str) -> None:
    """Render page header with cluster name and timestamp."""
    st.title(f"Cluster Monitoring: {cluster_name}")
    st.caption(f"Latest monitoring snapshot: {datetime.now().strftime('%H:%M')}")


render_header(selected_cluster)

def render_kpi_metrics() -> None:
    """Render KPI metric cards in a 4-column layout."""
    col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
    
    with col_metric1:
        st.metric(label="Average CPU Usage", value="42.8 %", delta="+3.2 %", delta_color="inverse")
    
    with col_metric2:
        st.metric(label="Active Connections", value="184", delta="-12")
    
    with col_metric3:
        st.metric(label="TPS", value="4,850", delta="+320")
    
    with col_metric4:
        st.metric(label="Health Check", value="99.98 %", delta="STABLE")
    
    st.divider()


render_kpi_metrics()

def render_tabs() -> None:
    """Render tabbed content for nodes, queries, and alerts."""
    tab_nodes, tab_queries, tab_alerts = st.tabs([
        "🖥️ Server Node Status",
        "⚡ Active Queries",
        "🚨 Recent Warnings"
    ])

    with tab_nodes:
        st.subheader("Resource Status on Cluster Nodes")
        c_left, c_right = st.columns([2, 1])
        
        with c_left:
            node_data = pd.DataFrame({
                "Node ID": ["node-01 (Master)", "node-02 (Replica)", "node-03 (Replica)"],
                "IP Address": ["192.168.10.11", "192.168.10.12", "192.168.10.13"],
                "RAM Usage": ["78%", "45%", "52%"],
                "Disk Free": ["1.2 TB", "2.4 TB", "2.1 TB"],
                "Status": ["ONLINE", "ONLINE", "ONLINE"]
            })
            st.dataframe(node_data, use_container_width=True, hide_index=True)

            with st.container(border=True):
                st.markdown("**Main Node Specifications**")
                st.write("Ubuntu 22.04 LTS")
                st.write("**Uptime:** 48 days and 12 hours")
                st.button("Safe Service Restart", type="secondary", use_container_width=True)

    with tab_queries:
        st.subheader("Long-Running Queries")
        long_queries = pd.DataFrame({
            "SPID / Session": [841, 912, 1024],
            "Duration (sec)": [128, 94, 65],
            "Database": ["Analytics", "Core_DB", "Staging"],
            "Command": ["SELECT * FROM sales_fact...", "ALTER TABLE logs...", "CREATE INDEX idx_cdc..."]
        })
        st.dataframe(long_queries, use_container_width=True, hide_index=True)

        with st.expander("View Full Query for Session 1024"):
            st.code("CREATE INDEX idx_cdc_event_time ON staging.cdc_events (event_timestamp DESC);", language="sql")

    with tab_alerts:
        st.subheader("Infrastructure Alerts Log")
        st.warning("Disk space on Node 3 has dropped to less than 25%.", icon="⚠️")
        st.info("Automatic backup completed successfully at 2:00 AM.", icon="ℹ️")

    st.divider()


render_tabs()

def render_log_stream() -> None:
    """Render a fixed-height scrollable log stream container."""
    st.subheader("Real-time Log Stream")
    
    with st.container(height=180, border=True):
        for i in range(1, 15):
            st.text(
                f"[{datetime.now().strftime('%H:%M:%S')}] [INFO] Worker-{i % 4}: "
                f"Health check ping received (latency: {np.random.randint(1, 12)}ms)"
            )


render_log_stream()
