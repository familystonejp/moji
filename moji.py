import moviepy.editor as mp
clip = mp.VideoFileClip("movie.mp4")
clip.audio.write_audiofile("audio.wav")