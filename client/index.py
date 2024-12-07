import cv2
import asyncio
import websockets
from io import BytesIO
from PIL import Image
import numpy as np


def bytes_to_numpy_image(byte_data):
    buffer = BytesIO(byte_data)
    image = Image.open(buffer)
    return np.array(image)


async def connect_to_server():
    uri = "ws://127.0.0.1:5000/ws"  # Адрес WebSocket сервера
    async with websockets.connect(uri) as websocket:
        # Для захвата видео
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Не удалось захватить изображение.")
                break

            # Кодируем изображение в формат JPG
            _, img_encoded = cv2.imencode('.jpg', frame)
            img_bytes = img_encoded.tobytes()  # Преобразуем в байты

            # Отправляем изображение на сервер в бинарном формате
            await websocket.send(img_bytes)

            # Задержка перед отправкой следующего кадра
            await asyncio.sleep(0.3)  # Примерная задержка для 30 fps

            # # Ожидаем ответа от сервера
            # try:
            #     byte_data = await websocket.recv()  # Ожидаем данные от сервера
            #     array = bytes_to_numpy_image(byte_data)  # Преобразуем байты в изображение
            #     print("Полученные данные от сервера:", array)

            #     # Отображаем полученное изображение
            #     cv2.imshow("Received Image", array)
            #     cv2.waitKey(1)  # Задержка для обновления окна
            # except asyncio.TimeoutError:
            #     print("Нет ответа от сервера.")
            #     await asyncio.sleep(0.03)  # Даем серверу время на обработку

        cap.release()
        cv2.destroyAllWindows()

# Запуск клиента
asyncio.run(connect_to_server())
