import numpy as np
from PIL import Image
from io import BytesIO


# Преобразование NumPy массива в байты изображения
def numpy_image_to_bytes(array):
    # Убедимся, что массив в формате uint8 (для изображений)
    if array.dtype != np.uint8:
        array = (array * 255).astype(np.uint8)  # Нормализация для float данных
    image = Image.fromarray(array)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def notificationSend(mode : bool, pick, client_uuid):
    if mode:
        print("NOTIFICATION")                   
        #Отправляем уведомления
        bytes_array = numpy_image_to_bytes(pick)
        return bytes_array
    return None