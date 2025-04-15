from fastapi import FastAPI
import uvicorn

def get_app() -> FastAPI:

    # Creap app instance with parameters defined in settings
    app = FastAPI()

    return app

app = get_app()

if __name__ == "__main__":
    uvicorn.run(app, port=8080)