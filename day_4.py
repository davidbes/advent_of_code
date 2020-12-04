
def create_documents():
    data = " ".join(["-" if x == "\n" else x.strip()
                     for x in open("inputs/day_4.txt")]).split(" - ")
    documents = []
    for doc in data:
        valid_pass = {
            "byr": None,
            "iyr": None,
            "eyr": None,
            "hgt": None,
            "hcl": None,
            "ecl": None,
            "pid": None,
            "cid": None
        }
        for spec in doc.split(" "):
            line = spec.split(":")
            valid_pass[line[0]] = line[1]

        documents.append(valid_pass)
    return documents


data = create_documents()


def validate_document(document):
    for key, value in document.items():
        if value == None:
            if key != "cid":
                return False
    else:
        return True


def is_valid_height(height):
    if height.endswith("cm"):
        return height[:-2].isnumeric() and len(height) == 5 and 150 <= int(height[:-2]) <= 193
    elif height.endswith("in"):
        return height[:-2].isnumeric() and len(height) == 4 and 59 <= int(height[:-2]) <= 76
    else:
        return False


# I could use regex but why not this.
def is_hex_code(string):
    valid_chars = "0123456789abcdef"
    if string.startswith("#") and len(string) == 7:
        for c in string[1:]:
            if c not in valid_chars:
                return False
        else:
            return True
    else:
        return False


def better_validate(document):
    valid = 0
    eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    for item, value in document.items():
        if value != None:
            valid += item == "byr" and value.isnumeric() and len(value) == 4 and 1920 <= int(value) <= 2002
            valid += item == "iyr" and value.isnumeric() and len(value) == 4 and 2010 <= int(value) <= 2020
            valid += item == "eyr" and value.isnumeric() and len(value) == 4 and 2020 <= int(value) <= 2030
            valid += item == "hgt" and is_valid_height(value)
            valid += item == "hcl" and is_hex_code(value)
            valid += item == "ecl" and value in eye_colors
            valid += item == "pid" and len(value) == 9 and value.isnumeric()
    return valid == len(document) - 1


def count_valid_documents_one(data):
    return sum([validate_document(doc) for doc in data])


def count_valid_documents_two(data):
    return sum([better_validate(doc) for doc in data])


print(count_valid_documents_one(data), count_valid_documents_two(data))
