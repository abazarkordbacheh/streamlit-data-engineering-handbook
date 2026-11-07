"""Streamlit Session 2: Form-Based Data Filtering.

This module demonstrates form-based data filtering with:
- st.form for debounced input collection
- Multiple widget types (text_input, multiselect, slider, checkbox)
- Conditional data filtering logic
- Form submission handling

Author: Data Engineering Team
Version: 1.0.0
"""

import streamlit as st
import pandas as pd
from typing import Tuple, List, Optional


def initialize_page() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Database Logs Filter Panel",
        page_icon="🔍",
        layout="wide"
    )
    st.title("ETL Logs Monitoring and Filtering Panel")
    st.caption("Using the form below, specify the conditions for extracting logs and click the Apply button.")


initialize_page()

@st.cache_data
def get_mock_logs() -> pd.DataFrame:
    """Generate mock ETL log data for demonstration.
    
    Returns:
        DataFrame containing simulated ETL execution logs.
    """
    return pd.DataFrame({
        "job_id": [101, 102, 103, 104, 105, 106],
        "job_name": [
            "sync_customers_cdc",
            "agg_sales_daily",
            "cdc_orders_stream",
            "clickhouse_bulk_insert",
            "divar_web_scraper",
            "sync_inventory_cdc"
        ],
        "target_db": ["MSSQL", "PostgreSQL", "MSSQL", "ClickHouse", "MongoDB", "MSSQL"],
        "records_processed": [15000, 420, 89000, 1200000, 3400, 0],
        "status": ["SUCCESS", "SUCCESS", "SUCCESS", "SUCCESS", "FAILED", "FAILED"]
    })


dummy_logs = get_mock_logs()

def render_filter_form() -> Tuple[str, List[str], Tuple[int, int], bool]:
    """Render the filter form and return user inputs.
    
    Returns:
        Tuple containing: search_query, selected_dbs, records_range, show_only_success
    """
    with st.form(key="filter_form"):
        st.subheader("Filter Settings", divider="blue")

        col1, col2 = st.columns(2)

        with col1:
            search_query = st.text_input(
                label="Search Job Name:",
                value="",
                help="Enter part of the job name to filter."
            )

            db_options = ["MSSQL", "PostgreSQL", "ClickHouse", "MongoDB"]
            selected_dbs = st.multiselect(
                label="Select Databases:",
                options=db_options,
                default=db_options
            )

        with col2:
            records_range = st.slider(
                label="Range of Records Processed",
                min_value=0,
                max_value=1500000,
                value=(0, 1500000),
                step=10000
            )
            show_only_success = st.checkbox(
                label="Show Only Successful Jobs",
                value=False
            )
            submit_button = st.form_submit_button(
                label="Apply Filters 🚀",
                type="primary",
                use_container_width=True
            )

    return search_query, selected_dbs, records_range, show_only_success, submit_button


search_query, selected_dbs, records_range, show_only_success, submit_button = render_filter_form()


def apply_filters(
    df: pd.DataFrame,
    search_query: str,
    selected_dbs: List[str],
    records_range: Tuple[int, int],
    show_only_success: bool
) -> pd.DataFrame:
    """Apply all filter conditions to the dataframe.
    
    Args:
        df: Source dataframe to filter.
        search_query: Text to search in job_name column.
        selected_dbs: List of target databases to include.
        records_range: Tuple of (min, max) records processed.
        show_only_success: If True, only show SUCCESS status.
    
    Returns:
        Filtered dataframe.
    """
    filtered_df = df.copy()

    if selected_dbs:
        filtered_df = filtered_df[filtered_df["target_db"].isin(selected_dbs)]

    if search_query:
        filtered_df = filtered_df[
            filtered_df["job_name"].str.contains(search_query.strip().lower(), case=False)
        ]

    min_rec, max_rec = records_range
    filtered_df = filtered_df[
        (filtered_df["records_processed"] >= min_rec) &
        (filtered_df["records_processed"] <= max_rec)
    ]

    if show_only_success:
        filtered_df = filtered_df[filtered_df["status"] == "SUCCESS"]

    return filtered_df


if submit_button:
    st.info("Fetching and filtering data...")

    filtered_df = apply_filters(
        dummy_logs,
        search_query,
        selected_dbs,
        records_range,
        show_only_success
    )

    st.success(f"{len(filtered_df)} records matching the filters were found.")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
else:
    st.write("Please select the desired filters in the form above and click 'Apply Filters'.")
