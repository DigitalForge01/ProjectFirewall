# rules_manager.py

# In-memory rule set
rules = {
    "block_ips": [],
    "allow_ports": [],
    "block_protocols": []
}

def load_rules():
    return rules

def add_rule(rule_type, value):
    if rule_type in rules:
        if value not in rules[rule_type]:
            rules[rule_type].append(value)

def remove_rule(rule_type, value):
    if rule_type in rules and value in rules[rule_type]:
        rules[rule_type].remove(value)

def get_rules():
    return rules
