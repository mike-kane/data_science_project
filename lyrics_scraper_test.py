from lyrics_scraper import Lyrics_Scraper
import requests


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
    actual = test_scraper.get_lyrics_for_song(song_title)
    assert r.text == actual
