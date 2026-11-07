# Streamlit Enterprise Reference Repository

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A definitive, enterprise-grade Streamlit reference repository engineered for Python developers and Data Engineers. This repository serves as a comprehensive knowledge base for production-ready Streamlit applications, covering fundamental UI components, state management, layout patterns, and data visualization.

## 📋 Executive Summary

This repository provides a complete reference implementation of Streamlit best practices, organized into modular sessions that progressively build from basic components to advanced dashboard patterns. Each session demonstrates clean architecture, type safety, proper state management, and production-ready code patterns.

**Key Features:**
- ✅ Production-ready code with type hints and docstrings
- ✅ Comprehensive Persian documentation (course notes + cheat sheet)
- ✅ Secure secrets management with `.streamlit/secrets.toml.example`
- ✅ Optimized caching strategies (`@st.cache_data` vs `@st.cache_resource`)
- ✅ Modular, maintainable architecture
- ✅ Docker-ready deployment configuration

## 📁 Repository Structure

```
streamlit/
├── .gitignore                          # Git ignore patterns
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── .streamlit/
│   ├── config.toml                     # Streamlit configuration
│   └── secrets.toml.example            # Secrets template (DO NOT commit actual secrets)
├── docs/
│   ├── streamlit-course-notes.fa.md    # Comprehensive Persian study handbook
│   └── streamlit-cheatsheet.fa.md      # Persian quick-reference cheat sheet
├── session1/
│   └── app.py                          # Basic UI Components & Data Display
├── session2/
│   └── query_panel.py                  # Form-Based Data Filtering
├── session3/
│   └── state_pipeline.py               # Session State & Callbacks
├── session4/
│   └── layout_dashboard.py             # Layout Containers & Dashboard Design
└── session5/
    └── viz_dashboard.py                # Data Visualization with Plotly
```

## 🗺️ Roadmap & Covered Topics

| Session | File Covered | Enterprise Concepts |
|---------|--------------|---------------------|
| Session 1 | `session1/app.py` | Page configuration, typography, status messages, dataframe display with column config, code blocks, JSON metadata |
| Session 2 | `session2/query_panel.py` | Form-based debounced input, widget types, conditional filtering, pandas string operations, caching mock data |
| Session 3 | `session3/state_pipeline.py` | Safe session state initialization, callback functions, state persistence, navigation patterns, idempotent operations |
| Session 4 | `session4/layout_dashboard.py` | Sidebar configuration, multi-column layouts, tab-based organization, fixed-height scrollable containers, nested containers |
| Session 5 | `session5/viz_dashboard.py` | Native vs Plotly charts, caching data generation, dark theme templates, correlation analysis, interactive visualizations |

## 🚀 Quickstart & Local Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Windows PowerShell

```powershell
# Clone the repository
git clone https://github.com/yourusername/streamlit.git
cd streamlit

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Setup secrets (copy example and fill in your values)
Copy-Item .streamlit\secrets.toml.example .streamlit\secrets.toml
# Edit .streamlit\secrets.toml with your actual credentials
```

### Linux/macOS (bash)

```bash
# Clone the repository
git clone https://github.com/yourusername/streamlit.git
cd streamlit

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup secrets (copy example and fill in your values)
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml with your actual credentials
```

### Secrets Configuration

Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and fill in your actual credentials:

```toml
[database]
host = "your-database-host.example.com"
port = 5432
database = "your_database_name"
username = "your_username"
password = "your_secure_password"

[api]
api_key = "your_api_key_here"
endpoint = "https://api.example.com"
```

**⚠️ IMPORTANT:** Never commit `.streamlit/secrets.toml` to version control. It is already in `.gitignore`.

### Running Individual Sessions

```bash
# Session 1: Basic UI Components
streamlit run session1/app.py

# Session 2: Form-Based Filtering
streamlit run session2/query_panel.py

# Session 3: Session State & Callbacks
streamlit run session3/state_pipeline.py

# Session 4: Layout Dashboard
streamlit run session4/layout_dashboard.py

# Session 5: Data Visualization
streamlit run session5/viz_dashboard.py
```

Each session runs on `http://localhost:8501` by default. To run on a different port:

```bash
streamlit run session1/app.py --server.port 8502
```

## 🐳 Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "session1/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build the image
docker build -t streamlit-reference .

# Run the container
docker run -p 8501:8501 \
  -v $(pwd)/.streamlit:/app/.streamlit \
  streamlit-reference
```

### Docker Compose (Recommended)

```yaml
version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./.streamlit:/app/.streamlit
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
    restart: unless-stopped
```

```bash
docker-compose up -d
```

## 📚 Documentation

### Persian Study Handbook
Comprehensive, publication-grade study handbook in Persian covering:
- Architecture & execution engine
- Step-by-step session module analysis
- Deep-dive code analysis
- Production troubleshooting matrix
- Technical audit log

📖 [Read Full Handbook](docs/streamlit-course-notes.fa.md)

### Persian Cheat Sheet
Dense, practical quick-reference for double-screen development:
- CLI commands and flags
- Syntax reference cards
- Architectural comparison tables
- Copy-paste production snippets

📖 [Read Cheat Sheet](docs/streamlit-cheatsheet.fa.md)

## 🏗️ Architecture Principles

### Stateless-Safe Design
- All state managed through `st.session_state` or caching
- No reliance on local variables for persistence
- Safe initialization pattern using `st.session_state.setdefault()`

### Cached Connections
- Database connections cached with `@st.cache_resource`
- Query results cached with `@st.cache_data` and TTL
- Clear cache hooks for manual invalidation

### Containerized Layout
- Structured layout using columns, tabs, and containers
- Fixed-height scrollable containers for log streams
- Responsive design with relative column widths

### Type Safety & Documentation
- Explicit type hints on all functions
- Comprehensive docstrings with parameter descriptions
- Module-level documentation explaining purpose

### Security Best Practices
- Secrets managed via `st.secrets` from `.streamlit/secrets.toml`
- No hardcoded credentials in source code
- Secrets template provided for easy setup

## 🔧 Development Guidelines

### Code Style
- Follow PEP 8 standards
- Use type hints for all function signatures
- Write docstrings for all functions and modules
- Modularize code into logical functions

### State Management
- Always use `st.session_state.setdefault()` for initialization
- Never mutate widget-bound keys after instantiation
- Use callbacks for complex state mutations
- Keep state minimal and focused

### Caching Strategy
- Use `@st.cache_data` for data transformations and query results
- Use `@st.cache_resource` for connections and expensive objects
- Set appropriate TTL for time-sensitive data
- Provide clear cache invalidation mechanisms

### Layout Patterns
- Use `st.form` for debounced input collection
- Organize complex UIs with tabs
- Use columns for responsive layouts
- Implement scrollable containers for long content

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes with descriptive messages
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Review Checklist
- [ ] Code follows PEP 8 standards
- [ ] Type hints included on all functions
- [ ] Docstrings present and comprehensive
- [ ] No hardcoded credentials
- [ ] Session state initialized safely
- [ ] Caching used appropriately
- [ ] Tests added for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - The amazing framework that makes this possible
- [Plotly](https://plotly.com/) - Interactive visualization library
- Data Engineering community for best practices and patterns

## 📞 Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Check the [Persian Handbook](docs/streamlit-course-notes.fa.md) for detailed explanations
- Refer to the [Cheat Sheet](docs/streamlit-cheatsheet.fa.md) for quick syntax reference

## 🔗 Resources

- [Streamlit Official Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Community Forum](https://discuss.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)

---

**Version:** 1.0.0  
**Last Updated:** 2026-11-07  
**Maintained by:** Data Engineering Team
