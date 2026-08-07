# broken_service.py — intentionally buggy for BLUEFIST sandbox testing

def get_user_discount(order: dict) -> float:
    # Bug 1: raw dict access — will KeyError if "customer" or "tier" missing
    tier = order["customer"]["tier"]

    discounts = {
        "gold": 0.20,
        "silver": 0.10,
        "bronze": 0.05,
    }

    # Bug 2: raw dict access again — will KeyError on an unknown tier
    return discounts[tier]


def apply_discount(order: dict) -> float:
    discount = get_user_discount(order)
    # Bug 3: no type coercion — "total" arrives as a string from the API
    total = order["total"]
    return total - (total * discount)


def top_line_item(order: dict) -> str:
    # Bug 4: unguarded index access on a possibly empty list
    return order["items"][0]["name"]


if __name__ == "__main__":
    sample_order = {
        "customer": {"tier": "platinum"},   # not in the discounts table
        "total": "199.99",                   # string, not float
        "items": [],                          # empty list
    }

    print("Discounted total:", apply_discount(sample_order))
    print("Top item:", top_line_item(sample_order))
