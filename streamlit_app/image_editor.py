import io

from PIL import ImageEnhance, Image
from class_streamlit import Streamlit 
from textfile_app import *

stream = Streamlit()


class Editor():

    def __init__(self, image, color, contrast, brightness) -> None:
        # with open('image.jpeg', 'rb') as f:
            # image_data = f.read()

        img = Image.open(io.BytesIO(image))
        self.image = img.convert("RGB")

        # self.image = Image.open(image_data)
        self.color = color
        self.contrast = contrast
        self.brightness = brightness

    def editing(self):
        """Изменение насыщенности

        Args:
            var (float): число в пределах [0,2]
        """

        try:
            # Изменяем насыщенность и сохраняем результат
            img_col = ImageEnhance.Color(self.image).enhance(self.color)
            img_col.save(f'color_{self.color}.jpeg')

            # Открываем изображение с изменённой насыщенностью
            img_col = Image.open(f'color_{self.color}.jpeg')

            # Изменяем контраст и сохраняем результат
            img_col_con = ImageEnhance.Contrast(img_col).enhance(self.contrast)
            img_col_con.save(f'color_{self.contrast}.jpeg')

            # Открываем изображение с изменёнными насыщенностью и контрастом
            img_col_con = Image.open(f'color_{self.contrast}.jpeg')
            
            # Изменяем контраст и сохраняем результат
            img_col_con_bri = ImageEnhance.ImageEnhance.Brightness(img_col_con).enhance(self.brightness)
            img_col_con_bri.save(f'color_{self.brightness}.jpeg')

            # Открываем полностью отредактированный снимок
            image_full_edit = Image.open(f'color_{self.brightness}.jpeg')

            # Сохраняю файл локально
            with open(f"color_{self.brightness}.jpeg", 'wb') as f:
                        f.write(image_full_edit)

            return  getattr(image_full_edit, 'image')
        

        except Exception as e:
            stream.make_error(error_edit)