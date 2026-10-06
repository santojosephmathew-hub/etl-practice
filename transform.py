def transform(rows):
    for row in rows:
        row["amount"] = float(row["amount"])
    return rows

def validate(rows):
    return [row for row in rows if row.get("amount") is not None and row.get("amount") != ""]
