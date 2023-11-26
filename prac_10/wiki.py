"""
CP1404 Practical
Wiki api test program
Expected: 40m
Actual: 45m
"""

import wikipedia


def main():
    """Takes a title or phrase input from the user until blank, and prints the respective wiki summary."""
    search = input("Wikipedia title/phrase: ")
    while search != '':
        try:
            wiki_page = wikipedia.page(search)
        except wikipedia.exceptions.DisambiguationError as error:
            print(f"DisambiguationError: {error.options}")
            wiki_page = None

        if wiki_page:
            print(wiki_page.title)
            print(wiki_page.summary)
        search = input("\nWikipedia title/phrase: ")


if __name__ == '__main__':
    main()
