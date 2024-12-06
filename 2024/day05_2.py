def get_rules(rules, update):
    return [rule for rule in rules if rule[0] in update and rule[1] in update]

def is_ordered(update, checking_rules):
    return all(update.index(rule[0]) < update.index(rule[1]) for rule in checking_rules)

def get_priority(page, checking_rules):
    return sum(page == a for a, b in checking_rules)
    
def get_middle_page(update):
    return update[len(update)//2]

rules, updates = open("input.txt").read().split("\n\n")
rules = [list(map(int, rule.split("|"))) for rule in rules.split()]
updates = [list(map(int, update.split(","))) for update in updates.split()]

ans = 0
for update in updates:
    checking_rules = get_rules(rules, update)
    if not is_ordered(update, checking_rules):
        sorted_update = sorted(update, key=lambda x: get_priority(x, checking_rules))
        ans += get_middle_page(sorted_update)
print(ans)