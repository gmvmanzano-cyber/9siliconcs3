class Song:
    def __init__(self, title: str, artist: str, writer: str, duration: int):
        # Public attr.
        self.title = title
        self.artist = artist
        self.writer = writer

        # Private attr (encapsulated)
        self.__duration = duration
        self.__current_position = 0
    
    def get_duration(self):
        return self.__duration

    def get_current_position(self):
        return self.__current_position
    
    def forward(self, seconds: int):
        if seconds > 0:
            self.__current_position += seconds
            if self.__current_position > self.__duration:
                self.__current_position = self.__duration

    def previous(self, seconds: int):
        if seconds > 0:
            self.__current_position -= seconds
            if self.__current_position < 0:
                self.__current_position = 0

    def start(self):
        print(f"Now playing: '{self.title}' by {self.artist}")

    def pause(self):
        print(f"Paused: '{self.title}' at {self.__current_position}s")


class Album:
    def __init__(self, title: str, artist: str, release_year: int):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.songs = []  # List storing references to Song objects

    def add_song(self, song: Song):
        self.songs.append(song)
        print(f"Added track: '{song.title}' to album '{self.title}'")

    def display_album(self):
        print(f"\n--- Album Details ---")
        print(f"Album: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Release Year: {self.release_year}")
        print("Tracklist:")
        
        if not self.songs:
            print("  (No tracks added yet)")
            return

        for idx, song in enumerate(self.songs, start=1):
            print(f"  Track {idx}: '{song.title}' | Writer: {song.writer} | Duration: {song.get_duration()}s")

    def get_total_duration(self):
        return sum(song.get_duration() for song in self.songs)

print("=== BEFORE RELATIONSHIP ===")

album1 = Album("Queen", "Queen", 1973)

song1 = Song("Keep Yourself Alive", "Queen", "Brian May", 225)
song2 = Song("Doing All Right", "Queen", "Brian May-Tim Staffell", 250)
song3 = Song("Great King Rat", "Queen", "Freddie Mercury", 341)

print(f"Album Created: {album1.title} (Track Count: {len(album1.songs)})")
print(f"Song 1 Created: '{song1.title}'")
print(f"Song 2 Created: '{song2.title}'")
print(f"Song 3 Created: '{song3.title}'")

print("\n=== BUILDING RELATIONSHIP ===")
album1.add_song(song1)
album1.add_song(song2)
album1.add_song(song3)


print("\n=== AFTER RELATIONSHIP ===")
album1.display_album()
print(f"\nTotal Album Duration: {album1.get_total_duration()} seconds")