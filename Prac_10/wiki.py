"""
CP1404 Practical 10
Theodore Lee
wiki.py
"""

import wikipedia


def main():
    search_request = input("Search: ")
    while search_request != "":
        try:
            requested_page = wikipedia.page(search_request, auto_suggest=False)
            print(f"Title: {requested_page.title}\nSummary: {requested_page.summary}\nURL: {requested_page.url}")

        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

        search_request = input("Search: ")

    print("Exited.")


if __name__ == "__main__":
    main()
