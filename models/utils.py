def calculate_weight(things: list):
    total_weight = 0.0
    for thing in things:
        total_weight += thing.weight
    return total_weight
