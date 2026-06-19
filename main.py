from dataclasses import dataclass
from math import ceil

# ==========================

# DATA STRUCTURE

# ==========================

@dataclass
class Dimsum:
    name: str
    price: int
    pieces: int
    tags: set

# ==========================

# MENU DATASET

# ==========================

MENU = [
    Dimsum(
        "Siomay Udang Ayam",
        22727,
        3,
        {"contains_shrimp"}
    ),

    Dimsum(
        "Siomay Ayam",
        21818,
        3,
        set()
    ),

    Dimsum(
        "Hakau",
        23636,
        3,
        {"contains_shrimp", "gluten_free"}
    ),

    Dimsum(
        "Stim Dumpling Udang Kucai",
        23636,
        3,
        {"contains_shrimp", "gluten_free"}
    ),

    Dimsum(
        "Xiao Long Bao Ayam",
        22727,
        3,
        set()
    ),

    Dimsum(
        "Stim Ceker",
        21818,
        3,
        {"contains_shrimp"}
    ),

    Dimsum(
        "Lumpia Steam Saus Tiram",
        26363,
        3,
        set()
    ),

    Dimsum(
        "Pao Telur Asin",
        26363,
        4,
        set()
    ),

    Dimsum(
        "Bao Ayam Panggang Merah",
        25454,
        3,
        set()
    ),

    Dimsum(
        "Dimsum Asparagus Tio Chiu",
        23636,
        3,
        {"vegetarian", "vegan", "gluten_free"}
    ),

    Dimsum(
        "Mantao Kukus HAKA",
        20909,
        3,
        {"vegetarian"}
    ),

    Dimsum(
        "Sayap Ayam Isi Goreng",
        31818,
        2,
        set()
    ),

    Dimsum(
        "Pangsit Udang Goreng",
        29090,
        3,
        {"contains_shrimp"}
    ),

    Dimsum(
        "Lumpia Udang Kulit Tahu",
        34545,
        3,
        {"contains_shrimp"}
    ),

    Dimsum(
        "Lumpia Ayam Kulit Tahu",
        26363,
        3,
        set()
    ),

    Dimsum(
        "Cakwe Udang Goreng",
        23636,
        3,
        {"contains_shrimp"}
    ),

    Dimsum(
        "Onde Telur Asin",
        26363,
        3,
        set()
    ),

    Dimsum(
        "Onde Wijen Hitam",
        23636,
        3,
        set()
    ),

    Dimsum(
        "Mantao Goreng HAKA",
        20909,
        3,
        {"vegetarian"}
    ),

    Dimsum(
        "Puff Ayam Panggang Merah HAKA",
        26363,
        3,
        set()
    ),

    Dimsum(
        "Lobak Panggang",
        22727,
        3,
        {"contains_shrimp"}
    ),

    Dimsum(
        "Dimsum Panggang Daging Vegetarian",
        26363,
        3,
        {"vegetarian", "vegan"}
    ),

    Dimsum(
        "Pao Sapi Panggang",
        26363,
        2,
        set()
    ),

    Dimsum(
        "Bolo Bao Ayam Panggang Merah",
        24545,
        2,
        set()
    ),

    Dimsum(
        "Bolo Bao Mentega Dingin",
        23636,
        1,
        {"vegetarian"}
    ),
]

# ==========================

# FILTERING

# ==========================

def satisfies_restrictions(item, restrictions):
    if "shrimp_allergy" in restrictions:
        if "contains_shrimp" in item.tags:
            return False
    if "vegetarian" in restrictions:
        if "vegetarian" not in item.tags:
            return False
    if "vegan" in restrictions:
        if "vegan" not in item.tags:
            return False
    if "gluten_intolerance" in restrictions:
        if "gluten_free" not in item.tags:
            return False
    return True

# ==========================

# EFFECTIVE COST

# ==========================

def calculate_effective_cost(item, group_size):
    required_servings = ceil(
        group_size / item.pieces
    )
    effective_cost = (
        item.price *
        required_servings
    )
    return effective_cost, required_servings

# ==========================

# PREPROCESSING

# ==========================

def preprocess_menu(menu,group_size,restrictions):
    processed_items = []
    for item in menu:
        if not satisfies_restrictions(item, restrictions):
            continue
        effective_cost, servings = (calculate_effective_cost(item, group_size))
        processed_items.append(
            {
                "name": item.name,
                "effective_cost": effective_cost,
                "required_servings": servings,
                "value": 1
            }
        )
    return processed_items

# ==========================

# DYNAMIC PROGRAMMING

# ==========================

def solve_knapsack(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost = items[i - 1]["effective_cost"]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b:
                dp[i][b] = max(dp[i][b], 1 + dp[i - 1][b - cost])
    return dp

# ==========================

# RECONSTRUCT SOLUTION

# ==========================

def reconstruct_solution(dp, items, budget):
    chosen = []
    i = len(items)
    b = budget
    while i > 0:
        if dp[i][b] != dp[i - 1][b]:
            chosen.append(items[i - 1])
            b -= (items[i - 1]["effective_cost"])
        i -= 1
    chosen.reverse()
    return chosen

# ==========================

# USER INPUT

# ==========================

def get_user_input():
    group_size = int(input("Number of diners: "))
    budget = int(input("Budget (IDR): "))
    restrictions = set()
    print("\nDietary Restrictions:")
    print("1. Shrimp Allergy")
    print("2. Vegetarian")
    print("3. Vegan")
    print("4. Gluten Intolerance")
    print("5. None")
    choices = input("\nSelect option(s): ").split()
    mapping = {
        "1": "shrimp_allergy",
        "2": "vegetarian",
        "3": "vegan",
        "4": "gluten_intolerance"
    }
    for choice in choices:
        if choice in mapping:
            restrictions.add(mapping[choice])
    return (group_size, budget, restrictions)

# ==========================

# DISPLAY RESULT

# ==========================

def display_results(
    chosen_items,
    budget):
    print("\n" + "=" * 40)
    print("RECOMMENDED DIMSUM")
    print("=" * 40)
    total_cost = 0
    for item in chosen_items:
        print(f"{item['name']}")
        print(
            f"  Required Servings : "
            f"{item['required_servings']}"
        )
        print(
            f"  Effective Cost    : "
            f"Rp{item['effective_cost']:,}"
        )
        print()
        total_cost += (item["effective_cost"])
    print("=" * 40)
    print(
        f"Variety Count : "
        f"{len(chosen_items)}"
    )
    print(
        f"Total Cost    : "
        f"Rp{total_cost:,}"
    )
    print(
        f"Budget Left   : "
        f"Rp{budget - total_cost:,}"
    )
    print("=" * 40)


# ==========================

# MAIN

# ==========================

def main():
    (group_size, budget, restrictions) = get_user_input()
    items = preprocess_menu(MENU, group_size, restrictions)
    if len(items) == 0:
        print("\nNo menu items satisfy the selected restrictions.")
        return
    dp = solve_knapsack(items, budget)
    chosen_items = reconstruct_solution(dp, items, budget)
    if len(chosen_items) == 0:
        print("\nNo feasible solution found.")
        print("No menu combination satisfies the specified budget and dietary constraints.")
        return
    display_results(chosen_items, budget)

if __name__ == "__main__":
    main()