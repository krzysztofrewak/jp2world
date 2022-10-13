import csv
import json
import random
from toc import categories


places = []

for category in categories:
    for file in categories[category]:
        with open(file, encoding='utf-8') as f:
            i = 0
            for line in csv.reader(f, delimiter=";"):
                if i == 0:
                    i += 1
                    continue

                places.append({
                    "name": line[0],
                    "city": line[1],
                    "type": category,
                    "coordinates": [line[2], line[3]]
                })

random.shuffle(places)

with open("./public/assets/places.json", "w", encoding='utf-8') as file:
    json.dump(places, file, indent=True, ensure_ascii=False)
