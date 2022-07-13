import requests
from bs4 import BeautifulSoup

reviews = []
ratings = []
pages_numbers = []

check = 0
page_num = 1
last_page = 999

while page_num <= last_page:
    url = f'https://www.cinemagia.ro/filme/avatar-17818/reviews/?pagina={page_num}&order_direction=DESC'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    if check == 0:
        check = 1
        max_pages = soup.find_all('a', class_='page_nav_link')
        for each in max_pages:
            pages_numbers.append(each.get_text())
            last_page = int(pages_numbers[-1])

    comment_content = soup.find_all('div', class_='comment_content')

    rating = 0
    count = 0
    for i in comment_content:
        scraped_review = i.find('div', class_='left comentariu')
        has_rating = i.find("span", class_='stelutze')
        if has_rating:
            reviews.append(scraped_review.get_text().strip())
            raw_ratings = i.find_all("span", {"class": "stelutze"})
            for j in raw_ratings:
                raw_rating = j.find_all("img")
                for p in raw_rating:
                    if "star_full.gif" in p.get("src"):
                        rating += 1
                    count += 1
                    if count == 10:
                        ratings.append(rating)
                        rating = 0
                        count = 0
    page_num += 1

for i in range(0, len(reviews)):
    reviews[i] = reviews[i].replace('\n', '')
            
from deep_translator import GoogleTranslator

texts = []
for i in range(0, len(reviews)):
    texts.append(reviews[i])
translated = GoogleTranslator('ro', 'en').translate_batch(texts)

with open("avatar_pos.txt", 'w', encoding="utf-8") as output_pos, open("avatar_neg.txt", "w", encoding="utf-8") as output_neg:
    for row_review, row_rating in zip(translated, ratings):
        if row_rating > 5:
            output_pos.write(str(row_review) + '\n')
        elif row_rating <= 5:
            output_neg.write(str(row_review) + '\n')