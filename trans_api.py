from fastapi import Query,Body,FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from api.PYtranslator import google_translator
from api import constant
from langdetect import detect,DetectorFactory
import time

DetectorFactory.seed = 0  

app=FastAPI(description='Tranlating API for Reduct Nepal')


class Text(BaseModel):
    text:str
    lang:str
    
    class Config:
        extra_schema={
            'example':{
                'text':'Hello world this is a test text to be translated',
                'lang':'en'
            }

        }

@app.get('/codes')
async def get_codes()-> str:
    return JSONResponse(constant.LANGUAGES)

async def translate_munche(sentence:str,lang:str) -> dict:
    result_lang = detect(sentence)
    try:
        if result_lang == lang:        
            return {"Detected language":result_lang,"translated_text":sentence}
        else:
            try:
                translator = google_translator()
                translated = await translator.translate(sentence,lang_src=str(result_lang),lang_tgt=str(lang))
                final_output = {"Detected language":result_lang,"translated_text":translated}
                return final_output
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
   
@app.post('/translate')
async def translate(text:Text):
    start = time.time()
    _tobe_translated = (text.dict())['text']
    langugae = (text.dict())['lang']
    final_output = await translate_munche(_tobe_translated,langugae)
    return JSONResponse(final_output)
    

    
