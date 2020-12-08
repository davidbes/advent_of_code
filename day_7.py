data = [x.strip() for x in open("inputs/day_7.txt")]


def process_rules(rules):
    processed = dict()
    for rule in rules:
        splitted_rule = rule.split(" bags contain")
        rule_nm = "".join([x for x in splitted_rule[0].split(' ')])
        shorties = {"".join([y for y in x.replace(".", "").replace("bags", "").replace("bag", "").split(" ")[
                            2:]]) for x in splitted_rule[1].split(",")}
        processed[rule_nm] = shorties
    return processed


def contains_bag(bag, rules):
    current_bags = set()
    for rule_name, allowed in rules.items():
        if bag in allowed:
            current_bags.add(rule_name)
            current_bags |= contains_bag(rule_name, rules)
    return current_bags


rules = process_rules(data)
gold_bag = "shinygold"

print(len(contains_bag(gold_bag, rules)))


def process_weight(rules):
    processed = dict()
    for rule in rules:
        splitted_rule = rule.split(" bags contain")
        rule_nm = "".join([x for x in splitted_rule[0].split(' ')])
        rulies = set()
        for rule in splitted_rule[1].split(','):
            short_rule = rule.replace("bags", "").replace(
                "bag", "").replace(".", "").strip().split(" ")
            rule_tup = (int(short_rule[0]), "".join(short_rule[1:])) if len(
                short_rule) == 3 else (0, "".join(short_rule))
            rulies.add(rule_tup)
        processed[rule_nm] = rulies
    return processed


def get_amount_of_baggs(bag, rules):
    amount = 0
    for count, rule in rules[bag]:
        if count != 0:
            amount += count
            amount += count * get_amount_of_baggs(rule, rules)
    return amount


print(get_amount_of_baggs(gold_bag, process_weight(data)))
