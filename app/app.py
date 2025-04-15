# import uvicorn
# from fastapi import FastAPI, Response, Header, status
# from fastapi.responses import JSONResponse, FileResponse
# from datetime import datetime

# from InfodentTreats import InfodentTreats
# from InfodentTreatsBetween import InfodentTreatsBetween
# from InfodentCustomerRepresentatives import InfodentCustomerRepresentatives

# from firebird.driver import connect, driver_config

# from config import RABBIT_MQ_HOST
# from config import RABBIT_MQ_PORT
# from config import RABBIT_MQ_VIRTUAL_HOST
# from config import RABBIT_MQ_VIRTUAL_EXCHANGE
# from config import RABBIT_MQ_LOGIN
# from config import RABBIT_MQ_PASSWORD
# from config import CENTRAL_FIREBIRD_SERVER
# from config import CENTRAL_FIREBIRD_SERVER_NAME
# from config import CENTRAL_FIREBIRD_DB
# from config import CENTRAL_FIREBIRD_DB_NAME

# from config import LIST_OF_TOKEN

# if driver_config.get_server(CENTRAL_FIREBIRD_SERVER_NAME) is None:
#     driver_config.register_server(CENTRAL_FIREBIRD_SERVER_NAME, CENTRAL_FIREBIRD_SERVER)

# if driver_config.get_database(CENTRAL_FIREBIRD_DB_NAME) is None:
#     driver_config.register_database(CENTRAL_FIREBIRD_DB_NAME, CENTRAL_FIREBIRD_DB)

# app = FastAPI()


# # cache = {"Treats":{}, "TreatsBetween":}

# @app.get("/")
# async def root():
#     return FileResponse("public/index.html")


# @app.put("/v1/Treats", status_code=200)
# async def getTreats(
#         date1: str | None = None,
#         date2: str | None = None,
#         routing_key: str | None = None,
#         token: str = Header('')
# ):
#     if not token in LIST_OF_TOKEN:
#         return Response(status_code=status.HTTP_401_UNAUTHORIZED)

#     if date1 == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть заполнен."}
#         )

#     try:
#         date1_as_date = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
#     except ValueError as message:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть в формате 'YYYY-MM-DD HH:MM:SS'."}
#         )

#     if date2 == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date2' должен быть заполнен."}
#         )

#     try:
#         date2_as_date = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
#     except ValueError as message:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date2' должен быть в формате 'YYYY-MM-DD HH:MM:SS'."}
#         )

#     if date2_as_date < date1_as_date:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть меньше или равен параметру 'date2'."}
#         )

#     if routing_key == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'routing_key' пустой."}
#         )

#     treats = InfodentTreats()
#     treats.run(routing_key, date1_as_date, date2_as_date)

#     return {"message": 'Success'}


# @app.put("/v1/TreatsBetween", status_code=200)
# async def getTreatsBetween(
#         date1: str | None = None,
#         date2: str | None = None,
#         routing_key: str | None = None,
#         token: str = Header('')
# ):
#     if not token in LIST_OF_TOKEN:
#         return Response(status_code=status.HTTP_401_UNAUTHORIZED)

#     if date1 == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть заполнен."}
#         )

#     try:
#         date1_as_date = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
#     except ValueError as message:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть в формате 'YYYY-MM-DD HH:MM:SS'."}
#         )

#     if date2 == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date2' должен быть заполнен."}
#         )

#     try:
#         date2_as_date = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
#     except ValueError as message:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date2' должен быть в формате 'YYYY-MM-DD HH:MM:SS'."}
#         )

#     if date2_as_date < date1_as_date:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть меньше или равен параметру 'date2'."}
#         )

#     if routing_key == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'routing_key' пустой."}
#         )

#     treats = InfodentTreatsBetween()
#     treats.run(routing_key, date1_as_date, date2_as_date)

#     return {"message": 'Success'}


# @app.put("/v1/CustomerRepresentatives", status_code=200)
# async def getCustomerRepresentatives(
#         date1: str | None = None,
#         date2: str | None = None,
#         routing_key: str | None = None,
#         token: str = Header('')
# ):
#     if not token in LIST_OF_TOKEN:
#         return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED)

#     if date1 == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть заполнен."}
#         )

#     try:
#         date1_as_date = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
#     except ValueError as message:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть в формате 'YYYY-MM-DD HH:MM:SS'."}
#         )

#     if date2 == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date2' должен быть заполнен."}
#         )

#     try:
#         date2_as_date = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
#     except ValueError as message:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date2' должен быть в формате 'YYYY-MM-DD HH:MM:SS'."}
#         )

#     if date2_as_date < date1_as_date:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'date1' должен быть меньше или равен параметру 'date2'."}
#         )

#     if routing_key == None:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": "Параметр 'routing_key' пустой."}
#         )

#     customRepresentatives = InfodentCustomerRepresentatives()
#     customRepresentatives.run(routing_key, date1_as_date, date2_as_date)

#     return {"message": 'Success'}


# if __name__ == "__main__":
#     uvicorn.run(app, port=8080)