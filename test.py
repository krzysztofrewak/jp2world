import csv
from toc import categories


def is_proper_coordinate(value):
    parts = value.split(".")

    if not len(parts) == 2:
        return False

    if parts[0].startswith("-"):
        if not parts[0][1:].isnumeric():
            return False
    else:
        if not parts[0].isnumeric():
            return False

    if parts[1].startswith("-"):
        if not parts[1][1:].isnumeric():
            return False
    else:
        if not parts[1].isnumeric():
            return False

    return True

for category in categories:
    for file in categories[category]:
        with open(file, encoding='utf-8') as f:
            i = 0
            for line in csv.reader(f, delimiter=";"):
                if not i == 0:
                    assert len(line) == 4, "Line {} should contain 4 elements in {}".format(i, file)
                    assert is_proper_coordinate(line[2]), "Line {} of {} latitude should be a proper coordinate".format(i, file)
                    assert is_proper_coordinate(line[3]), "Line {} of {} longitude should be a proper coordinate".format(i, file)
                else:
                    assert ";".join(line) == "name;location;longitude;latitude", "First line in {} file should be a header row".format(file)

                i = i + 1