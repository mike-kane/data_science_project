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

    def save_cleaned_lyrics(self, song_title, song_lyrics):
        pattern = re.compile(r"(?:^\[[^\]]*\]$)|(?:[^a-zA-Z\s])", re.I | re.M)
        clean = re.sub(pattern, "", song_lyrics)
        file_name = song_title + '.txt'
        with open(file_name, "a+") as f:
            f.write(clean)
            print("file created successfully!")

    def get_raw_lyrics(self, song_title):
        # Create URL, get html, pull lyrics out of div class lyrics
        url = self.base_url + "/{}-{}-lyrics".format(self.artist, song_title)
        r = requests.get(url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html5lib')
        results = soup.find('p')
        raw_lyrics = results.text
        return raw_lyrics


if __name__ == "__main__":
    x = Lyrics_Scraper("luke_bryan_songlist.txt")
    song_title = x.get_song_list()[0]
    song_lyrics = x.get_raw_lyrics(song_title)
    x.save_lyrics(song_title, song_lyrics)
