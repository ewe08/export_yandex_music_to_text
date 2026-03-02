# Export Yandex Music to Text

Экспорт плейлистов из Яндекс.Музыки в текстовый файл.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

1. Создайте файл `.env`:
```bash
PLAYLIST_UUID=your_playlist_uuid_here
```

![UUID в адресной строке](images/image.png)

UUID плейлиста берется из URL: `https://music.yandex.ru/playlists/{UUID}`

2. Для приватных плейлистов добавьте токен ([получить](https://oauth.yandex.ru/)) или [тут](https://yandex-music.readthedocs.io/en/main/token.html):
```bash
TOKEN=your_token_here
PLAYLIST_UUID=your_playlist_uuid_here
```

3. Запустите скрипт:
```bash
python export_playlist.py
```

Результат сохранится в файл `{UUID}.txt`

## Перенос в другие сервисы

Для переноса плейлистов из Яндекс.Музыки в Spotify, Apple Music, YouTube Music и другие сервисы используйте [TuneMyMusic](https://www.tunemymusic.com/) — бесплатный онлайн-сервис для миграции плейлистов между музыкальными платформами.

![TuneMyMusic](images/image-1.png)