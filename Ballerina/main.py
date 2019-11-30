import moviepy.editor as mp
import os.path
import glob
from random import choice


video_path = os.path.join(os.path.dirname(__file__), "video")
audio_path = os.path.join(os.path.dirname(__file__), "audio")
output_path = os.path.join(os.path.dirname(__file__), "output")

query = False

command = "ffmpeg -y -i {video} -ss 0 -i {audio} -map 1:a:0 -map 0:v:0 -async 1 -shortest {output}"

def combine_all_moviepy():
    for clip in os.listdir(video_path):
        for audio in os.listdir(audio_path):
            if not clip == '.DS_Store' and not audio == '.DS_Store':
                video = mp.VideoFileClip(video_path + os.sep + clip)
                music = mp.AudioFileClip(audio_path + os.sep + audio)
                music = music.set_duration(video.duration)

                video = video.set_audio(music)
                video.write_videofile(
                    output_path + os.sep + clip.split(".")[0] + "+" + audio.split(".")[0] + ".mp4",
                    audio_codec="aac"
                )

def combine_all_ffmpeg():
    for clip in os.listdir(video_path):
        for audio in os.listdir(audio_path):
            if not clip == '.DS_Store' and not audio == '.DS_Store':
                os.system(
                    command.format(
                        video=f'\"{video_path + os.sep + clip}\"',
                        audio=f'\"{audio_path + os.sep + audio}\"',
                        output='\"'+output_path + os.sep + clip.split(".")[0] + "+" + audio.split(".")[0] + ".mp4\""
                    )
                )

def get_tracks():
    return [track for track in glob.glob("/Users/zackamiton/Music/iTunes/iTunes Media/Music/**/*.mp3", recursive=True)]

def make_random_video():
    video = choice([path for path in os.listdir(video_path) if path != '.DS_Store'])
    audio = choice(get_tracks())
    os.system(
        command.format(
            video=f'\"{video_path + os.sep + video}\"',
            audio=f'\"{audio}\"',
            output=f'\"{output_path+os.sep+video.split(".")[0]+ " x " + audio.split("/")[-1]}.mp4\"'
        )
    )



if __name__ == '__main__':
    for i in range(50): make_random_video()
    pass
