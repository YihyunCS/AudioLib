from sclib import SoundcloudAPI, Track, Playlist

# do not pass a Soundcloud client ID that did not come from this library, but you can save a client_id that this lib found and reuse it
api = SoundcloudAPI()

URL = input("Enter Soundcloud URL: ")

track = api.resolve(URL)

assert type(track) is Track

filename = f'./playlist/{track.artist} - {track.title}.mp3'

with open(filename, 'wb+') as file:
    track.write_mp3_to(file)
