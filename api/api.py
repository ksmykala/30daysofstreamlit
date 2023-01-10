import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from src.repository import AirportsRepository
from fastapi.responses import JSONResponse

api = FastAPI(docs_url=None)
api.mount('/img', StaticFiles(directory='img'), name='img')


@api.get('/')
async def root():
    return {'msg': 'Hi!'}


@api.get('/data/{repository_id}')
async def get_data(repository_id):
    if repository_id == 'airports':
        airport_data = AirportsRepository().get_data()
        return JSONResponse(content=airport_data.to_json())

    return None


@api.get('/docs', include_in_schema=False)
async def swagger_ui_html():
    print('Im here!')
    return get_swagger_ui_html(
        openapi_url='/openapi.json',
        title='Docs - API - 30 Days of Streamlit',
        swagger_favicon_url='/img/favicon.ico'
    )


if __name__ == '__main__':
    uvicorn.run(api, host='0.0.0.0', port=8000)
