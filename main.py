import os

import speech_recognition as sr
import moviepy.editor as mp

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def clip_to_text(name1):
    vid_name = f'{name1}.mp4'
    print(vid_name)
    clip = mp.VideoFileClip(rf"{vid_name}")  # Use moviepy.editor to open the video file and extract its audio track.
    clip.audio.write_audiofile(r"converted_mp3.wav")  # Save the audio track as a WAV file.

    r = sr.Recognizer()
    audio = sr.AudioFile(r"converted_mp3.wav")
    with audio as source:
        audio_file = r.record(source)  # read the audio data from the AudioFile object

    result = r.recognize_google(audio_file, language='en-US',
                                show_all=True)  # perform speech recognition on the audio data

    with open('recog.txt', mode='w') as file:
        file.write("speech recognized")
        file.write("\n")
        file.write(str(result))
        print("Now the file is ready")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input("what is the Video name?:")
    clip_to_text(name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
