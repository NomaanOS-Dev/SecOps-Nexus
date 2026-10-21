# 🛡️ SecOps-Nexus

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://secops-nexus.streamlit.app/)

An **All-in-One AI-Powered Cyber Security Operations Center (SOC) Suite & Threat Intelligence Platform** that unifies Log SIEM Threat Analysis, Firmware Vulnerability Scanning, and Security Document Investigation into a single dashboard.

Developed by **[NomaanOS-Dev](https://github.com/NomaanOS-Dev)**.

---

## 🚀 Unified Modules

1. **🚨 SIEM Log Anomaly Analyzer:** Parses authentication, access, and server logs for brute-force attacks, SQL injection attempts, and unauthorized execution.
2. **🛡️ Firmware Security Guardian:** Audits binaries, source code, and configuration files for exposed secret keys, hardcoded passwords, and high-entropy blocks.
3. **📄 Document Threat Investigator:** RAG-enabled document analysis engine for querying complex security policies, incident reports, and compliance guidelines.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Engine:** OpenAI `gpt-4o-mini` & LangChain Core
* **UI Framework:** Streamlit (Multi-Module Architecture)
* **Parsing Engine:** Regex Heuristics & Shannon Entropy Analysis

---

## 📦 Local Installation & Setup

1. **Clone Repository:**
   ```bash
   git clone [https://github.com/NomaanOS-Dev/SecOps-Nexus.git](https://github.com/NomaanOS-Dev/SecOps-Nexus.git)
   cd SecOps-Nexus
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Master Dashboard:**
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ License
Open-source SOC platform built for cyber security research, demonstration, and AI security engineering.
