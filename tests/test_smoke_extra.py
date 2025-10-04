from core import extract_tickers, extract_urls

def test_extract_tickers_simple():
    assert set(extract_tickers("alpha $APT $SOL!")) >= {"APT","SOL"}

def test_extract_urls_simple():
    urls = extract_urls("see https://example.com and http://foo.bar")
    assert any(u.startswith("http") for u in urls)
