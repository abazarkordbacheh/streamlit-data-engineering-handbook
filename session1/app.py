"""Streamlit Session 1: Basic UI Components and Data Display.

This module demonstrates fundamental Streamlit UI components including:
- Page configuration
- Typography elements (title, caption, headers)
- Status messages (success, warning, error)
- Dataframe display with column configuration
- Code block display
- JSON metadata display

Author: Data Engineering Team
Version: 1.0.0
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from typing import Dict, Any

def initialize_page() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Streamlit Fundamentals",
        page_icon="🐱‍👤",
        layout="wide"
    )


initialize_page()


def render_header() -> None:
    """Render page header with title and server timestamp."""
    st.title("Streamlit UI Components Demo")
    st.caption(f"Server Time: {datetime.now().strftime('%Y-%m-%d')}")
    st.divider()


render_header()

def render_status_messages() -> None:
    """Demonstrate Streamlit status message components."""
    st.subheader("Status Messages", divider="blue")
    st.success("Operation completed successfully", icon="💚")
    st.warning("Configuration requires attention", icon="💛")
    st.error("Critical error detected", icon="❤")


render_status_messages()


def render_job_performance() -> None:
    """Display ETL job performance metrics with formatted dataframe."""
    st.subheader("Job Performance Metrics", divider="gray")

    monitoring_data: Dict[str, list] = {
        "Job Name": ["Sync_Customers_CDC", "Aggregate_Daily_Sales", "Clickhouse_Ingestion", "Divar_Scraper"],
        "Target Engine": ["MSSQL", "PostgreSQL", "ClickHouse", "MongoDB"],
        "Processed Rows": [145020, 8530, 2400500, 12400],
        "Duration (sec)": [14.2, 3.5, 85.0, 120.4],
        "Status": ["SUCCESS", "SUCCESS", "SUCCESS", "FAILED"]
    }
    df_jobs = pd.DataFrame(monitoring_data)

    st.dataframe(
        df_jobs,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Processed Rows": st.column_config.NumberColumn(
                "Processed Rows",
                format="%d"
            ),
            "Duration (sec)": st.column_config.NumberColumn(
                "Duration",
                format="%.1f s"
            )
        }
    )


render_job_performance()


def render_sql_reference() -> None:
    """Display SQL query reference with syntax highlighting."""
    st.subheader("SQL Query Reference", divider="red")

    sample_sql = """
SELECT job_name,
       target_engine,
       records_affected,
       execution_status
FROM sys_monitoring.etl_execution_logs
WHERE start_time >= DATEADD(day, -1, GETDATE());
    """

    st.code(sample_sql, language="sql", line_numbers=True)


render_sql_reference()
def render_environment_metadata() -> None:
    """Display environment metadata in JSON format."""
    st.subheader("Environment Metadata")
    metadata: Dict[str, Any] = {
        "cluster_node": "worker-data-01",
        "python_version": "3.11.8",
        "active_workers": 4
    }
    st.json(metadata)


render_environment_metadata()
