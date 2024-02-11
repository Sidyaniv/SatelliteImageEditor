import requests

from datetime import datetime
from src.enums.global_enums import WrongStatusCode, GlobalErrorMessages

class Image():
    """Класс для полноценной работы с изображением
    """
    def __init__(self, long, lat, date):
        self.long = long
        self.lat = lat
        self.date = date

    def get_image(self):
        """Функция отправляет на сервер запрос, в ответ получая спутниковый снимок

        Returns:
            image: спутниковый снимок
        """

        url = f"http://127.0.0.1:5000/v5000/earth/imagery/?lon={self.long}&lat={self.lat}&date={self.date}&dim=0.32"
        image = requests.get(url)
        return image


    def download_image(self, filename):
        """Загрузка спутникового снимкка на локальную машину

        Args:
            filename (str): имя файла с изображением

        Raises:
            WrongStatusCode: ошибка ответа сервера 

        Returns:
            bytes: загруженный спутниковый снимок 
        """

        image = Image.get_image(self)
        
        try:
            if image.status_code == 200:
                with open(f"{filename}.jpeg", 'wb') as f:
                    f.write(image.content)
            else:
                raise WrongStatusCode(image.status_code)
            
        except FileNotFoundError:
            print(GlobalErrorMessages.FILE_NOT_FOUND)

        except IOError:
            print(GlobalErrorMessages.READ_FILE_ERROR)
            
        return image.content


def str_to_date(string):
    """Перевод даты в формате YYYY-MM-DD из строки в формат date

    Args:
        string (str): дата. представленная в строковом формате 

    Returns:
        date: дата, представленная в формате date
    """
    date = datetime.strptime(string, "%Y-%m-%d")
    return date

# dataset = Image(106.21, 29.67, '2018-07-01')
# image = dataset.download_image('image')

