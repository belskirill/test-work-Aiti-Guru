import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.orders import router as orders_router


app = FastAPI()
app.include_router(orders_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)