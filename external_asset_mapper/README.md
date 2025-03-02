# Ethical Hack Audit Tool

## 📌 Overview
The **Ethical Hack Audit Tool** is a CLI-based utility designed to **automate security audit processes** by verifying RSA Archer API data, ensuring proper report structures, and checking penetration test artifacts for quality control (QC).

This tool enables auditors to:
- Fetch and validate data from the **Archer API** 🔍
- Verify required folder structures for SOWs 📂
- Extract risk ratings from **Word reports** 📄
- Validate QC checklists from **Excel files** 📊
- Perform **date-based filtering** for report status (Preliminary or Final) 📅
- Generate structured **JSON & Excel reports** 📈
- Use **color-coded CLI output** for quick analysis 🎨

---
## 🚀 Features
✅ **Automated RSA Archer API Data Fetching**
✅ **Checks Folder Structure & QC Reports**
✅ **Multi-threaded for Fast Audits**
✅ **Date-Range & Report Status Filtering**
✅ **Export to JSON & Excel**
✅ **Colorized CLI Output**
✅ **Supports Both Interactive & Non-Interactive Modes**

---
## 🔧 Installation
### Prerequisites
Ensure you have **Python 3.8+** installed along with the required dependencies.

```sh
pip install -r requirements.txt
```

#### Required Libraries:
- `requests` (For API communication)
- `pandas` (For data handling & exporting results)
- `openpyxl` (For Excel file processing)
- `python-docx` (For Word document analysis)
- `colorama` (For CLI color formatting)

---
## 🎯 Usage
The tool supports both **interactive** and **non-interactive** modes.

### **1️⃣ Running in Interactive Mode**
Simply execute:
```sh
python audit_tool.py
```
You'll be prompted to enter a **month, filters, and export options** interactively.

### **2️⃣ Running with CLI Arguments**
For non-interactive mode, use CLI arguments:
```sh
python audit_tool.py --month 02 --export
```

### **3️⃣ Running Full Audit Across All SOWs**
```sh
python audit_tool.py --month all
```

### **4️⃣ Filtering by Report Status & Date Range**
#### Example: Get only **Preliminary** reports from **Jan 1 - Feb 10, 2024**
```sh
python audit_tool.py --status prelim --start-date 2024-01-01 --end-date 2024-02-10
```

### **5️⃣ Exporting to JSON & Excel**
Add `--export` to save results:
```sh
python audit_tool.py --month 02 --export
```
By default, results are saved in the **current directory**. To specify an output folder:
```sh
python audit_tool.py --month 02 --export --output-dir ./audit_results/
```

---
## 🎨 CLI Output Example
```
=== Pentest Audit Summary ===
SOW ID          | Structure       | Findings Match   | Archer Status   | Testers
--------------------------------------------------------------------------------
SOW_1234        | Valid           | Matches Archer   | Completed       | Tester1, Tester2
SOW_5678        | Missing: REPORTS| Mismatch Found   | In Progress     | Tester3
```
- **🟢 Green** = Matches Archer
- **🟡 Yellow** = Missing Reports
- **🔴 Red** = Mismatched Findings

---
## 🛠 Configuration
### **API Token Setup**
The tool reads Archer API credentials from a **config.json** file.
1. Create `config.json`:
```json
{
    "API_TOKEN": "your_secret_api_token"
}
```
2. Ensure `config.json` is in the same directory as `audit_tool.py`.

---
## 📂 File Structure
```
Ethical_Hack_Audit_Tool/
│-- audit_tool.py
│-- config.json
│-- requirements.txt
│-- README.md
│-- audit_log.log  # (Generated after execution)
│-- audit_results.json  # (Generated when exporting)
│-- audit_results.xlsx  # (Generated when exporting)
```

---
## 🏆 Future Enhancements
- ✅ **Web Dashboard** (Flask/Streamlit) for viewing results
- ✅ **Auto-email notifications** when mismatches are found
- ✅ **Integration with JIRA/Ticketing System**

---
## 👨‍💻 Contributors
- **Your Name** – Lead Developer
- **Team Member 1** – API Integration
- **Team Member 2** – Report Processing

🔹 Open to community contributions!

---
## 📜 License
MIT License © 2024 Ethical Hack Audit Tool

