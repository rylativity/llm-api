from src.llms import AppModel
from src.models import LlmRequest

from fastapi import FastAPI, File, UploadFile
from fastapi.logger import logger
from fastapi.responses import RedirectResponse

from io import BytesIO
import logging
import os

### https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/issues/19
gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)
# DEBUG > INFO > WARN > ERROR > CRITICAL > FATAL

app = FastAPI(debug=True)

MODEL_NAME = os.environ.get("MODEL_NAME")
MODEL_FILE = os.environ.get("MODEL_FILE")
TOKENIZER_MODEL_NAME = os.environ.get("TOKENIZER_MODEL_NAME")

model = AppModel(
    model_name=MODEL_NAME,
    model_file=MODEL_FILE,
    tokenizer_model_name=TOKENIZER_MODEL_NAME
)

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse("/docs")


@app.post("/generate")
async def generate(request:LlmRequest):

    return model.run(
        inputs=request.inputs,
        prompt_template=request.prompt_template,
        **request.generation_kwargs
    )
