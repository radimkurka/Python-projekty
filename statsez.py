def sum(values):
    result = 0
    for value in values:
        result += value
    return result

def count(values):
    result = 0
    for value in values:
        result += 1
    return result

def median(values):
    mid_point = len(values) // 2
    seq = sorted(values)
    if len(values) % 2 == 0:
        return (seq[mid_point] + seq[mid_point - 1]) / 2
    else:
        return seq[mid_point]

def modus(values):
    counts = {}
    for value in values:
        counts[value] = counts.setdefault(value, 0) + 1

    result = None
    for k, v in counts.items():
        if not result or result[1] < v:
            result = (k, v)
    return result[0]

def mean(values):
    return sum(values) / count(values)


def main():
    dataset = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]
    print("Hi we have the following dataset")
    print(dataset)

    actions = {
        'SUM': sum,
        'COUNT': count,
        'MEAN': mean,
        "MODUS": modus,
        "MEDIAN": median
    }

    while True:
        choice = input("""
        What do you want to calculate?
        Type your choice or "q" to quit.
        | SUM | COUNT | MEAN | MODUS | MEDIAN
        """)
        choice = choice.upper()
        if choice.lower() == "q":
            break
        elif choice not in actions:
            input("Action not found")
            input("Press ENTER to continue")
            continue
        result = actions[choice](dataset)

        print(f"Result of {choice}: {result}")
        input("Press ENTER to continue")

main()