from fastapi import FastAPI
from api.endpoints import detect_router
import uvicorn

from services.tgbot_service import *

#Создаем приложение
app = FastAPI(
    title="Detect helmets",
    description="Server application for detect helmets in heads.",
    version="1.0.0"
)

#Добавляем эндпоинты    
app.include_router(detect_router.router)

#Тестовый
@app.get("/")
async def root():
    return {"message": "Helmet Detection API is running!"}


def main():
    #Запуск бота в отдельном потоке
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, bot_service_run)
    
    #Запуск приложения FAST API
    uvicorn.run(app, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    asyncio.run(main())