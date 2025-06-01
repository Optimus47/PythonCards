from bs4 import BeautifulSoup

html = """
<html><body><h1>Пример</h1><p>Это абзац.</p></body></html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)     # Пример
print(soup.p.text)      # Это абзац.
