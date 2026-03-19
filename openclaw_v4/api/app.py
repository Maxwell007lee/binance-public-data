from fastapi import FastAPI

from openclaw_v4.api.routes import router


def create_app() -> FastAPI:
    app = FastAPI(title='OpenClaw V4.0 Phase 1 Control Plane')
    app.include_router(router)
    return app


app = create_app()
