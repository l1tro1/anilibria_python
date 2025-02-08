# encoding: UTF-8
# language: ru

Функция: Проверка описания

  Сценарий: Проверка описания Расписания
    Дано я открываю браузер на странице "Расписание"
    И я должен увидеть в разделе breadcrumbs путь "Расписание"
    И я должен увидеть в описании страницы заголовок
    """
    Расписание выхода новых эпизодов
    """
    И я должен увидеть в описании страницы тело
    """
    Следите за расписанием выхода новых эпизодов на нашем сайте
    Будьте в курсе последних обновлений и не пропустите ни одного нового эпизода вашего любимого релиза!
    """

  Сценарий: Проверка описания Релизы
    Дано я открываю браузер на странице "Релизы"
    И я должен увидеть в разделе breadcrumbs путь "Каталог релизов"
    И я должен увидеть в описании страницы заголовок
    """
    Каталог релизов
    """
    И я должен увидеть в описании страницы тело
    """
    Самые новые и свежие эпизоды в любимой озвучке
    """

  Сценарий: Проверка описания Поддержка
    Дано я открываю браузер на странице "Поддержка"
    И я должен увидеть в разделе breadcrumbs путь "Поддержка проекта"
    И я должен увидеть в описании страницы заголовок
    """
    Поддержка
    """
    И я должен увидеть в описании страницы тело
    """
    Друзья, мы нуждаемся в вашей поддержке!
    Поддержите проект AniLibria удобным для вас способом, чтобы мы и дальше могли радовать вас своей озвучкой так же круто и эффективно!
    """