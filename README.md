
crypto-summary-core

Lightweight text utilities for crypto-chat analytics: extract $tickers, URLs, and compact lines by author.
Install
pip install -r requirements.txt
Usage
from core import extract_tickers, extract_urls, group_by_author

print(extract_tickers("Alpha on $APT and $SOL soon"))
# ['APT', 'SOL']


