import requests

def search_papers(topic: str, year_filter: str, citation_filter: str):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": topic,
        "fields": "title,year,citationCount,url",
        "limit": 100
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return f"API error: {response.status_code}"

    papers = response.json().get("data", [])
    results = []
    for paper in papers:
        try:
            if eval(f"{paper['year']} {year_filter}") and eval(f"{paper['citationCount']} {citation_filter}"):
                results.append({
                    "title": paper['title'],
                    "year": paper['year'],
                    "citations": paper['citationCount'],
                    "url": paper['url']
                })
        except:
            continue
    return results[:3] if results else "No matching papers found."
