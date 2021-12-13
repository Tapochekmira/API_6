# Публикация комиксов в сообщество Вконтакте
- `main.py` скачивает случайный комикс автоара [xkcd](https://xkcd.com/), публикует в группу в [Вк](vk.com). Удаляет скаченный комикс.

## Файл переменных окружения .env

- `VK_ACCESS_TOKEN` ключ доступа к VK, получить можно [на оф. сайте Вконтакте](https://vk.com/dev/implicit_flow_user). Необходимы следующие права: `photos`, `groups`, `wall` и `offline`.
- `VK_GROUP_ID` идентификатор сообщества, посмотреть можно [здесь](https://regvk.com/id/).

## Установка

### Подготовка скрипта

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Запуск

```
python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).