import csv

def extract(file_path):
    with open(file_path, newline="") as file:
        rows = list(csv.DictReader(file))
    print(f"Row count: {len(rows)}")
    return rows

if __name__ == "__main__":
    extract("sample.csv")
