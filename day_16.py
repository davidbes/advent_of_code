def process_data_task_one(filename):
    rules, your_ticket, nearby_tickets = [x for x in open(
        filename).read().split("\n\n")]
    rules = [y for x in rules.split("\n")
             for y in x.split(": ")[1].split(" or ")]
    intervals = []
    for rule_line in rules:
        first, second = rule_line.split("-")
        intervals.append((int(first), int(second)))

    nearby_tickets_processed = []
    for x in nearby_tickets.split("\n")[1:]:
        for num in x.split(","):
            if num != "":
                nearby_tickets_processed.append(int(num))
    your_ticket = [int(x) for x in your_ticket.split("\n")[1:][0].split(",")]
    return sorted(intervals), sorted(your_ticket), sorted(nearby_tickets_processed)


def task_one(data):
    intervals, _, nearby = data
    allowed = set()
    for first, second in intervals:
        allowed.update(set(range(first, second + 1)))

    return [x for x in nearby if x not in allowed]


def process_data_task_two(filename):
    rules, your_ticket, nearby_tickets = [x for x in open(
        filename).read().split("\n\n")]

    intervals = dict()
    for line in rules.split("\n"):
        name, values = line.split(": ")
        vals = []
        for rule_line in values.split(" or "):
            first, second = rule_line.split("-")
            vals.append((int(first), int(second)))
        intervals[name] = vals

    your_ticket = [int(x) for x in your_ticket.split("\n")[1:][0].split(",")]

    non_allowed = set(task_one(process_data_task_one(filename)))
    tickets = []
    for line in nearby_tickets.split("\n")[1:]:
        numbers = [int(x) for x in line.split(",")]
        if set(numbers) & non_allowed != set():
            continue
        else:
            tickets.append(numbers)

    return intervals, your_ticket, tickets


def get_rules_order(rules, nearby):
    get_current_orders = [set(rules.keys())] * len(rules)
    for ticket in nearby:
        for i, rule in enumerate(ticket):
            possibile_rules = set()
            for key, ((x1, x2), (y1, y2)) in rules.items():
                if x1 <= rule <= x2 or y1 <= rule <= y2:
                    possibile_rules.add(key)
            get_current_orders[i] = get_current_orders[i] & possibile_rules

    while any(len(item) > 1 for item in get_current_orders):
        for order in get_current_orders[:]:
            if len(order) == 1:
                for indx, _ in enumerate(get_current_orders[:]):
                    if len(get_current_orders[indx]) != 1:
                        get_current_orders[indx] -= order

    return [x.pop() for x in get_current_orders]


def get_multiple(your, order):
    multi = 1
    for num, order in zip(your, order):
        if "departure" in order:
            multi *= num
    return multi


data = process_data_task_one("inputs/day_16.txt")

print(sum(task_one(data)))

rules, your, nearby = process_data_task_two("inputs/day_16.txt")
order_of_rules = get_rules_order(rules, nearby)
print(get_multiple(your, order_of_rules))
