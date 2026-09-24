class Audio_Track:
    def __init__(self, title: str, duration: int):
        self.title = title
        self._duration = duration
        self._current_position = 0

    def get_duration(self):
        return self._duration

    def get_current_position(self):
        return self._current_position

    def forward(self, seconds: int):
        if seconds > 0:
            self._current_position += seconds
            if self._current_position > self._duration:
                self._current_position = self._duration

    def previous(self, seconds: int):
        if seconds > 0:
            self._current_position -= seconds
            if self._current_position < 0:
                self._current_position = 0

class Song(Audio_Track):
    def __init__(self, title: str, artist: str, writer: str, duration: int):
        super().__init__(title, duration)
        self.artist = artist
        self.writer = writer

    def start(self):
        print(f"Now playing: '{self.title}' by {self.artist}")

    def pause(self):
        print(f"Paused: '{self.title}' at {self._current_position}s")

class Album:
    def __init__(self, title: str, artist: str, release_year: int):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
        print(f"Added track: '{song.title}' to album '{self.title}'")

    def display_album(self):
        print(f"\nAlbum: {self.title} ({self.release_year})")
        for idx, song in enumerate(self.songs, start=1):
            print(f"    Track {idx}: '{song.title}' | Duration: {song.get_duration()}s")

print("Test 1: INHERITANCE")
song1 = Song("Keep Yourself Alive", "Queen", "Brian May", 225)
print(f"Child Object: '{song1.title}'")
print(f"Initial Position: {song1.get_current_position()}s")

print("Executing method: song1.forward(45)...")
song1.forward(45)
print(f"Updated Position: {song1.get_current_position()}s")

print("\nTest 2: AGGREGATION")
album1 = Album("Queen", "Queen", 1973)
song2 = Song("Doing All Right", "Queen", "Brian May-Tim Staffell", 250)

album1.add_song(song1)
album1.add_song(song2)

album1.display_album()
