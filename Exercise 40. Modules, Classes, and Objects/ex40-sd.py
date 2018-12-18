# Exercise 40. Modules, Classes, and Objects - Study Drills

class Song(object):

    def __init__(self, name, lyrics, artist, album, year):
        self.name = name
        self.lyrics = lyrics
        self.artist = artist
        self.album = album
        self.year = year

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def print_details(self):
        print(f"\"{self.name}\" ({self.year}). ~{self.artist}~ {self.album}")

hbd_lyrics = ["Happy birthday to you",
              "I don't want to get sued",
              "So I'll stop right there"]

happy_bday = Song("Happy Birthday to You", hbd_lyrics, "Patty Hill", "Happy Birthday", 1893)

bulls_lyrics = ["They rally around tha family",
                "With pockets full of shells"]
bulls_on_parade = Song("Bulls on Parade", bulls_lyrics, "Rage Against the Machine", "Evil Empire", 1996)

happy_bday.print_details()
happy_bday.sing_me_a_song()
print("*****************")
bulls_on_parade.print_details()
bulls_on_parade.sing_me_a_song()