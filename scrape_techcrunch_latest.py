import requests
from bs4 import BeautifulSoup

def scrape_techcrunch_latest():
    base_url = "https://techcrunch.com"
    response = requests.get(f"{base_url}/latest/")
    soup = BeautifulSoup(response.text, "html.parser")

    posts = []
    for post_li in soup.select("ul.wp-block-post-template li.wp-block-post"):
        try:
            title_tag = post_li.select_one("h3.loop-card__title")
            title = title_tag.get_text(strip=True) if title_tag else "No title"
            url = title_tag.find("a")["data-destinationlink"] if title_tag and title_tag.find("a") else None
            image = post_li.select_one("img")["src"] if post_li.select_one("img") else None
            created_at = post_li.select_one("time")["datetime"] if post_li.select_one("time") else None

            # Fetch full article page
            if url:
                article_res = requests.get(url)
                article_soup = BeautifulSoup(article_res.text, "html.parser")
                content = article_soup.select_one("div.entry-content")
                content_text = content.get_text(strip=True) if content else "No content"
                posts.append({
                    "title": title,
                    "url": url,
                    "image": image,
                    "created_at": created_at,
                    "content": content_text
                })
        except Exception as e:
            print(f"Error processing post: {e}")

    return posts

if __name__ == "__main__":
    from pprint import pprint
    pprint(scrape_techcrunch_latest())
