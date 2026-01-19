# NotiTracker System

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A high-performance, asynchronous Telegram bot designed for real-time YouTube RSS tracking. Built with **Python 3.10+**, **Asyncio**, and **Aiohttp**, optimized for low latency and efficient resource usage.

## 🚀 Key Features

- **Asynchronous Core**: Fully non-blocking I/O operations allowing concurrent tracking of multiple channels without lag.
- **Smart Scheduling**:
  - **Burst Mode**: Automatically increases scan frequency for 5 minutes after detecting a new video.
  - **Jitter Intervals**: Randomized scan delays (50-80s) to prevent pattern detection.
  - **Hibernation Protocol**: Automatically reduces activity during off-hours (22:00 - 08:00) to save resources.
- **Resilience**:
  - Auto-retry mechanism for network fluctuations.
  - Handles `HTTP 429` (Too Many Requests) with exponential backoff.
- **Management Dashboard**: Full control via Telegram commands (Add, Remove, Mute, List, Status).

## 🛠️ Installation & Setup

### 1. For End Users (Deployment)
If you are deploying the pre-compiled binary:
1. Go to the [Releases Page](../../releases).
2. Download the latest `NotiTracker_v1.0.zip`.
3. Extract the archive.
4. Run `NotiTracker.exe`.
   *(Data and Log directories will be automatically generated upon first launch)*.

### 2. For Developers (Source Code)

**Prerequisites:**
- Python 3.10 or higher.
- `pip` package manager.

**Setup:**

```bash
# Clone the repository
git clone [https://github.com/younglonelyfeel/Notitracker.git](https://github.com/younglonelyfeel/Notitracker.git)
cd Notitracker

# Install dependencies
pip install -r requirements.txt

# Configure environment
# Ensure config.py is set up with valid credentials
python main.py
⚙️ ConfigurationThe system uses a centralized configuration file (config.py) for security practices.Security Note: Do not commit your config.py with real tokens to GitHub.Python# config.py example structure
TELEGRAM_BOT_TOKEN = "YOUR_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
FETCH_SEMAPHORE_COUNT = 5  # Max concurrent requests
HIBERNATION_WINDOW = (22, 8) # Sleep between 22h and 8h
🤖 CommandsInteract with the bot via Telegram using the following commands:CommandDescription/add <ID> <Name>Add a new channel to the tracking list./del <ID>Remove a channel and clear its persistent data./mute <ID>Pause tracking for a specific channel (Hibernation override)./unmute <ID>Resume tracking for a specific channel./listShow all tracked channels with status indicators./statusDisplay system health (RAM usage, Uptime, Threads)./stopManually stop the scanning loop./resumeResume the scanning loop.📂 Project StructureNotiTracker/
├── data/               # JSON persistence storage (Auto-generated)
├── logs/               # Runtime logs (Auto-generated)
├── config.py           # Configuration & Secrets
├── main.py             # Application Entry point
├── requirements.txt    # Project Dependencies
└── README.md           # Documentation
📜 LicenseDistributed under the MIT License. See LICENSE for more information.Maintained by @younglonelyfeel
