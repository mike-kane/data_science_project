import requests
import re
from bs4 import BeautifulSoup


class Lyrics_Scraper():

    def __init__(self, song_list_path):
        self.artist = None
        self.base_url = "http://www.genius.com"
        self.song_list_path = song_list_path
        with open(song_list_path) as f:
            self.artist = f.readline().replace(' ', '-')
        self.artist = self.artist.replace('\n', '')

    def get_song_list(self):
        with open(self.song_list_path) as f:
            # Leave out item 0, arist's name is not a song
            song_list = list(f)[1::]
            # Chomp all newlines
            song_list = list(map(lambda s: s.strip('\n'), song_list))
            # replace spaces with dashes
            song_list = list(map(lambda s: s.replace(' ', '-'), song_list))
            return song_list

    def format_lyrics(song):
        pass

    def get_lyrics_for_song(self, song_title):
        # Create URL, get html, pull lyrics out of div class lyrics
        url = self.base_url + "/{}-{}-lyrics".format(self.artist, song_title)
        r = requests.get(url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html5lib')
        results = soup.find('p')
        lyrics = results.text
        print(type(lyrics))
        # for line in lyrics:
        #     line.string.replace_with()
        #  print(lyrics)

if __name__ == "__main__":
    x = Lyrics_Scraper("luke_bryan_songlist.txt")
    song = x.get_song_list()[0]
    print(x.get_lyrics_for_song(song))
