import hashlib  # для хэширования пароля
import time  # модуль для паузы при воспроизведении видео

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя
        self.password = self.hash_password(password)  # хэшированный пароль
        self.age = age  # возраст

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() # хэшируем используя алгоритм sha256

    def __str__(self):
        return self.nickname  # возвращаем только никнейм


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # название видео
        self.duration = duration  # продолжительность видео в секундах
        self.time_now = 0  # секунда остановки, изначально 0
        self.adult_mode = adult_mode  # ограничение по возрасту (по умолчанию False)


class UrTube:
    def __init__(self):
        self.users = []  # список пользователей
        self.videos = []  # список видео
        self.current_user = None  # текущий пользователь

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # вход в аккаунт сразу после регистрации

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print("Неправильное имя пользователя или пароль")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы")
            self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        result = [video.title for video in self.videos if search_term.lower() in video.title.lower()]
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_to_watch = None
        for video in self.videos:
            if video.title == title:
                video_to_watch = video
                break

        if video_to_watch is None:
            return  # убираем вывод "видео не найдено"

        if video_to_watch.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for second in range(video_to_watch.time_now, video_to_watch.duration):
            print(f"{second + 1}", end=' ', flush=True)  # выводим секунды в одну строку
            time.sleep(1)  # пауза в 1 секунду
        print("Конец видео")
        video_to_watch.time_now = 0  # после просмотра сбрасываем время



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

# проверяем поиск
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# проверяем вход пользователя и возраст
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# проверяем повторную регу
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


ur.watch_video('Лучший язык программирования 2024 года!')
