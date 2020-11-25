import mysql.connector
from fastapi import FastAPI, Query, HTTPException

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "admin",
    database = "my_api"
)

mycursor = mydb.cursor()
table = []
mycursor.execute("SHOW TABLES LIKE 'user'")
for x in mycursor:
    table.append(x)
# print(table)
if table == [] :
    mycursor.execute("CREATE TABLE user (name VARCHAR(255), phone VARCHAR(255))")

app = FastAPI()

@app.post("/adduser/")
def Add_User(name: str, phone: str = Query(None, min_length=11, max_length=11, regex="^09")): 
    if name == "":
        raise HTTPException(status_code = 400, detail = "Please Enter Your Name")
    if phone == None:
        raise HTTPException(status_code = 400, detail = "Please Enter Your PhoneNumber")
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    listt = []
    list_names = []
    list_phones = []
    for x in myresult:
        listt.append(list(x))
    # print(listt)
    for z in listt: 
        names = z[0]
        list_names.append(names)
    # print(list_names)
    for y in listt:
        phones = z[1]
        list_phones.append(phones)
    # print(list_phones)
    if name in list_names:
        raise HTTPException(status_code = 400, detail = "Name is existed")
    if phone in list_phones:
        raise HTTPException(status_code = 400, detail = "PhoneNumber is existed")
    else:
        sql = 'INSERT INTO user (name, phone) VALUES (%s, %s)'
        val = (name, phone)
        mycursor.execute(sql, val)
        mydb.commit()
        return {"Username": name, "PhoneNumber": phone} 

@app.get("/read/")
def show_users():
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    listt = []
    for x in myresult:
        listt.append(x)
    return listt

@app.get("/div/")
async def divition(a: int, b: int):
    div = a/b
    return int(div)