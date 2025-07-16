# 🚀 XRecon: Quantum Reconnaissance Toolkit

> **XRecon v2.0 (Quantum Edition) — Offensive Automation for Elite Recon**

---

## 🧬 Overview

**XRecon** is a high-performance, cyberpunk-inspired reconnaissance engine built for bug bounty hunters, red teamers, and security researchers. Designed with quantum efficiency and maximum stealth in mind, XRecon automates deep web asset discovery, vulnerability mapping, and intelligence reporting — all in a single, stylish script.

- **Matrix UI:** Glitch & High-Tech mode visuals
- **Automated Wayback Historical Recon**
- **Pattern-Based Vulnerability Discovery:** XSS, SQLi, LFI, SSRF, Open Redirect, IDOR, RCE
- **Cyberpunk HTML Reporting:** Beautiful, actionable output — ready for ops or client handoff
- **Fast, Async, Minimal Dependencies**
- **Zero Bloat:** No hardcoded creds, no unsafe parsing, no weak crypto

---

## 🦾 Features

| Mode         | Description                                             |
| ------------ | ------------------------------------------------------ |
| High-Tech    | Glitch effects, cyber visuals, verbose output          |
| Stealth      | Silent mode, minimal logs, operational discretion      |
| Vuln Scan    | Auto-categorizes URLs by exploit patterns              |
| HTML Report  | Generates stylish, matrix-style report on desktop      |

---

## ⚡ Quickstart

```bash
git clone https://github.com/ritikshrivas-ai/XRecon.git
cd XRecon
pip3 install -r requirements.txt
python3 xrecon.py -d target.com -t          # High-Tech Mode
python3 xrecon.py -d target.com             # Stealth Mode
```

- **Report Output:** `~/Desktop/xrecon_report.html`  
- **Supported Python:** 3.8+

---

## 🔥 Usage

```bash
python3 xrecon.py -d example.com -t
```

| Flag         | Usage                           |
|--------------|---------------------------------|
| `-d, --domain` | Target domain (required)        |
| `-t, --tech`   | Enable high-tech mode (optional)|

---

## 🧩 Sample Output

![report](https://raw.githubusercontent.com/ritikshrivas-ai/XRecon/main/assets/report-preview.png)

---

## 👁️‍🗨️ Recon Modules

- **Wayback Machine Harvesting**
- **Pattern-Based Vulnerability Detection**
- **Cyberpunk Matrix/Glitch Effects**
- **Auto-Generated HTML Reports**

---

## 🕸️ Vulnerability Patterns Detected

- **XSS:** `<script>`, `alert()`, `onerror=`, `javascript:`
- **SQLi:** `UNION SELECT`, `'--`, `SELECT ... FROM`, `OR 1=1`
- **LFI:** `../`, `etc/passwd`, `boot.ini`
- **Open Redirect:** `redirect=`, `url=`, `next=`, `dest=`
- **SSRF:** `internal=`, `private=`, `admin=`, `127.0.0.1`
- **IDOR:** `id=`, `user=`, `account=`, `number=`
- **RCE:** `bash -i`, `nc -e`, `cmd.exe`

---

## 🛡️ OPSEC Notice

- **No credentials stored**
- **No unsafe input handling**
- **No weak crypto**
- Designed for **auditability** and **secure integration**

---

## 👤 Author

- **Ritik Shrivas**
- [GitHub](https://github.com/ritikshrivas-ai)
- [Twitter](https://twitter.com/ritikshrivas_ai)

---

## 🧠 Advanced Usage

For chaining, automation, or custom modules:  
See `xrecon.py` — every function is minimal, auditable, and ready for rapid integration.

---

## 💀 Disclaimer

> This tool is for educational and authorized security testing only. Do not use against systems without proper permission.

---
