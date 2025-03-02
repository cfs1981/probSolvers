"""
External Asset Mapper - Automated Mapping of External IPs to Applications

This tool is designed to solve the challenge of mapping externally exposed IPs to their respective applications.
It achieves this by leveraging multiple data sources and ensuring validation between automated script results and commercial scanner outputs.

1️⃣ **Starting Point: CIDR Ranges or Qualys Scan Data**
   - Accepts CIDR ranges and expands them to individual IPs.
   - Parses Qualys scan data to extract IPs for processing.
   - **Cross-validates results between both methods**, identifying discrepancies between automated scripts and Qualys outputs.

2️⃣ **Extracting SSL Certificates**
   - Scrapes public certificate transparency logs (crt.sh, Censys, Google CT logs).
   - Probes external-facing edges directly for certificates (via OpenSSL & Nmap SSL scripts).
   - Pulls cert data from Qualys reports if available.

3️⃣ **Mapping Domains to App IDs**
   - Uses internal documentation or API pulls (e.g., CSI where application info is stored).
   - Cross-references domain names found in certs with known application mappings.

4️⃣ **Mapping IPs to Domains**
   - Uses Reverse DNS lookups to find domains tied to externally exposed IPs.
   - Queries passive DNS databases (Censys, PassiveTotal, RiskIQ, VirusTotal, etc.) to enrich mappings.

5️⃣ **Validation & Correlation**
   - **Cross-validates results from CIDR expansion and Qualys scan data**, highlighting discrepancies.
   - Compares multiple data sources to validate findings.
   - Highlights inconsistencies and gaps between sources.
   - Generates **Delta Reports** to explain differences between the script's findings and Qualys results.
   - Flags **high-risk deltas** and logs them for integration into **ASM/ASR workflows**.

6️⃣ **VIP (Virtual IP) Handling & Multi-Tenant Identification**
   - Identifies **VIPs with multiple hosts behind them** by:
     - Parsing Qualys reports for VIP-related metadata.
     - Performing active **load balancer checks** (e.g., HTTP headers, round-robin detection, passive fingerprinting).
     - **Cross-checking multiple sources** (DNS, certificate SANs, server banners) for varying responses.
   - **Multi-Tenant VIP Detection:**
     - Runs repeated HTTP(s) requests to detect **rotating hostnames** behind a VIP.
     - Analyzes SSL certificate Subject Alternative Names (SANs) for multiple services on the same VIP.
     - Captures differences in HTTP response headers or content hash variations.
     - Detects distinct **server fingerprinting (TLS versions, ciphers, banners, etc.)**.
   - Generates **relationship mapping** between VIPs and their real hosts.
   - Flags **multi-tenant VIPs**, ensuring security teams are aware of shared infrastructure risks.

7️⃣ **Visualizing VIP-Host Mappings**
   - **JSON Graph Format**:
     - Outputs a structured JSON file representing the relationships between **VIPs, backend hosts, and applications**.
   - **GraphViz / NetworkX Diagrams**:
     - Generates interactive diagrams to **visualize multi-tenant VIP structures**.
     - Shows the mapping between **external VIPs and backend systems**.
   - **HTML Reports with Sankey Diagrams**:
     - Visual representation of **VIP traffic flow** to backend hosts.
     - Helps security teams understand how an external IP maps to multiple internal systems.

8️⃣ **Output & Reporting**
   - Generates structured JSON & CSV reports.
   - Option to send alerts for unknown IPs/domains without mappings.
   - Delta reports for discrepancies between automated scans and Qualys results.
   - Flags high-risk discrepancies for ASM/ASR workflows.
   - **Graph & JSON-based VIP relationship mapping.**
   - Future-ready for API integration.

9️⃣ **CLI Support for Dynamic Input & Error Handling**
   - Users can specify **CIDR ranges** or **Qualys scan files** as input.
   - Ensures **input validation**, rejecting malformed CIDRs or improperly formatted Qualys scans.
   - Handles missing or unexpected data fields gracefully, logging errors while continuing execution.
"""
