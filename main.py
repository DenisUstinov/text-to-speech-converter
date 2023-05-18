from texttospeechconverter import TextToSpeechConverter

if __name__ == '__main__':
    input_list = ["Hello:привет", "world:мир"]
    delimiter = ":"
    output_filename = "output.mp3"
    languages = "en:ru"

    converter = TextToSpeechConverter(input_list, delimiter, languages)
    converter.process_text_list()
    converter.create_audio_file(output_filename)
