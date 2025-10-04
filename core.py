import regex as re
from typing import List, Dict, Iterable

_TICKER_RE = re.compile(r'(?<![A-Za-z0-9_])\$([A-Z0-9]{2,10})(?![A-Za-z0-9_])')
_URL_RE = re.compile(r'(https?://[^\s]+)')

def extract_tickers(text: str) -> List[str]:
    """Return unique tickers (uppercased) like $SOL, $APT."""
    return sorted(set(m.upper() for m in _TICKER_RE.findall(text or "")))

def extract_urls(text: str) -> List[str]:
    """Return unique URLs found in text."""
    return sorted(set(_URL_RE.findall(text or "")))

def group_by_author(messages: Iterable[Dict]) -> Dict[str, List[str]]:
    """
    messages: [{'author':'Quentin','text':'...'}, ...]
    returns: {'Quentin':[line1, line2], ...}
    """
    out: Dict[str, List[str]] = {}
    for m in messages:
        a = m.get("author", "unknown")
        t = (m.get("text") or "").strip()
        if not t:
            continue
        out.setdefault(a, []).append(t)
    return out
