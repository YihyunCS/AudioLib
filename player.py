import os
from pydub import AudioSegment
import simpleaudio as sa

def play_song(file_path):
    # Load the audio file
    song = AudioSegment.from_file(file_path)

    # Play the song
    play_obj = sa.play_buffer(song.raw_data,
                              num_channels=song.channels,
                              bytes_per_sample=song.sample_width,
                              sample_rate=song.frame_rate)
    play_obj.wait_done()

def play_playlist(directory='./playlist'):
    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            file_path = os.path.join(directory, filename)
            print(f'Playing: {filename}')
            play_song(file_path)

if __name__ == "__main__":
    play_playlist()
