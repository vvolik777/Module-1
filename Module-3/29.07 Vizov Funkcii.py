def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in recipient or not (
            recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net")) or \
            "@" not in sender or not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(
        ".net")):  # проверка корректности e-mail для обоих адресов
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:  # если получатель и отправитель совпадают
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":  # если отправитель - это значение по умолчанию
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:  # если отправитель не стандартный
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


# вызоваем функции с различными данными:
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
