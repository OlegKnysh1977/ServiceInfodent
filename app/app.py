import os

from fastapi import FastAPI
from fastapi import Header
from fastapi.responses import FileResponse
import uvicorn

from firebird.driver import connect

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

@app.get("/v1/filials", status_code = 200)
async def getTreats(
    token: str = Header('')
):
    filials = []

    with connect(database = INFODENT_CENTRAL["database"], user=INFODENT_CENTRAL["user"], password=INFODENT_CENTRAL["password"], charset="utf8") as con:
        cur = con.cursor()
        str_query = "select FILID, FULLNAME from FILIALS"
        cur.execute(str_query)
        for fileid, fullname in cur:
            filials.append(
                {
                    "id": fileid,
                    "descr": fullname
                }
            )

    return filials

if __name__ == "__main__":
    uvicorn.run(app, port=SERVICE_INFODENT_PORT)