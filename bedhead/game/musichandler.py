import arcade
import time
from game import constants


class MusicHandler():
    def __init__(self) -> None:
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None

    def advance_song(self):
        """ Advance our pointer to the next song. This does NOT start the song. """
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0

    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        if self.music:
            self.music.stop(self.current_player)
        # Play the next song
        self.music = arcade.Sound(
            self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(constants.MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)

    def play_song_looped(self):
        """ Play the song. """
        # Stop what is currently playing.
        # if self.music:
        #     self.music.stop(self.current_player)
        # Play the next song
        self.music = arcade.Sound(
            self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(
            constants.MUSIC_VOLUME, loop=True)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)

    def add_song_list(self, song_list):
        self.music_list = song_list

    def clear_queue(self):
        self.music_list = []
