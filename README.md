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

### 1. For End Users (Pre-built)
If you just want to run the bot without coding:
1. Go to the [Releases Page](../../releases).
2. Download the latest `NotiTracker_v1.0.zip`.
3. Extract the archive.
4. Run `NotiTracker.exe`.

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
# Rename 'config.example.py' to 'config.py' and update your credentials.
