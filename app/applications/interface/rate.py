import requests
from django.core.cache import cache


class RateInterface:
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def get_rub_rate(self) -> float:
        # получение кураса из кэша
        rub_rate = cache.get('rub_rate')

        if rub_rate is None:
            valute_dict = requests.get(self.url).json()
            rub_rate = valute_dict.get('Valute').get('USD').get('Value')

            # сохранение курса в кэш
            cache.set('rub_rate', rub_rate, 60 * 60)

        return float(rub_rate)
