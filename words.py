"""
Demo DocString

Yields:
    Nothing
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch words from URL
    Args:
        url ():

    Returns:

    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for words in line_words:
            story_words.append(words)
    story.close()
    return story_words


def print_words(story_words):
    """Prints one item at a time
    :param story_words:
    :type story_words:
    """
    for word in story_words:
        print(word, end=" ")


def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    main(sys.argv[1])
