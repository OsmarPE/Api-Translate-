from fastapi import Body,Request, FastAPI
from pydantic import BaseModel;
from traductor_texto import translateText
from fastapi.middleware.cors import CORSMiddleware 
app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins='*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)


class Item(BaseModel):
    text: str

@app.post("/promp")
async def get_body(data: Item):
    textTranslated = translateText(data.text)
    return{"message":textTranslated} 