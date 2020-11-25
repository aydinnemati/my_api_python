from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_end1_correct():
    res = client.post("/adduser/?name=aaabc&phone=09458aaaaaa")
    assert res.status_code == 200
    assert res.json() == {"Username": "aaabc", "PhoneNumber": "09458aaaaaa"} #change name and phone everytime
def test_end1_name():
    res = client.post('/adduser/?name=&phone=09aaaaaaaaa')
    assert res.json() == {"detail":"Please Enter Your Name"} 
    assert res.status_code == 400
def test_end1_phone():
    res = client.post('/adduser/?name=sadsafsa&phone=')
    assert res.status_code != 200
def test_end1_phone2():
    res = client.post('/adduser/?name=sadsafsa&phone=121351531')
    assert res.status_code == 422
def test_end2_read():
    res = client.get('/read/')
    assert res.status_code == 200
def test_end2_correct():
    res = client.get("/div/?a=100&b=2")
    assert res.json() == 50
    assert res.status_code == 200
def test_end2_wrong_params():
    res = client.get("/div/",
    json = {"a": "", "b": "455"})
    assert res.status_code != 200
    