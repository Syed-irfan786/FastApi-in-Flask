















from flask import Flask, request, jsonify
import mysql.connector as mysql
from fastapi import FastAPI
from flask_cors import CORS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = Flask(__name__)
CORS(app)
app = FastAPI()
origins = [
     "http://localhost",
    "http://192.168.0.85:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





conn = mysql.connect(host="localhost", user="root", password="", database="test_fast_api")

@app.get("/get-all-data")
def allData():
    curs=conn.cursor(dictionary=True)
    curs.execute("SELECT * from items")
    temp=curs.fetchall()
    for a in temp:
        print(a)
    return temp

@app.get("/get-data-by-id/{id}")
def getDataById(id: int):
    curs=conn.cursor(dictionary=True)
    query="SELECT * from items where id="+ str(id)
    curs.execute(query)
    temp=curs.fetchall()
    return temp


@app.get("/delete-data-by-id/{id}")
def deleteDataById(id: int):
    curs=conn.cursor(dictionary=True)
    query="DELETE FROM items where id="+ str(id)
    curs.execute(query)
    conn.commit()
    return "Deleted successfully"

class Item(BaseModel):
    item_name: str
    item_price: float
    item_status: int

@app.post("/post-data")
async def post_data(item:Item):
    item_name = item.item_name
    item_price = item.item_price
    item_status = item.item_status
    curs=conn.cursor(dictionary=True)
    query = "Insert into items (`item_name`, `item_price`, `item_status`) values ('"+item_name+"',"+str(item_price)+","+str(item_status)+")"
    curs.execute(query)
    conn.commit()
    return "Data successfully inserted into database"
             

@app.get("/delete-by-name/{name}")
def deleteByName(name:str):
    curs=conn.cursor(dictionary=True)
    query="DELETE FROM items where item_name="+name
    curs.execute(query)
    conn.commit()
    return "Deleted Successfully"

