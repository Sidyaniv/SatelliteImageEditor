import requests

from datetime import datetime
from src.enums.global_enums import WrongStatusCode, GlobalErrorMessages

class Image():

    def __init__(self, long, lat, date):
        self.long = long
        self.lat = lat
        self.date = date

    def get_image(self):

        url = f"http://127.0.0.1:5000/v5000/earth/imagery/?lon={self.long}&lat={self.lat}&date={self.date}&dim=0.32"
        image = requests.get(url)
        return image


    def download_image(self, filename):

        image = Image.get_image(self)
        
        try:
            if image.status_code == 200:
                with open(f"images/{filename}.png", 'wb') as f:
                    f.write(image.content)
            else:
                raise WrongStatusCode(image.status_code)
            
        except FileNotFoundError:
            print(GlobalErrorMessages.FILE_NOT_FOUND)

        except IOError:
            print(GlobalErrorMessages.READ_FILE_ERROR)
            
        return image.content


def str_to_date(string):
    date = datetime.strptime(string, "%Y-%m-%d")
    return date

dataset = Image(106.21, 29.67, '2018-07-01')
image = dataset.download_image('image')



# requests.get('http://127.0.0.1:5000/v5000/imagery/?lon=61.128185&lat=-129.597130&date= 2018-11-20')
# simage = get_image(61.128185, -129.597130, 2018-11-20)
# sprint(type(image))

# пример корректного запроса на сервер 
# http://127.0.0.1:5000/v5000/earth/imagery/?lon=-95.21&lat=29.67&date=2018-07-01&dim=0.32

