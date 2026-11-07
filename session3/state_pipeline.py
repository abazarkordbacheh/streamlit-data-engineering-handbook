"""Streamlit Session 3: Session State and Callbacks.

This module demonstrates session state management with:
- Safe session state initialization pattern
- Callback functions for button interactions
- State persistence across reruns
- Navigation through data lists
- Tracking reviewed items

Author: Data Engineering Team
Version: 1.0.0
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Any


def initialize_page() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Pipeline Status Management",
        page_icon="🔻",
        layout="wide"
    )
    st.title("Stateful Error Review")
    st.caption("Demonstrates session state persistence across user interactions")
    st.divider()


initialize_page()

@st.cache_data
def get_error_logs() -> List[Dict[str, str]]:
    """Generate mock error log data for demonstration.
    
    Returns:
        List of error log dictionaries.
    """
    return [
        {"error_id": "ERR-101", "job": "Sync_CDC_MSSQL", "message": "Deadlock detected during transaction commit"},
        {"error_id": "ERR-102", "job": "Agg_Sales_Daily", "message": "Memory limit exceeded: Worker killed by OOM"},
        {"error_id": "ERR-103", "job": "ClickHouse_Stream", "message": "Connection timeout: Socket reset by peer"},
        {"error_id": "ERR-104", "job": "Scraper_Divar", "message": "Rate limit exceeded (HTTP 429)"}
    ]


error_logs = get_error_logs()

def initialize_session_state() -> None:
    """Initialize session state with safe defaults."""
    st.session_state.setdefault("current_index", 0)
    st.session_state.setdefault("reviewed_errors", [])


initialize_session_state()

def next_error() -> None:
    """Navigate to the next error in the list."""
    if st.session_state.current_index < len(error_logs) - 1:
        st.session_state.current_index += 1


def prev_error() -> None:
    """Navigate to the previous error in the list."""
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1


def mark_as_reviewed() -> None:
    """Mark current error as reviewed."""
    current_err = error_logs[st.session_state.current_index]
    reviewed_ids = {item["error_id"] for item in st.session_state.reviewed_errors}
    if current_err["error_id"] not in reviewed_ids:
        st.session_state.reviewed_errors.append(current_err)


def clear_all() -> None:
    """Reset all session state to initial values."""
    st.session_state.reviewed_errors = []
    st.session_state.current_index = 0

def render_error_viewer() -> None:
    """Render the current error viewer panel with navigation controls."""
    st.subheader("Current Log Check Panel", divider="orange")
    current_item = error_logs[st.session_state.current_index]
    st.info(f"Error ID: {current_item['error_id']} => {st.session_state.current_index + 1} / {len(error_logs)}")
    st.text_input("Job Failed:", value=current_item["job"], disabled=True)
    st.text_area("Error Message (Traceback):", value=current_item["message"], disabled=True, height=120)
    
    btn_col1, btn_col2, btn_col3 = st.columns(3)

    with btn_col1:
        st.button(
            "⬅️ Previous Error",
            on_click=prev_error,
            disabled=(st.session_state.current_index == 0),
            use_container_width=True
        )

    with btn_col2:
        st.button(
            "✅ Mark as Reviewed",
            on_click=mark_as_reviewed,
            type="primary",
            use_container_width=True
        )

    with btn_col3:
        st.button(
            "➡️ Next Error",
            on_click=next_error,
            disabled=(st.session_state.current_index == len(error_logs) - 1),
            use_container_width=True
        )


def render_reviewed_history() -> None:
    """Render the panel showing reviewed errors."""
    st.subheader("Reviewed Errors", divider="green")

    if st.session_state.reviewed_errors:
        df_reviewed = pd.DataFrame(st.session_state.reviewed_errors)
        st.dataframe(df_reviewed, use_container_width=True, hide_index=True)
        st.button("🗑️ Clear History", on_click=clear_all, type="secondary", use_container_width=True)
    else:
        st.write("No reviewed errors yet.")


col_viewer, col_history = st.columns([3, 2])

with col_viewer:
    render_error_viewer()

with col_history:
    render_reviewed_history()

st.divider()

with st.expander("🔍 Debug Mode - Session State"):
    st.json(dict(st.session_state))
