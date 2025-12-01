from app.main import app

def test_api_uses_replaced_chars_txt():
    client = app.test_client()
    res = client.post("/replace", json={"text": "aku suka nasi"})
    assert res.status_code == 200
    assert res.get_json()["result"] == "4ku 5uk4 n451"
