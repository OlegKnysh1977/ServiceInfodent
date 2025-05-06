import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

from config import WORKINGPATH

from config import INFODENT_CENTRAL
from config import INFODENT_VO
from config import INFODENT_SAVUSHKINA
from config import INFODENT_KUPCHINO
from config import INFODENT_VODETSTVO
from config import INFODENT_BALTPERL
from config import INFODENT_PARNAS

from config import RABBIT
from config import RABBIT_VIRTUAL_HOST
from config import RABBIT_EXCHANGE
from config import RABBIT_ROUTING_KEY

from config import LIST_OF_TOKENS

from config import SERVICE_INFODENT_PORT


def get_app() -> FastAPI:

    # Creap app instance with parameters defined in settings
    app = FastAPI()

    return app

app = get_app()

@app.get("/")
async def root():
    print(WORKINGPATH + "\\public\\index.html")
    return FileResponse(WORKINGPATH + "\\public\\index.html")


if __name__ == "__main__":
    uvicorn.run(app, port=SERVICE_INFODENT_PORT)