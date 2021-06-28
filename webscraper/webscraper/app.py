import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
[print("* ", question.select_one(".question-hyperlink").getText(), question.select_one(".vote-count-post").getText())
 for question in questions]


# print(questions[0].select_one(".question-hyperlink").getText())
