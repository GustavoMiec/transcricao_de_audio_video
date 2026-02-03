from moviepy.video.io.VideoFileClip import VideoFileClip
import speech_recognition as sr
import os

def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    
def transcribe_audio(audio_path, text_output_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print('trascrição: ', text)
            
            with open(text_output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition não conseguiu entender o áudio")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço Google Speech Recognition; {e}".format(e))
            
            
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(script_dir, 'video.mp4')
    audio_path = os.path.join(script_dir, 'audio.wav')
    text_output_path = os.path.join(script_dir, 'transcription.txt')
    
    extract_audio_from_video(video_path, audio_path)
    transcribe_audio(audio_path, text_output_path)
    
if __name__ == "__main__":
    main()          