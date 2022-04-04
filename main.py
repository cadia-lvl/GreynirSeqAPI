from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
from pydantic import BaseModel
import traceback

import tokenizer 
import model

__version__ = 0.1

app = FastAPI()

def error(errors):
    return JSONResponse(content=({"failure":{"errors":[errors]}}))


@app.get("/", response_class=HTMLResponse)  # type: ignore
def root() -> str:
    return """
<html>
    <head><title>GreynirSeq API Server v{0}</title></head>
    <body>
        <h1>GreynirSeq API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(
        __version__
    )

class TranslateInput(BaseModel):
    type: Optional[str] = "text"
    content: str
    
@app.post("/translate/isen")
def translate(text : TranslateInput):
    try:
        sentences = tokenizer.split_into_sentences(text.content)
        ice = model.model_isen.sample(sentences)
    except:
        return error({"code":"greynirseq.model.isen.error", "text":"Model could not process input", "detail":{'traceback':traceback.format_exc()}})   
    texts = []
    for sentence in ice:
        texts.append({"content":sentence})
        
    return JSONResponse(content={"response":{"type":"texts", "texts":texts}})

@app.post("/translate/enis")
def translate(text : TranslateInput):
    try:
        sentences = tokenizer.split_into_sentences(text.content)
        en = model.model_enis.sample(sentences)
    except:
        return error({"code":"greynirseq.model.enis.error", "text":"Model could not process input", "detail":{'traceback':traceback.format_exc()}})   
    texts = []
    for sentence in en:
        texts.append({"content":sentence})
        
    return JSONResponse(content={"response":{"type":"texts", "texts":texts}})

