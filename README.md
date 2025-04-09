<h1 align="center">🚀 XRecon</h1>
<p align="center">
  <strong>Advanced Cyber Reconnaissance & Vulnerability Detection Tool</strong><br>
  <em>Made with 💻 by <a href="https://github.com/ritikshrivas-ai">Ritik Shrivas</a></em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/ritikshrivas-ai/XRecon?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/ritikshrivas-ai/XRecon?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/forks/ritikshrivas-ai/XRecon?style=flat-square" alt="Forks">
  <img src="https://img.shields.io/github/issues/ritikshrivas-ai/XRecon?style=flat-square" alt="Issues">
  <img src="https://img.shields.io/github/languages/top/ritikshrivas-ai/XRecon?style=flat-square" alt="Language">
</p>

---

## 📌 Overview

**XRecon** is an all-in-one automated reconnaissance tool built for **bug bounty hunters**, **penetration testers**, and **cybersecurity researchers**. It combines **JavaScript analysis**, **API enumeration**, **vulnerability tagging**, and high-tech terminal visuals into one slick Python-powered package.

✨ Built for **Kali Linux**  
⚔️ Designed for **real-world recon workflows**  
🧠 Powered by **async execution and smart vulnerability detection**

---

## 🧠 Features

| Feature                        | Description |
|-------------------------------|-------------|
| 🎭 Dual Mode                  | High-Tech (glitchy UI + animations) and Stealth (silent, no-banner recon) |
| 🧬 JS Analyzer                | Extract secrets & endpoints using **LinkFinder** and **SecretFinder** |
| 🛰️ API Enumeration            | Discover old API endpoints from **Wayback Machine** via `waymore` |
| 📊 Smart HTML Report          | Categorized, color-coded, hacker-themed report |
| ⚡ Async Recon Engine         | Lightning-fast scanning via async/multithreaded modules |
| 🧠 Vulnerability Categorizer  | Auto tags URLs with likely vulns (XSS, SQLi, Open Redirect, etc.) |
| 👁️‍🗨️ Terminal Visuals          | Matrix logs, glitch effects, cyberpunk transitions |
| 💾 Auto Report Storage        | Saves output directly to `~/Desktop/XRecon_Report.html` |
| 🎨 Custom Banners             | Sharp ASCII & neon glitch banners with developer credits |

---

## 🧪 Supported Vulnerability Categories

- 🧨 SQL Injection (sqli)
- 🔥 XSS (Reflected & DOM)
- 🎣 Open Redirect
- 📤 SSRF / LFI / RFI
- 🔐 Auth Bypass Indicators
- 📎 Sensitive Data Exposure
- 🎯 JS Secrets & Endpoints
- 📡 Deprecated APIs (via Wayback)
- 💣 Command Injection
- 🧼 CRLF Injection
- 🛑 Clickjacking
- 🛡️ CSRF (Heuristic)
- 📚 Directory Traversal

---

## ⚙️ Installation

### 🐍 Requirements
```bash
sudo apt update && sudo apt install python3 python3-pip -y
git clone https://github.com/ritikshrivas-ai/XRecon.git
cd XRecon
pip install -r requirements.txt
