from __future__ import annotations

import os
from typing import Optional, Dict, Any, List


def perplexity_search(
    query: str,
    max_results: int = 20,
    max_tokens: int = 12_500,
    max_tokens_per_page: int = 2048,
    search_after_date_filter: Optional[str] = None,
    search_before_date_filter: Optional[str] = None,
    country: Optional[str] = None,
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search Perplexity for web results and return a compact JSON-like dict.

    Keys: query, results. Each result includes title, url, date, last_updated, snippet.
    Optional filters allow date range (format %m/%d/%Y) and country scoping.
    """
    from dotenv import find_dotenv, load_dotenv
    from perplexity import Perplexity

    env_path = find_dotenv(usecwd=True)
    if env_path:
        load_dotenv(env_path)

    key = api_key or os.getenv("PERPLEXITY_API_KEY")
    if not key:
        raise ValueError("PERPLEXITY_API_KEY is not set")

    client = Perplexity(api_key=key)
    kwargs: Dict[str, Any] = {
        "query": query,
        "max_results": max_results,
        "max_tokens": max_tokens,
        "max_tokens_per_page": max_tokens_per_page,
    }
    if search_after_date_filter:
        kwargs["search_after_date_filter"] = search_after_date_filter
    if search_before_date_filter:
        kwargs["search_before_date_filter"] = search_before_date_filter
    if country:
        kwargs["country"] = country

    try:
        search = client.search.create(**kwargs)
    except Exception as e:
        return {"query": query, "results": [], "error": str(e)}

    out: List[Dict[str, Any]] = []
    for r in getattr(search, "results", []) or []:
        out.append(
            {
                "title": getattr(r, "title", None),
                "url": getattr(r, "url", None),
                "date": getattr(r, "date", None),
                "last_updated": getattr(r, "last_updated", None),
                "snippet": getattr(r, "snippet", None),
            }
        )
    return {"query": query, "results": out}
