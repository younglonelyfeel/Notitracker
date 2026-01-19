import os
from pathlib import Path
from typing import List

# =============================================================================
# APPLICATION CONFIGURATION
# =============================================================================

# --- Environment Setup ---
# BASE_DIR handles cross-platform path compatibility (Windows/Linux)
BASE_DIR: Path = Path(__file__).parent.resolve()

# --- Secrets & Credentials ---
# SECURITY NOTE: These values should be loaded from Environment Variables in production.
# DO NOT hardcode actual tokens here to prevent leakage in version control.
TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID: str = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

# --- Persistence Paths ---
DATA_FILE: Path = BASE_DIR / "youtube_tracker.json"
CHANNELS_FILE: Path = BASE_DIR / "channels.json"
PAUSED_FILE: Path = BASE_DIR / "paused.json"
LOG_FILE: Path = BASE_DIR / "runtime.log"

# --- Performance Tuning ---
# Number of concurrent coroutines for fetching RSS feeds
FETCH_SEMAPHORE_COUNT: int = 5

# --- Networking ---
USER_AGENTS: List[str] = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
]