from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_end1_correct():
    res = client.post("/",
    json = {"name": "abc", "phone": "09458786631"})
    assert res.json() == {"name": "abc", "phone": "09458786631"}
    assert res.status_code == 200
def test_end1_name_none():
    res = client.post("/",
    json = {"name": None, "phone": "09458786631"})
    assert res.status_code != 200
def test_end1_phone_wrong():
    res = client.post("/",
    json = {"name": "abc", "phone": "1321546"})
    assert res.status_code != 200

def test_end2_correct():
    res = client.get("/div/?a=100&b=2")
    assert res.json() == 50
    assert res.status_code == 200
def test_end2_wrong_params():
    res = client.get("/div/",
    json = {"a": "", "b": "455"})
    assert res.status_code != 200
    