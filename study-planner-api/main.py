import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Study Planner API")


@app.get("/")
def home() -> dict[str, str]:
    return {
        "project": "Study Planner API",
        "message": os.getenv("APP_MESSAGE", "Plan a focused study session"),
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "framework": "fastapi"}


@app.get("/today")
def today() -> dict[str, object]:
    return {
        "tasks": [
            {"subject": "Networking", "task": "Review subnetting", "minutes": 25},
            {"subject": "Programming", "task": "Practice functions", "minutes": 30},
            {"subject": "Databases", "task": "Revise SQL joins", "minutes": 20},
        ]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
