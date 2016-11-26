from lyrics_scraper import Lyrics_Scraper
import requests
import os
import time
from bs4 import BeautifulSoup


def setup():
    songlist = "luke_bryan_songlist.txt"
    test_scraper = Lyrics_Scraper(songlist)
    return test_scraper


def test_get_song_list():
    expected_song = "Are-You-Leaving-With-Him"
    test_scraper = setup()
    actual_song = test_scraper.get_song_list()[0]
    assert expected_song == actual_song


def test_make_request():
    test_scraper = setup()
    song_title = "Are-You-Leaving-With-Him"
    r = requests.get("http://genius.com/Luke-bryan-are-you-leaving-with-him-lyrics")
    html_content = r.text
    actual = test_scraper.get_raw_lyrics(song_title)
    soup = BeautifulSoup(html_content, "html5lib")
    results = soup.find('p')
    raw_lyrics = results.text
    assert raw_lyrics == actual


def test_save_cleaned_lyrics():
    test_scraper = setup()
    song_title = "Are-You-Leaving-With-Him"
    test_file_path = "test_output"
    lyrics_cleaned = False
    dirty_symbols = ['?', '!', '-', '.', '<', '>', '/']
    # ensure test output file does not already exist
    try:
        os.remove('test_output.txt')
        # time.sleep(0.5)
        print('"test_output.txt" deleted so test can continue')
    except FileNotFoundError:
        print("file does not exist.  Continue the test!")
    raw_lyrics = test_scraper.get_raw_lyrics(song_title)
    test_scraper.save_cleaned_lyrics(test_file_path, raw_lyrics)
    # Test to ensure regex has cleaned lyrics successfully
    with open(test_file_path + '.txt', 'r') as f:
        x = f.read()
        for symbol in dirty_symbols:
            if symbol in x:
                lyrics_cleaned = False
                break
            elif symbol == '/' and symbol not in x:
                lyrics_cleaned = True
        assert (lyrics_cleaned is True)
