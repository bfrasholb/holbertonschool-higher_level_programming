import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        posts_list = [{"id": post.get("id"), "title": post.get(
            "title"), "body": post.get("body")} for post in data]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
