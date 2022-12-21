from fastapi import FastAPI

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC7b46e594a5ff0c58143ecfbed6cb55d9"
auth_token = "ee4a7991107b09a1d7bd62f11a6870b8"
client = Client(account_sid, auth_token)


app = FastAPI()


from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random
with open('student_name.txt', 'w') as f:
        f.write('')
"""
무드등: A
산타모자: B
헤어핀 : C
선글라스 : D
초콜릿: X
"""

product_dict = {"A": "무드등",  "B":  "산타모자",  "C":"헤어핀","D": "선글라스","X": "초콜릿"}
award = ["A", "B", "B", "C", "C", "C", "C", "D", "X", "X", "X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X",  ]
student_list = []
app = FastAPI()

app.mount("/staticFiles", StaticFiles(directory="staticFiles"), name="staticFiles")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/lottery", response_class=HTMLResponse)
async def lotto_clk(request: Request):
    return templates.TemplateResponse("lotto.html", {"request": request})

@app.post("/lottery/chose", response_class=HTMLResponse)
async def submit_number(request: Request ,input_number = Form()):
    if input_number in student_list:
        return templates.TemplateResponse("close.html", {"request": request})
    else:
        student_list.append(input_number)
    if len(award) == 0:
        product = "X"
    else:
        product_num = random.randint(0, len(award) - 1)
        product = award[product_num]
        award.remove(product)
        message = client.messages.create(
        body= input_number +  product_dict.get(product),
        from_="+12136000248",
        to="+821084752286"
        )
        print(message.sid)
    return templates.TemplateResponse("award.html", {"request": request, "input_number":input_number, "product":product})