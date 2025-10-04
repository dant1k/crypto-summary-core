
<h1 align="center">💬 crypto-summary-core</h1> <p align="center"> <b>Core text-analysis library for crypto chat insights</b><br> <a href="https://github.com/dant1k/crypto-summary-core/stargazers"> <img src="https://img.shields.io/github/stars/dant1k/crypto-summary-core?style=for-the-badge&color=yellow"/> </a> <a href="https://github.com/dant1k"> <img src="https://img.shields.io/badge/Made%20by-dant1k-8A2BE2?style=for-the-badge"/> </a> </p>
�� What it does

Parses raw Telegram/Discord messages into insights:

Extracts $tickers

Detects links

Groups messages by author

🔍 Example
from core import extract_tickers, extract_urls, group_by_author

text = "Alpha on $APT and $SOL soon — https://pump.fun/apt"
print(extract_tickers(text))  # ['APT', 'SOL']

🧩 Usage
python demo.py

👨‍💻 Author

@dant1k

