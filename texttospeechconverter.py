import gtts
import os
import subprocess


class TextToSpeechConverter:
    def __init__(self, text_list, delimiter, languages):
        self.text_list = text_list
        self.delimiter = delimiter
        self.languages = languages
        self.audio_list = []

    def translate_to_speech(self, text, language):
        tts = gtts.gTTS(text, lang=language)
        audio_filename = f"{text.replace(' ', '_')}.mp3"
        audio_filepath = os.path.join('sounds', audio_filename)
        tts.save(audio_filepath)
        self.audio_list.append(audio_filepath)

    def process_text_list(self):
        parts_languages = self.languages.split(self.delimiter)
        for text in self.text_list:
            parts_string = text.split(self.delimiter)
            for text, language in zip(parts_string, parts_languages):
                self.translate_to_speech(text, language)

    def create_audio_file(self, output_filename):
        command = ["ffmpeg", "-i", "concat:" + "|".join(self.audio_list), "-c", "copy", output_filename]
        subprocess.run(command)