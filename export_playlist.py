from yandex_music import Client, Playlist
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен и UUID плейлиста из переменных окружения
token = os.getenv("TOKEN")  # Опционально, только для приватных плейлистов
playlist_uuid = os.getenv("PLAYLIST_UUID")

if not playlist_uuid:
    print("Ошибка: Установите PLAYLIST_UUID в файле .env")
    exit(1)

# Инициализация клиента (с токеном или без)
client = Client(token).init() if token else Client().init()

# Используем внутренний request клиента для API запроса
url = f"{client.base_url}/playlist/{playlist_uuid}"
result = client._request.get(url)
playlist = Playlist.de_json(result.get('result') or result, client)

if playlist:
    print(f"=== {playlist.title} ===")
    print(f"Владелец: {playlist.owner.name if playlist.owner else 'Неизвестен'}")
    print(f"Количество треков: {playlist.track_count}\n")
    
    # Выводим треки
    if playlist.tracks:
        for i, track_short in enumerate(playlist.tracks, 1):
            track = track_short.track
            if track:
                artists = ", ".join([artist.name for artist in track.artists])
                print(f"{i}. {artists} - {track.title}")
    
    # Сохранение в файл
    with open(f"{playlist_uuid}.txt", "w", encoding="utf-8") as f:
        f.write(f"{playlist.title}\n")
        f.write(f"Владелец: {playlist.owner.name if playlist.owner else 'Неизвестен'}\n")
        f.write(f"Треков: {playlist.track_count}\n\n")
        
        tracks_to_save = playlist.tracks or []
        for track_short in tracks_to_save:
            track = track_short.track
            if track:
                artists = ", ".join([artist.name for artist in track.artists])
                f.write(f"{artists} - {track.title}\n")
    
    print(f"\n✓ Плейлист сохранен в файл {playlist_uuid}.txt")
else:
    print("Не удалось получить плейлист")
