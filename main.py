from texttospeechconverter import TextToSpeechConverter


def read_file_lines(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines


if __name__ == '__main__':
    file_path = "words.txt"
    input_list = read_file_lines(file_path)
    delimiter = ":"
    output_filename = "output.mp3"
    languages = "en:ru"

    converter = TextToSpeechConverter(input_list, delimiter, languages)
    converter.process_text_list()
    converter.create_audio_file(output_filename)
