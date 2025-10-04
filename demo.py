from core import extract_tickers, extract_urls, group_by_author

msgs = [
    {"author": "Kos", "text": "Готовится апдейт $APT — смотри https://pump.fun/apt"},
    {"author": "Kos", "text": "Думаю зайти в пул $APT"},
    {"author": "Alex", "text": "Фармлю на $SOL и $PYTH"},
]

print("tickers:", extract_tickers(" ".join(m["text"] for m in msgs)))
print("urls:", extract_urls(" ".join(m["text"] for m in msgs)))
print("grouped:", group_by_author(msgs))
