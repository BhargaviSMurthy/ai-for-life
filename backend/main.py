"""
Small local HTTP entrypoint.

Uses FastAPI for routing. It listens on the port defined by the PORT
environment variable (defaults to 8080).

Endpoints:
- GET / -> plain text welcome
- GET /health -> JSON status
- POST /predict -> echoes JSON body (placeholder)
"""

import os
import sys
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from routes.financial_plan import router as financial_router

app = FastAPI()

# Include your route
app.include_router(financial_router, prefix="/api")

# --- Basic routes ---
app.get("/", response_class=PlainTextResponse)
async def root():
    return "ai-for-life backend - running\n"

app.get("/health")
async def health():
    return {"status": "ok", "service": "ai-for-life"}

app.post("/predict")
async def predict(request: Request):
    try:
        payload = await request.json()
    except Exception:
        return JSONResponse(status_code=400, content={"error": "invalid json"})

    # Placeholder: echo back payload under `prediction`
    return {"prediction": None, "input": payload}

# --- Run locally ---
def run(port: int = None):
    import uvicorn
    port = (
        port
        or (int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else None)
        or int(os.environ.get("PORT", "8080"))
    )
    host = "0.0.0.0"
    print(f"Starting ai-for-life backend on http://{host}:{port} (Ctrl-C to stop)")
    uvicorn.run("main:app", host=host, port=port, reload=True)

if __name__ == "__main__":
    run()
