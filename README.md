# External Asset & Audit Automation Tools

## Overview
This repository contains two powerful tools designed to **automate external asset mapping and pentest audit validation**. These tools streamline **security assessments, validation processes, and asset ownership identification** by leveraging multiple data sources, automation, and cross-validation techniques.

### **1️⃣ Pentest Audit SPOG Tool**
#### **Purpose:**
- Provides a **Single Pane of Glass (SPOG)** for **pentest audit validation**.
- Ensures **test artifacts, reports, findings, and Archer data** remain aligned.
- Reduces human oversight errors by automating internal **pentest reporting audits**.

#### **Key Features:**
✅ **Automated Audit Checks** – Ensures **headers, risk ratings, and QC checklists** match Archer data.  
✅ **File Structure Validation** – Scans **SOW directories** and verifies required files.  
✅ **Multi-Source Validation** – Ensures **Archer status, report findings, and risk levels** match expectations.  
✅ **API-Ready** – Can be **extended to a web UI** or API for reporting.

#### **Upcoming Enhancements:**
- **Live dashboard** to provide real-time compliance monitoring.
- **Automated anomaly detection** in pentest reporting.
- **Integration with Archer API** for real-time validation.

---

### **2️⃣ External Asset Mapper**
#### **Purpose:**
- Maps **external-facing IPs to applications** using **multi-source intelligence.**
- Provides a **definitive external inventory** by correlating **Qualys, SSL certs, DNS records, and App ID mappings.**
- Identifies **multi-tenant VIPs** and flags discrepancies between **CIDR scans and Qualys findings**.

#### **Key Features:**
✅ **Multi-Source Data Collection** – Uses **Qualys, Reverse DNS, Passive DNS, SSL Certs, and CSI APIs**.  
✅ **VIP (Virtual IP) Handling** – Detects **multi-tenant hosts behind load balancers**.  
✅ **Cross-Validation of Findings** – Identifies deltas between **automated scans and Qualys results**.  
✅ **Graph-Based Mapping** – Generates JSON graphs, NetworkX diagrams, and Sankey flows for **VIP-host relationships**.  
✅ **Risk Prioritization** – Flags **high-risk deltas** for ASM/ASR program integration.

#### **Upcoming Enhancements:**
- **Interactive visualization dashboards** for better mapping of **VIP-to-backend relationships**.
- **Automated API export** for integration into **CMDB, ASM/ASR workflows**.
- **Machine Learning models** for anomaly detection in **asset exposure changes.**

---

## How These Tools Solve Critical Problems
🔴 **Problem: Unknown External Assets & Weak Inventory**  
🟢 **Solution: External Asset Mapper automates discovery, mapping, and validation.**

🔴 **Problem: Lack of Audit Oversight for Pentest Reports**  
🟢 **Solution: Pentest Audit SPOG ensures consistency and reduces manual audit efforts.**

🔴 **Problem: Unclear VIP Ownership & Multi-Tenant Risks**  
🟢 **Solution: Multi-source correlation detects VIPs with backend hosts and flags risks.**

---

## Installation & Usage
### **🔹 Prerequisites:**
- Python 3.8+
- Required Python modules (install via `pip install -r requirements.txt`)
- Access to Qualys scan data & CSI API (if applicable)

### **🔹 Running the Pentest Audit SPOG Tool**
```bash
python audit_spog.py --month 02 --export
```
- Run an audit for February (`--month 02`).
- Export results to JSON & Excel (`--export`).

### **🔹 Running the External Asset Mapper**
```bash
python external_mapper.py --input 192.168.1.0/24
```
- Expands **CIDR range**, collects data, and outputs validated mappings.

Or, for **Qualys scan ingestion:**
```bash
python external_mapper.py --input qualys_scan.json
```
- Parses Qualys scan, cross-checks findings, and flags discrepancies.

---

## Contributing
💡 **We welcome contributions!** If you have ideas for enhancements, **open an issue or submit a pull request.**  
📌 **Priority Features:** VIP detection improvements, UI visualization, API integration.

---

## Future Plans
🚀 **Phase 1:** Fully automate validation across **Qualys, SSL certs, and internal API mappings**.  
📊 **Phase 2:** Build **interactive visualization tools** for VIP tracking and risk mapping.  
🔍 **Phase 3:** Integrate **machine learning models** for **automated anomaly detection** in external asset changes.  

---

## Contact
🔗 **For questions, feature requests, or support, reach out via GitHub Issues or your internal security team.**

