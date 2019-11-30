import moviepy.editor as mp
import os.path
import subprocess


video_path = os.path.join(os.path.dirname(__file__), "video")
audio_path = os.path.join(os.path.dirname(__file__), "audio")
output_path = os.path.join(os.path.dirname(__file__), "output")

query = False

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
    command = "ffmpeg -y -i {video} -ss 0 -i {audio} -map 1:a:0 -map 0:v:0 -async 1 -shortest {output}"

    for clip in os.listdir(video_path):
        for audio in os.listdir(audio_path):
            if not clip == '.DS_Store' and not audio == '.DS_Store':
                command_str = command.format(
                    video=f'\"{video_path + os.sep + clip}\"',
                    audio=f'\"{audio_path + os.sep + audio}\"',
                    output='\"'+output_path + os.sep + clip.split(".")[0] + "+" + audio.split(".")[0] + ".mp4\"")
                os.system(command_str)
if __name__ == '__main__':
    # combine_all_moviepy()
    combine_all_ffmpeg()
    pass
