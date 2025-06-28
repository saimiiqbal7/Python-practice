
import csv

with open("hello.csv", 'r') as f:
    reader = csv.reader(f)
    content = list(reader)

    for item in content:
        print(f"{item[0]} got a {item[2]} in {item[3]}")