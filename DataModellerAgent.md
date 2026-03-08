# Data Modeller Agent

An intelligent agent that analyzes source code, business logic, and data transformations to ensure proper data modeling practices. Now with **AI-powered LLM integration** for natural conversations and expert guidance!

## Features

### 🤖 LLM Agent Mode (NEW!)
- **Natural Conversations**: Chat naturally about data modeling topics
- **Analysis Interpretation**: Get AI explanations of analysis results
- **Code Review**: AI-powered code analysis and recommendations
- **Concept Explanations**: Learn data modeling concepts interactively
- **Context-Aware**: Agent remembers your conversation and project context
- **Multi-Provider**: Support for Anthropic Claude and OpenAI GPT

### 🔍 Code Analysis
- **Schema Detection**: Automatically identifies table structures, column types, and relationships
- **Transformation Analysis**: Tracks data transformations through ETL pipelines
- **Business Logic Validation**: Ensures business rules are consistently applied

### 📊 Data Lineage
- **Source-to-Target Mapping**: Traces data flow from source systems to targets
- **Dependency Graph**: Visualizes relationships between data entities
- **Impact Analysis**: Identifies downstream effects of schema changes

### ✅ Quality Checks
- **Naming Conventions**: Validates consistent naming patterns
- **Data Type Consistency**: Ensures appropriate data types
- **Null Handling**: Identifies missing null checks
- **Key Constraints**: Validates primary and foreign keys

### 📈 Optimization Suggestions
- **Index Recommendations**: Suggests missing indexes
- **Query Performance**: Identifies slow transformation patterns
- **Data Denormalization**: Recommends when to denormalize

## Quick Start

### 🚀 5-Minute Setup with LLM

1. **Launch the app**:
   ```bash
   .\create_shortcut.bat
   # Double-click desktop icon
   ```

2. **Configure LLM** (optional but recommended):
   - Click Configuration tab
   - Enable LLM
   - Choose provider (Anthropic or OpenAI)
   - Enter your API key
   - Click Save

3. **Start chatting**:
   ```
   /help - See available commands
   /explain star schema - Learn concepts
   /interpret - Get AI interpretation of analysis
   ```

📖 **Full LLM setup guide**: docs/LLM_SETUP_GUIDE.md

### 🖥️ Desktop Launch (Easiest)
```bash
# Setup once (creates desktop shortcut):
.\create_shortcut.bat

# Then double-click "Data Modeller Agent" icon on your desktop!
```

### 🌐 Web GUI (Interactive)

```bash
# Start the interactive GUI
python gui_app.py

# Or use the startup script (Windows)
start_gui_with_browser.bat

# Then open browser to: [URL_REMOVED]
```

**Features:**
- 💬 Chat with the agent
- 📁 Analyze projects visually  
- 📊 Generate reports with one click
- 📜 View conversation history
- ⚙️ Configure settings
- 🤖 Optional LLM integration (Claude/GPT)

### 📋 Command Line

```bash
# Install dependencies
pip install -r requirements.txt

# Analyze a project
python data_modeller_agent.py --project-path ./your-project

# Generate report
python data_modeller_agent.py --project-path ./your-project --output report.html
```

## 💾 Data Persistence

**Everything is saved automatically:**
- ✅ All conversations → `data/conversation_history.json`
- ✅ All analyzed projects → `data/projects_history.json`
- ✅ Configuration → `agent_config.yaml`
- ✅ Reports → `static/reports/`

View anytime in the GUI or directly in the files!

## 🤖 Two Operating Modes

### Mode 1: Rule-Based (Default - FREE)
- Static code analysis
- 100% local processing
- No API keys required
- Enterprise compliant

### Mode 2: LLM-Enhanced (Optional)
- Natural conversations powered by Claude or GPT
- Requires API key
- See LLM_INTEGRATION.md for setup

## Supported Languages & Frameworks

- **Python**: Pandas, PySpark, SQLAlchemy
- **SQL**: PostgreSQL, MySQL, SQL Server, Oracle
- **Data Tools**: dbt, Airflow, Apache Spark
- **Cloud**: Azure Data Factory, AWS Glue, BigQuery

## Configuration

Create a `data_modeller_config.yaml`:

```yaml
analysis:
  include_patterns:
    - "*.py"
    - "*.sql"
    - "*.ipynb"
  exclude_patterns:
    - "tests/*"
    - "venv/*"
  
rules:
  naming_convention: "snake_case"
  require_primary_keys: true
  check_null_handling: true
```

## Usage Examples

### Analyze Python Data Transformations
```python
from data_modeller import DataModeller

modeller = DataModeller()
results = modeller.analyze_python_file("transformations.py")
print(results.summary())
```

### Validate SQL Schema
```python
results = modeller.analyze_sql_file("schema.sql")
for issue in results.issues:
    print(f"{issue.severity}: {issue.message}")
```

### Generate Data Dictionary
```python
modeller.generate_data_dictionary(
    project_path="./src",
    output="data_dictionary.html"
)
```

## Architecture

```
data_modeller_agent/
├── analyzers/
│   ├── python_analyzer.py    # Python/Pandas/PySpark analysis
│   ├── sql_analyzer.py        # SQL parsing and analysis
│   └── schema_detector.py     # Schema extraction
├── validators/
│   ├── naming_validator.py    # Naming convention checks
│   ├── type_validator.py      # Data type validation
│   └── logic_validator.py     # Business logic consistency
├── reporters/
│   ├── html_reporter.py       # HTML report generation
│   └── json_reporter.py       # JSON output
└── data_modeller_agent.py     # Main agent
```

## License

MIT License - Use freely in your organization with proper compliance approval.
