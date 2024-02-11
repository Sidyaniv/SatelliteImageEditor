from enum import Enum

class GlobalErrorMessages():

    def __init__(self) -> None:
        pass

    WRONG_STATUS_CODE = "Ответ от сервера неверный / не получен."
    FILE_NOT_FOUND = "Файл не найден"
    READ_FILE_ERROR = "Ошибка при чтении файла"

class WrongStatusCode(Exception):

    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"{GlobalErrorMessages.WRONG_STATUS_CODE} Статус код: {status_code}")
    