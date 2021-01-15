import requests
import pyttsx3
import json

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def fetchData(url):
    data = requests.get(url)
    data = data.text
    save_news_json(data)
    return json.loads(data)


def save_news_text(text):
    with open("read_news.txt", "w") as f:
        f.write(text)


def save_news_json(data):
    with open("news.json", "w") as f:
        f.write(data)


if __name__ == "__main__":
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=fcc85de3acfd4573897bb988e9cdf7b7"
    # speak("Fahad is a good boy")
    data = fetchData(url)
    # for key in data.keys():
    #     print(data.get(key))
    articlesList = data.get("articles")
    for i, article in enumerate(articlesList):
        date = f"{article.get('publishedAt')}"
        title = f"{article.get('title').split('-')[0]}"
        source = f"{article.get('source').get('name')}"
        number = f"According to {source} :"
        print(news)
        news = f"{i+1}. {number}[{date}]\nTitle: {title}"
        save_news_text(news)
        speak(f"{number}")
        speak(f"{title}")
