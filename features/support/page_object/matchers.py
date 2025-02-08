import re

from features.support.page_object.pages import Index, Schedule, Catalog, Support

matcher_pages = {
    "index": [re.compile('^Главная|Индекс$')],
    "schedule": [re.compile('^Расписание$')],
    "catalog": [re.compile('^Релизы$')],
    "support": [re.compile('^Поддержать проект|Поддержка$')]
}

matcher_loaders = {
    "index": Index,
    "schedule": Schedule,
    "catalog": Catalog,
    "support": Support
}
