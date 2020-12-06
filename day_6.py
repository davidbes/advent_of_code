import collections
data = " ".join(["-" if x == "\n" else x.strip()
                 for x in open("inputs/day_6.txt")]).split(" - ")

overall_count = 0
for group in data:
    answers = group.replace(" ", "")
    group_answers = collections.defaultdict(int)
    for c in answers:
        group_answers[c] += 1

    for value in group_answers.values():
        overall_count += value == len(group.split(" "))

print(overall_count)
