from core import extract_tickers, extract_urls, group_by_author

def test_extract_tickers_and_urls():
    text = "Alpha on $APT and $SOL soon -> https://pump.fun/apt"
    assert set(extract_tickers(text)) >= {"APT","SOL"}
    assert any("http" in u for u in extract_urls(text))

def test_group_by_author():
    msgs = [{"author":"A","text":"hi"},{"author":"A","text":"yo"},{"author":"B","text":"ok"}]
    g = group_by_author(msgs)
    assert g["A"] == ["hi","yo"]
    assert g["B"] == ["ok"]
