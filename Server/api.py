"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from fpdf import FPDF
import markdown
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.responses import FileResponse, PlainTextResponse,JSONResponse
from fastapi.middleware.cors import CORSMiddleware


genai.configure(api_key="")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Professional and consise",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "",
      ],
    },


  ]
)
def pdf_response(lecture_transcript):
    response = chat_session.send_message(f" Above given is a lecture. Generate lecture notes of the lecture that is over 1000 words long. Ensure that these notes captures the significant details of the text in over 1000 words. Output this 1000 word notes using basic html formatting and styling. it must be in markdown and structure into title, paragraph, lists.{lecture_transcript}")
    data = str(response.text)
    data.replace("–", "")
    return markdown.markdown(data)

def initialize():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Times", size=14)
    return pdf

def html2pdf(pdf, html_text):
    with open("new.txt", "w+") as handle:
        handle.write(html_text)
    pdf.write_html(html_text)

def create(html_text, output_file):
    pdf = initialize()
    html2pdf(pdf, html_text) 
    pdf.output(output_file)

def cheatsheet_response(lecture_transcript):
    response= chat_session.send_message(f"Generate a cheatsheet from the above given lecture. It should have atleast 30 bullet points Output this in markdown.{lecture_transcript}")
    data=str(response.text)
    return markdown.markdown(data)


def flashcard_response(lecture_transcript):
    response=chat_session.send_message(f"Generate flashcards from the given lecture.It should be in the form of a list with format [[index, question, answer]] . Return it as a Python 2D list{lecture_transcript}")
    data=str(response.text).replace("```python","")
    data=data.replace("```","")
    return data

def quiz_response(lecture_transcript):
    response=chat_session.send_message(f"Generate 7-8 questions from the given lecture.  Each question should have a single correct answer and three incorrect options. Provide the questions and options in a JSON format, where each question is an object containing the question text, a list of four options, and the index of the correct option in the list.{lecture_transcript}")
    data=str(response.text).replace("```json","")
    data=data.replace("```","")
    return data



#API
pdf_test="summary.pdf"
cheatsheet_test="cheatsheet.pdf"
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/v1/info")
async def home():
    return {"200": "OK"}

@app.get("/v1/get_pdf/{data}", response_class=FileResponse)
async def get_pdf(data: str):
    create(pdf_response(data), "summary.pdf")
    return FileResponse(pdf_test, media_type='application/pdf', filename='summary.pdf')


@app.get("/v1/cheatsheet/{data}", response_class=FileResponse)
async def cheatsheet(data:str):
    create(cheatsheet_response(data),"cheatsheet.pdf")
    return FileResponse(cheatsheet_test, media_type='application/pdf',filename="cheatsheet.pdf")


@app.get("/v1/flashcard/{data}",response_class=PlainTextResponse)
async def flashcard(data:str):
    response=flashcard_response(data)
    newdata = response.replace("flashcards =", "")
    return PlainTextResponse(content=newdata)

@app.get("/v1/quiz/{flag}/{data}",response_class=PlainTextResponse)
async def quiz(data:str,flag:int):
    store=""
    if store == False:
        response=chat_session.send_message(f"Generate 1 multiple choice question with 4 options from the given lecture. Return it as a python list with question upfront followed by 4 choices and then the index of the correct option.{data}")
        store=str(response.text)
    else:
        if flag==0:
            response=chat_session.send_message(f"Generate 1 multiple choice question related to the given question. It should have 4 options. It should be returned as a python list with question upfront followed by options and finally the index of correct answer.{store}")
            store=str(response.text)
        else:
            response=chat_session.send_message(f"Generate 1 multiple choice question not so similar to the given question but still within the same topic. It should have 4 options. It should be returned as a python list with question upfront followed by options and finally the index of correct answer.{store}")
            store=str(response.text)
    return PlainTextResponse(content=store)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
