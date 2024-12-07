from fastapi import UploadFile
import torch
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import json
from ultralytics import YOLO

device = "cpu"
if torch.cuda.is_available():
    device = "cuda"

#Инициализация модели
path2Yolo11model = 'nn_models/yolo11l.pt'
# path2Yolo11model = 'app/nn_models/weights/best.pt'
model = YOLO(path2Yolo11model) #Загрузка модели
model.to(device)


#Обнаружение объектов
def detectImages(img_tensor: np.array):
    # Если img_tensor является тензором PyTorch, переводим его в NumPy
    if isinstance(img_tensor, torch.Tensor):
        img_tensor = img_tensor.permute(1, 2, 0).cpu().numpy()

    img_bgr = cv2.cvtColor(img_tensor, cv2.COLOR_RGB2BGR)
    
    # ---------- Предсказание ----------
    results = model(img_bgr)  # Получаем результаты
    return results