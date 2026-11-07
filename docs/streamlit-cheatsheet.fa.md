# Streamlit Cheatsheet - راهنمای سریع فارسی

## CLI Commands

```bash
# اجرای ساده
streamlit run app.py

# اجرا با پورت خاص
streamlit run app.py --server.port 8501

# اجرا در headless mode (بدون باز کردن مرورگر)
streamlit run app.py --server.headless true

# اجرا با file watcher غیرفعال
streamlit run app.py --server.runOnSave false

# اجرا با debug mode
streamlit run app.py --logger.level debug

# اجرا با theme سفارشی
streamlit run app.py --theme.base dark

# نمایش help
streamlit run --help

# نسخه Streamlit
streamlit version

# ساخت config file
streamlit config show
```

## Page Configuration

```python
import streamlit as st

st.set_page_config(
    page_title="عنوان صفحه",
    page_icon="🚀",
    layout="wide",  # "centered" یا "wide"
    initial_sidebar_state="expanded",  # "auto", "expanded", "collapsed"
    menu_items=[
        {"label": "درباره ما", "icon": "info", "url": "https://example.com"}
    ]
)
```

## Typography

```python
st.title("عنوان اصلی")
st.header("زیرعنوان سطح 1")
st.subheader("زیرعنوان سطح 2")
st.caption("متن توضیحی کوچک")
st.text("متن ساده")
st.markdown("**Bold** و *Italic*")
st.write("هر چیزی: string, number, dataframe, etc.")
st.latex(r"E = mc^2")
```

## Status Messages

```python
st.success("عملیات موفق بود", icon="✅")
st.info("اطلاعات مهم", icon="ℹ️")
st.warning("هشدار", icon="⚠️")
st.error("خطا", icon="❌")
st.exception(exception_object)  # نمایش stack trace
```

## Dataframes & Column Configuration

```python
import pandas as pd
import streamlit as st

df = pd.DataFrame({...})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "col1": st.column_config.TextColumn("نام ستون", width="medium"),
        "col2": st.column_config.NumberColumn("عدد", format="%d"),
        "col3": st.column_config.NumberColumn("اعشار", format="%.2f"),
        "col4": st.column_config.ProgressColumn("پیشرفت", format="{:.0f}%"),
        "col5": st.column_config.CheckboxColumn("وضعیت"),
        "col6": st.column_config.LinkColumn("لینک", url_template="https://example.com/{col6}"),
        "col7": st.column_config.ImageColumn("تصویر"),
        "col8": st.column_config.DateColumn("تاریخ", format="YYYY-MM-DD"),
        "col9": st.column_config.DatetimeColumn("زمان", format="YYYY-MM-DD HH:mm:ss")
    },
    height=400
)

# Static table (بدون sorting/filtering)
st.table(df)
```

## Input Widgets

```python
# Text Input
text = st.text_input("نام", value="پیش‌فرض", max_chars=50, type="password")

# Number Input
number = st.number_input("عدد", min_value=0, max_value=100, value=50, step=1)

# Text Area
text_area = st.text_area("توضیحات", height=200, max_chars=1000)

# Selectbox
option = st.selectbox("انتخاب", ["گزینه 1", "گزینه 2", "گزینه 3"], index=0)

# Multiselect
options = st.multiselect("انتخاب چندگانه", ["A", "B", "C"], default=["A"])

# Slider
slider = st.slider("اسلایدر", min_value=0, max_value=100, value=50, step=1)

# Range Slider
range_slider = st.slider("محدوده", min_value=0, max_value=100, value=(20, 80))

# Checkbox
checkbox = st.checkbox("تایید", value=False)

# Toggle
toggle = st.toggle("فعال/غیرفعال", value=True)

# Radio
radio = st.radio("انتخاب", ["گزینه 1", "گزینه 2"], horizontal=True)

# File Uploader
file = st.file_uploader("آپلود فایل", type=["csv", "xlsx"])

# Color Picker
color = st.color_picker("انتخاب رنگ", "#FF0000")

# Date Input
date = st.date_input("تاریخ", datetime.now())

# Time Input
time = st.time_input("زمان", datetime.now().time())

# Camera Input
image = st.camera_input("دوربین")

```

## Forms

```python
with st.form("my_form", clear_on_submit=False):
    st.subheader("فرم ورودی")
    name = st.text_input("نام")
    email = st.text_input("ایمیل")
    submitted = st.form_submit_button("ارسال", type="primary")
    
    if submitted:
        st.success(f"ارسال شد: {name}, {email}")
```

## State Management

```python
# Safe Initialization Pattern
st.session_state.setdefault("counter", 0)
st.session_state.setdefault("items", [])

# Direct Access
if "key" not in st.session_state:
    st.session_state.key = default_value

# Callbacks
def increment():
    st.session_state.counter += 1

st.button("افزایش", on_click=increment)

# Callback with args
def set_value(val):
    st.session_state.value = val

st.button("تنظیم 10", on_click=set_value, args=(10,))

# Clear state
st.session_state.clear()  # پاک کردن کل session state
del st.session_state.key  # پاک کردن key خاص
```

## Containers & Layouts

```python
# Columns
col1, col2, col3 = st.columns([1, 2, 1])  # relative widths
with col1:
    st.write("ستون 1")
with col2:
    st.write("ستون 2 (عرض دو برابر)")
with col3:
    st.write("ستون 3")

# Tabs
tab1, tab2, tab3 = st.tabs(["تب 1", "تب 2", "تب 3"])
with tab1:
    st.write("محتوای تب 1")
with tab2:
    st.write("محتوای تب 2")

# Expander
with st.expander("نمایش جزئیات", expanded=False):
    st.write("محتوای مخفی")

# Container with border
with st.container(border=True):
    st.write("کادر با حاشیه")

# Container with fixed height (scrollable)
with st.container(height=200, border=True):
    for i in range(50):
        st.write(f"خط {i}")

# Sidebar
with st.sidebar:
    st.title("تنظیمات")
    option = st.selectbox("انتخاب", ["A", "B"])
```

## Native Charts

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": np.arange(100),
    "y": np.random.randn(100)
})

# Line Chart
st.line_chart(df, x="x", y="y")

# Area Chart
st.area_chart(df, x="x", y="y")

# Bar Chart
st.bar_chart(df, x="x", y="y")

# Scatter Chart
st.scatter_chart(df, x="x", y="y")

# Map
df_map = pd.DataFrame({
    "lat": [35.6892, 34.0522],
    "lon": [51.3890, -118.2437],
    "name": ["Tehran", "Los Angeles"]
})
st.map(df_map)
```

## Plotly Charts

```python
import plotly.express as px
import plotly.graph_objects as go

# Line Chart
fig = px.line(df, x="x", y="y", title="نمودار خطی")
st.plotly_chart(fig, use_container_width=True)

# Bar Chart
fig = px.bar(df, x="category", y="value", color="category")
st.plotly_chart(fig)

# Pie Chart
fig = px.pie(df, names="category", values="value", hole=0.3)
st.plotly_chart(fig)

# Scatter Plot
fig = px.scatter(
    df, x="x", y="y", color="category", size="size",
    hover_data=["name"], template="plotly_dark"
)
st.plotly_chart(fig)

# Heatmap
fig = px.imshow(df.corr(), text_auto=True)
st.plotly_chart(fig)

# Custom Figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y=df["y"], mode="lines"))
st.plotly_chart(fig)
```

## Caching

```python
# Cache Data (برای داده‌ها و queryها)
@st.cache_data(ttl=3600, show_spinner="در حال بارگذاری...")
def expensive_computation(x):
    import time
    time.sleep(2)
    return x * 2

result = expensive_computation(10)

# Cache Resource (برای connections و engineها)
@st.cache_resource
def get_database_connection():
    import psycopg2
    return psycopg2.connect(...)

conn = get_database_connection()

# Clear Cache
st.cache_data.clear()  # پاک کردن تمام cache_data
st.cache_resource.clear()  # پاک کردن تمام cache_resource

# Cache with hash_funcs
@st.cache_data(hash_funcs={pd.DataFrame: lambda df: df.to_csv(index=False).encode()})
def process_data(df):
    return df.process()
```

## Secrets

```python
# دسترسی به secrets
db_host = st.secrets["database"]["host"]
api_key = st.secrets["api"]["api_key"]

# استفاده در connections
import psycopg2
conn = psycopg2.connect(
    host=st.secrets["database"]["host"],
    database=st.secrets["database"]["database"],
    user=st.secrets["database"]["username"],
    password=st.secrets["database"]["password"]
)
```

## Utility Functions

```python
# Divider
st.divider()

# JSON Display
st.json({"key": "value"})

# Code Display
st.code("print('Hello')", language="python")

# Progress Bar
import time
bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    bar.progress(i + 1)

# Spinner
with st.spinner("در حال پردازش..."):
    time.sleep(2)
st.success("انجام شد!")

# Status
status = st.status("در حال پردازش...")
status.update(label="انجام شد!", state="complete", expanded=True)

# Rerun
st.rerun()  # اجرای مجدد اسکریپت

# Stop
st.stop()  # توقف اجرای اسکریپت

# Empty
st.empty()  # placeholder برای dynamic content
```

## Media Elements

```python
# Image
st.image("path/to/image.jpg", caption="توضیح تصویر", width=300)

# Audio
st.audio("path/to/audio.mp3", format="audio/mp3")

# Video
st.video("path/to/video.mp4")

# From URL
st.image("https://example.com/image.jpg")
```

## Buttons & Interactions

```python
# Simple Button
if st.button("کلیک کنید"):
    st.write("کلیک شد!")

# Button with Callback
def callback():
    st.session_state.clicked = True

st.button("کلیک", on_click=callback)

# Download Button
st.download_button(
    label="دانلود CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='data.csv',
    mime='text/csv'
)

# Link Button
st.link_button("باز کردن لینک", "https://example.com")

# Page Link
st.page_link("app.py", label="صفحه اصلی", icon="🏠")
```

## Configuration Options

```toml
# .streamlit/config.toml

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[client]
showErrorDetails = true
maxUploadSize = 200
toolbarMode = "minimal"

[logger]
level = "info"

[runner]
magicEnabled = true
fastReruns = true

[server]
port = 8501
headless = false
enableCORS = false
enableXsrfProtection = true
```

## مقایسه معماری

### Local Variable vs Session State vs Cache

| نوع | چرخه حیات | استفاده | Performance |
|-----|-----------|---------|-------------|
| Local Variable | هر rerun بازسازی می‌شود | داده‌های موقت محاسباتی | سریع |
| `st.session_state` | در session کاربر حفظ می‌شود | state بین rerunها | سریع |
| `@st.cache_data` | تا تغییر input یا TTL | داده‌های سنگین و queryها | کند در اولین اجرا، سریع در cache hit |
| `@st.cache_resource` | تا تغییر input یا TTL | connections و engineها | کند در اولین اجرا، سریع در cache hit |

### Widget داخل Form vs خارج Form

| ویژگی | داخل Form | خارج Form |
|-------|-----------|-----------|
| Rerun Trigger | فقط بعد از submit | بعد از هر تغییر |
| Debouncing | بله (همه تغییرات در یک batch) | خیر (هر تغییر rerun) |
| Performance | بهتر برای فرم‌های پیچیده | بهتر برای interactions ساده |
| Use Case | فرم‌های ورودی، فیلترها | controls real-time |

### Button Conditional vs Callback

| روش | اجرا | State Mutation | Best Practice |
|------|------|----------------|---------------|
| `if st.button:` | بعد از rerun | در body اسکریپت | برای actions ساده |
| `on_click=callback` | قبل از rerun | در callback function | برای state mutation پیچیده |

## Snippets آماده تولید

### Safe Session State Initialization

```python
import streamlit as st
from typing import Any, Dict

def init_session_state(defaults: Dict[str, Any]) -> None:
    """Initialize session state with safe defaults."""
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

# Usage
init_session_state({
    "counter": 0,
    "items": [],
    "user_id": None,
    "filters": {"status": "all", "date_range": None}
})
```

### Debounced Database Query Form

```python
import streamlit as st
import pandas as pd

@st.cache_data(ttl=300)
def query_database(query: str, params: dict) -> pd.DataFrame:
    """Execute database query with caching."""
    # Your database connection logic here
    import psycopg2
    conn = psycopg2.connect(...)
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df

with st.form("query_form"):
    query = st.text_area("SQL Query", value="SELECT * FROM table LIMIT 100;")
    submitted = st.form_submit_button("اجرای کوئری")
    
    if submitted:
        with st.spinner("در حال اجرا..."):
            df = query_database(query, {})
        st.dataframe(df)
```

### Cached Engine Resource + Cached Query Data

```python
import streamlit as st
import pandas as pd

@st.cache_resource
def get_db_engine():
    """Get cached database engine."""
    from sqlalchemy import create_engine
    return create_engine(st.secrets["database"]["connection_string"])

@st.cache_data(ttl=600)
def get_cached_data(table_name: str) -> pd.DataFrame:
    """Get cached table data."""
    engine = get_db_engine()
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)

# Usage
df = get_cached_data("users")
st.dataframe(df)

# Clear cache button
if st.button("پاک کردن Cache"):
    st.cache_data.clear()
    st.rerun()
```

### Multi-tab Dashboard Grid

```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("CPU", "42%", "+5%")
with col2:
    st.metric("Memory", "68%", "-2%")
with col3:
    st.metric("Disk", "75%", "0%")
with col4:
    st.metric("Network", "120 MB/s", "+10%")

# Tabs
tab1, tab2, tab3 = st.tabs(["داده‌ها", "تحلیل", "لاگ‌ها"])

with tab1:
    st.dataframe(pd.DataFrame(np.random.randn(10, 5)))

with tab2:
    import plotly.express as px
    df = pd.DataFrame({
        "x": np.arange(100),
        "y": np.random.randn(100)
    })
    st.line_chart(df, x="x", y="y")

with tab3:
    with st.container(height=300, border=True):
        for i in range(20):
            st.text(f"[{i}] Log message here")
```

### Dynamic Filter with Plotly Dark Theme

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def get_data():
    return pd.DataFrame({
        "category": np.random.choice(["A", "B", "C"], 100),
        "value": np.random.randn(100),
        "date": pd.date_range("2024-01-01", periods=100)
    })

df = get_data()

# Filters
with st.sidebar:
    categories = st.multiselect(
        "انتخاب دسته‌بندی",
        df["category"].unique(),
        default=df["category"].unique()
    )
    
    date_range = st.date_input(
        "محدوده تاریخ",
        value=(df["date"].min(), df["date"].max())
    )

# Apply filters
filtered_df = df[
    df["category"].isin(categories) &
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1]))
]

# Visualization
fig = px.scatter(
    filtered_df,
    x="date",
    y="value",
    color="category",
    template="plotly_dark",
    title="تحلیل داده‌ها"
)
st.plotly_chart(fig, use_container_width=True)

# Data table
st.dataframe(filtered_df, use_container_width=True)
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + /` | Toggle sidebar |
| `Alt + R` | Rerun script |
| `Ctrl + Enter` | Run current cell (در editor) |
| `Shift + Enter` | Run current cell و move to next |
| `Esc` | Close dialog |

## Error Messages رایج

| Error | Cause | Solution |
|-------|-------|----------|
| `st.set_page_config() must be called as the first Streamlit command` | فراخوانی بعد از widget | در ابتدای اسکریپت فراخوانی کنید |
| `AttributeError: 'Series' object has no attribute 'contains'` | استفاده از `.contains()` | از `.str.contains()` استفاده کنید |
| `KeyError: 'key' not in session_state` | key وجود ندارد | از `setdefault()` استفاده کنید |
| `RuntimeError: Widget state is out of sync` | conditional widget creation | widgetها را همیشه ایجاد کنید |

---

**نسخه**: 1.0.0  
**تاریخ آخرین به‌روزرسانی**: 2026-11-07
