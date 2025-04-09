#!/usr/bin/env python3
import os
import re
import sys
import time
import random
import argparse
import asyncio
import aiohttp
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
from rich.style import Style
from rich.table import Table
from rich.box import SIMPLE as SIMPLE_BOX

console = Console()

# Compact Project Information Banner
PROJECT_BANNER = """
╭────────────────────────────────────────────╮
│ ██╗  ██╗██████╗ ███████╗ ██████╗ ██████╗   │
│ ╚██╗██╔╝╚════██╗██╔════╝██╔════╝ ██╔══██╗  │
│  ╚███╔╝  █████╔╝█████╗  ██║  ███╗██████╔╝  │
│  ██╔██╗ ██╔═══╝ ██╔══╝  ██║   ██║██╔══██╗  │
│ ██╔╝ ██╗███████╗███████╗╚██████╔╝██║  ██║  │
│ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝  │
├────────────────────────────────────────────┤
│       XRecon - Advanced Recon Tool         │
├────────────────────────────────────────────┤
│ Developer: Ritik Shrivas                   │
│ GitHub: github.com/ritikshrivas-ai         │
│ Version: 2.0 (Quantum Edition)             │
╰────────────────────────────────────────────╯
"""

# Compact Mode Banners
MODE_BANNERS = {
    "high_tech": """
╭──────────────────────────────╮
│ ╔═╗╦ ╦╔═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗     │
│ ║  ╠═╣╠═╣╚═╗ ║ ╠═╣ ║ ║ ║     │
│ ╚═╝╩ ╩╩ ╩╚═╝ ╩ ╩ ╩ ╩ ╚═╝     │
│   HIGH-TECH MODE ACTIVE      │
╰──────────────────────────────╯
""",
    "stealth": """
╭──────────────────────────────╮
│ █▀▀ █▀▀█ █▀▀█ █░░ █▀▀ ▀▀█▀▀  │
│ █▀▀ █▄▄█ █▄▄▀ █░░ █▀▀ ░░█░░  │
│ ▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀ ░░▀░░  │
│     STEALTH MODE ACTIVE      │
╰──────────────────────────────╯
"""
}

VULN_PATTERNS = {
    "XSS": [r"<script", r"alert\(", r"onerror=", r"javascript:"],
    "SQLi": [r"'--", r"UNION SELECT", r"SELECT.*FROM", r" OR 1=1"],
    "LFI": [r"\.\./", r"etc/passwd", r"boot.ini"],
    "RCE": [r"bash -i", r"nc -e", r"cmd.exe"],
    "Open Redirect": [r"redirect=", r"url=", r"next=", r"dest="],
    "SSRF": [r"internal=", r"private=", r"admin=", r"127.0.0.1"],
    "IDOR": [r"id=", r"user=", r"account=", r"number=\d+"],
}

REPORT_PATH = str(Path.home() / "Desktop" / "xrecon_report.html")

def glitch_text(text):
    """Add glitch effect to text for high-tech mode"""
    glitch_chars = "▓▒░⍆⊙⍣⍟⍤⍥⍨⍩◉◈◌◍◐◑◒◓◔◕◖◗"
    return ''.join([c if random.random() > 0.1 else random.choice(glitch_chars) for c in text])

def matrix_effect(text):
    """Add matrix-style effect for high-tech mode"""
    matrix_chars = "01"
    return ''.join([c if random.random() > 0.9 else random.choice(matrix_chars) for c in text])

def color_log(msg, mode="info", tech_mode=False):
    """Enhanced logging with mode-specific effects"""
    styles = {
        "info": "[cyan]",
        "success": "[green]",
        "error": "[bold red]",
        "warn": "[yellow]",
        "debug": "[dim]",
    }
    
    if tech_mode:
        if random.random() > 0.7:
            msg = glitch_text(msg)
        elif random.random() > 0.9:
            msg = matrix_effect(msg)
    
    console.print(f"{styles.get(mode, '')}{msg}[/]")

async def fetch_urls(domain, tech_mode=False):
    """Fetch URLs from Wayback Machine with mode-specific delays"""
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=text&fl=original&collapse=urlkey"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if tech_mode:
                    color_log("⚡ Bypassing firewalls...", "debug", tech_mode)
                    await asyncio.sleep(0.5)
                    color_log("🔓 Decrypting data streams...", "debug", tech_mode)
                
                text = await resp.text()
                return list(set(text.splitlines()))
    except Exception as e:
        color_log(f"Error fetching URLs: {e}", "error", tech_mode)
        return []

def categorize_urls(urls, tech_mode=False):
    """Categorize URLs by vulnerability patterns"""
    categorized = {key: [] for key in VULN_PATTERNS}
    categorized["Other"] = []

    if tech_mode:
        color_log("🔍 Running deep vulnerability analysis...", "info", tech_mode)
    
    for url in urls:
        matched = False
        for vuln_type, patterns in VULN_PATTERNS.items():
            if any(re.search(pat, url, re.IGNORECASE) for pat in patterns):
                categorized[vuln_type].append(url)
                matched = True
                if tech_mode:
                    color_log(f"❗ Detected {vuln_type} pattern in URL", "warn", tech_mode)
                break
        if not matched:
            categorized["Other"].append(url)
    
    return categorized

def generate_html_report(categorized, tech_mode=False):
    """Generate cyberpunk-style HTML report"""
    report_title = "XRecon Intelligence Report"
    if tech_mode:
        report_title = glitch_text(report_title)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{report_title}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

body {{
    background-color: #0f0f0f;
    font-family: 'Share Tech Mono', monospace;
    color: #00ff41;
    margin: 0;
    padding: 20px;
    line-height: 1.6;
}}

.header {{
    border-bottom: 1px solid #00ff41;
    padding-bottom: 10px;
    margin-bottom: 30px;
}}

h1 {{
    color: #00ff41;
    text-shadow: 0 0 10px rgba(0, 255, 65, 0.5);
    font-size: 2em;
    margin-bottom: 0;
}}

.header p {{
    color: #008f11;
    margin-top: 5px;
    font-size: 0.9em;
}}

.category {{
    margin: 15px 0;
    border: 1px solid #00ff41;
    padding: 10px;
    border-radius: 3px;
    box-shadow: 0 0 10px rgba(0, 255, 65, 0.1);
    background-color: #0a0a0a;
}}

.category h2 {{
    color: #00ff41;
    border-bottom: 1px dashed #008f11;
    padding-bottom: 3px;
    font-size: 1.2em;
    display: flex;
    justify-content: space-between;
}}

.url {{
    padding: 5px;
    margin: 3px 0;
    background-color: #101820;
    border-left: 2px solid #00ff41;
    font-size: 0.8em;
    word-break: break-all;
    transition: all 0.2s ease;
}}

.url:hover {{
    background-color: #1a2a3a;
    border-left: 2px solid #ff00ff;
}}

.glitched {{
    animation: glitch 0.8s linear infinite;
}}

@keyframes glitch {{
    0% {{ text-shadow: 1px 0 rgba(255,0,255,0.7), -1px 0 rgba(0,255,255,0.7); }}
    25% {{ text-shadow: -1px 0 rgba(255,0,255,0.7), 1px 0 rgba(0,255,255,0.7); }}
    50% {{ text-shadow: 1px 0 rgba(255,0,0,0.7), -1px 0 rgba(0,0,255,0.7); }}
    75% {{ text-shadow: -1px 0 rgba(0,255,0,0.7), 1px 0 rgba(255,0,255,0.7); }}
    100% {{ text-shadow: 1px 0 rgba(255,255,0,0.7), -1px 0 rgba(255,0,0,0.7); }}
}}

.tech-mode .category h2 {{
    animation: pulse 1.5s infinite;
}}

@keyframes pulse {{
    0% {{ color: #00ff41; }}
    50% {{ color: #ff00ff; }}
    100% {{ color: #00ff41; }}
}}
</style>
</head>
<body class="{'tech-mode' if tech_mode else ''}">
<div class="header">
    <h1{' class="glitched"' if tech_mode else ''}>🚀 {report_title}</h1>
    <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    <p><strong>Tool:</strong> XRecon v2.0 | Developer: Ritik Shrivas</p>
</div>
"""

    for cat, urls in categorized.items():
        count = len(urls)
        if count == 0:
            continue
            
        html += f"""
<div class='category'>
    <h2>{cat} <span>{count} findings</span></h2>"""
        
        for url in urls:
            highlighted_url = re.sub(
                r'(\?|\&)([^=]+)=([^&]*)',
                r'\1<span style="color:#ff00ff">\2</span>=<span style="color:#00ffff">\3</span>',
                url
            )
            html += f"<div class='url'>{highlighted_url}</div>"
        
        html += "</div>"

    html += """
<script>
document.querySelectorAll('.url').forEach(item => {
    item.addEventListener('click', function() {
        this.style.borderLeft = '2px solid #ffff00';
        setTimeout(() => {
            this.style.borderLeft = '2px solid #00ff41';
        }, 300);
    });
});
</script>
</body></html>
"""

    with open(REPORT_PATH, "w") as f:
        f.write(html)

    color_log(f"✔ Report saved at: [link={REPORT_PATH}]{REPORT_PATH}[/link]", "success", tech_mode)

async def main(domain, tech_mode):
    """Main execution with mode-specific UI"""
    # Print project banner
    console.print(PROJECT_BANNER, style="bold cyan")
    
    # Add small delay for effect
    if tech_mode:
        with console.status("[bold green]Initializing systems..."):
            await asyncio.sleep(1)
    
    # Print mode banner
    console.print(MODE_BANNERS["high_tech" if tech_mode else "stealth"])
    
    # Create target table
    target_table = Table(
        show_header=True,
        header_style="bold magenta",
        width=40,
        box=SIMPLE_BOX
    )
    target_table.add_column("Scan Details", style="cyan", width=20)
    target_table.add_column("Value", style="green", width=20)
    target_table.add_row("Target Domain", domain)
    target_table.add_row("Scan Mode", "High-Tech" if tech_mode else "Stealth")
    target_table.add_row("Start Time", datetime.now().strftime('%H:%M:%S'))
    console.print(target_table)
    
    color_log("🚀 Starting reconnaissance...", "info", tech_mode)

    if tech_mode:
        color_log("⚡ Activating enhanced protocols...", "info", tech_mode)
        await asyncio.sleep(0.5)
    else:
        color_log("🕵 Running silent scan...", "info", tech_mode)

    with Progress() as progress:
        task_desc = "⚡ Scanning" if tech_mode else "🔍 Analyzing"
        task = progress.add_task(f"{task_desc} [cyan]{domain}[/]", total=100)
        
        urls = await fetch_urls(domain, tech_mode)
        
        for i in range(100):
            if tech_mode and i % 15 == 0:
                color_log(f"📶 Signal: {random.randint(75, 100)}%", "debug", tech_mode)
            await asyncio.sleep(0.02 if tech_mode else 0.01)
            progress.update(task, advance=1)

    color_log("📊 Categorizing findings...", "info", tech_mode)
    categorized = categorize_urls(urls, tech_mode)

    color_log("📄 Generating report...", "info", tech_mode)
    generate_html_report(categorized, tech_mode)
    
    if tech_mode:
        color_log("✅ [bold]MISSION COMPLETE[/]", "success", tech_mode)
    else:
        color_log("✅ Scan finished", "success", tech_mode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XRecon - Automated Recon Tool")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    parser.add_argument("-t", "--tech", help="Enable high-tech mode", action="store_true")
    args = parser.parse_args()

    try:
        asyncio.run(main(args.domain, args.tech))
    except KeyboardInterrupt:
        color_log("⌨️ Scan interrupted by user", "error", args.tech)
    except Exception as e:
        color_log(f"💥 Critical error: {e}", "error", args.tech)
