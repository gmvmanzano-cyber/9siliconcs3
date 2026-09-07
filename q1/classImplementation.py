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

song1 = Song("Bohemian Rhapsody", "Queen", "Freddie Mercury", 355)
song2 = Song("Care", "Conan Gray", "Conan Gray", 209)

print("--- BEFORE STATE ---")
print(f"Song 1: {song1.title} | Position: {song1.get_current_position()}s / {song1.get_duration()}s")
print(f"Song 2: {song2.title} | Position: {song2.get_current_position()}s / {song2.get_duration()}s")

print("\nExecuting: song1.forward(15)...\n")
song1.forward(15)

print("--- AFTER STATE ---")
print(f"Song 1: {song1.title} | Position: {song1.get_current_position()}s / {song1.get_duration()}s")
print(f"Song 2: {song2.title} | Position: {song2.get_current_position()}s / {song2.get_duration()}s")