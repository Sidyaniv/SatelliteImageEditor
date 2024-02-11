import requests

from src.enums.global_enums import WrongStatusCode,GlobalErrorMessages


class Image():

    def __init__(self, long, lat, date):
        self.long = long
        self.lat = lat
        self.date = date

    def get_image(self):

        url = f"http://127.0.0.1:5000/v5000/earth/imagery/?lon={self.long}&lat={self.lat}&date={self.date}&dim=0.32"
        # info_json = f"http://127.0.0.1:5000/v5000/earth/assets/?lon={self.long}&lat={self.lat}&begin=2014-07-01&end=2014-09-01&dim=0.32"
        # image2 = requests.get(info_json)
        image = requests.get(url)
        return image
    

    def download_image(self, filename):

        image = Image.get_image(self)
        
        try:
            if image.status_code == 200:
                with open(f"{filename}".jpeg, 'wb') as f:
                    f.write(image.content)
            else:
                raise WrongStatusCode(image.status_code)
        except FileNotFoundError:
            print(GlobalErrorMessages.FILE_NOT_FOUND)
        except IOError:
            print(GlobalErrorMessages.READ_FILE_ERROR)


dataset = Image(120.21, 70.67, '2010-07-01')
image = dataset.download_image('image')


# requests.get('http://127.0.0.1:5000/v5000/imagery/?lon=61.128185&lat=-129.597130&date= 2018-11-20')
# simage = get_image(61.128185, -129.597130, 2018-11-20)
# sprint(type(image))

# пример корректного запроса на сервер 
# http://127.0.0.1:5000/v5000/earth/imagery/?lon=-95.21&lat=29.67&date=2018-07-01&dim=0.32

