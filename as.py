from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# if you want to make your api reachable from js CORS to let it go in order to get it! 


class stu(BaseModel):
    name:str
    roll:int   

my_d = {
    1: {"name": "ashish",
        "roll": 1},
    2: {"name": "Shubha",
        "roll": 2},
    3: {"name": "Bella",
        "roll": 3},
    4: {"name": "Tim",
        "roll": 4},
    }

@app.get("/")
async def show_all():
    return my_d

@app.post("/create/{item_id}")
def create_item(item_id, stu: stu):
    item_id = int(item_id)
    stu.roll = int(stu.roll) 
    my_d[item_id] = {"name":stu.name,"roll":stu.roll}
    return my_d[item_id]


@app.get("read/{item_id}")
def read_item(item_id):
    item_id = int(item_id)
    return my_d[item_id]


@app.put("/update/{item_id}")
def update_item(item_id, stu: stu):
    item_id = int(item_id)
    my_d[item_id] = {}
    my_d[item_id] = {"name":stu.name,"roll":stu.roll}
    return my_d[item_id]


@app.delete("/delete/{item_id}")
def delete_item(item_id):
    item_id = int(item_id)
    del my_d[item_id]