# Конвертер текста в речь

Этот модуль предоставляет возможность конвертировать текст в речь с использованием библиотеки `gtts`. Он позволяет преобразовывать текст в аудиофайлы.

## Установка

Для использования этого модуля вам необходимо установить библиотеку `gtts`. Вы можете установить ее с помощью следующей команды:

```shell
pip install gtts
```

Для создания аудиофайлов необходимо установить `ffmpeg`. Следуйте инструкциям ниже для установки `ffmpeg` на различных операционных системах:


### Windows

Перейдите на официальный веб-сайт [FFmpeg](https://ffmpeg.org/).
На странице загрузки выберите "Get the latest version of FFmpeg" (получить последнюю версию FFmpeg).
Скачайте статическую сборку FFmpeg для вашей версии Windows.
Распакуйте архив в удобное место на вашем компьютере.
Добавьте путь к папке с исполняемыми файлами FFmpeg в переменную среды PATH. Это позволит вам использовать `ffmpeg` из командной строки.

### macOS
Установите Homebrew, если вы еще не установили его. Подробные инструкции можно найти на официальном веб-сайте Homebrew: Homebrew
Откройте Terminal и выполните следующую команду для установки ffmpeg с помощью Homebrew:

```shell
brew install ffmpeg
```

### Linux (Ubuntu)
Откройте Terminal и выполните следующие команды для установки `ffmpeg`:

```shell
sudo apt update
sudo apt install ffmpeg
```
#### Проверка установки

Чтобы убедиться, что ffmpeg правильно установлен, выполните следующую команду в командной строке:

```shell
ffmpeg -version
```

Если у вас появляется информация о версии ffmpeg, значит, установка прошла успешно.


## Использование

Вот пример использования класса `TextToSpeechConverter`:

```python
from texttospeechconverter import TextToSpeechConverter

if __name__ == '__main__':
    input_list = ["Hello:привет", "world:мир"]
    delimiter = ":"
    output_filename = "output.mp3"
    languages = "en:ru"

    converter = TextToSpeechConverter(input_list, delimiter, languages)
    converter.process_text_list()
    converter.create_audio_file(output_filename)
