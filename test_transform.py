from transform import transform

def test_transform_amount_to_float():
    rows = [{"amount": "100"}]
    result = transform(rows)
    assert result[0]["amount"] == 100.0
