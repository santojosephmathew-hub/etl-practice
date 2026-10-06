def transform(rows):
    for row in rows:
        row["amount"] = float(row["amount"])
    return rows
