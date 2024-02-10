import requests

from src.enums.global_enums import WrongStatusCode

class Image():

    def __init__(self, long, lat, date):
        self.long = long
        self.lat = lat
        self.date = date

    def get_image(self):

        url = f'http://127.0.0.1:5000/v5000/earth/imagery/?lon={self.long}&lat={self.lat}&date={self.date}&dim=0.32'
        image = requests.get(url)
        return image

    def download_image(self, filename):

        image = Image.get_image(self)
        
        if not ('iterator' in locals()):
            iterator = 1
        
        
        if image.status_code == 200:
            with open(f"images/{filename}_{iterator}.png", 'wb') as f:
                f.write(image.content)
            iterator += 1
        else:
            raise WrongStatusCode(image.status_code)


dataset = Image(99.21, 29.67, '2018-07-01')
image = dataset.download_image('image')



# requests.get('http://127.0.0.1:5000/v5000/imagery/?lon=61.128185&lat=-129.597130&date= 2018-11-20')
# simage = get_image(61.128185, -129.597130, 2018-11-20)
# sprint(type(image))

# пример корректного запроса на сервер 
# http://127.0.0.1:5000/v5000/earth/imagery/?lon=-95.21&lat=29.67&date=2018-07-01&dim=0.32

