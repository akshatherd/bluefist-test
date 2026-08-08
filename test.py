def get_user_discount(order: dict) -> float:
    customer = order.get("customer", {})
    tier = customer.get("tier", "none")
    discounts = {
        "gold": 0.20,
        "silver": 0.10,
        "bronze": 0.05,
    }
    return discounts.get(tier, 0.0)


def apply_discount(order: dict) -> float:
    discount = get_user_discount(order)
    total = float(order.get("total", 0.0))
    return total - (total * discount)


def top_line_item(order: dict) -> str:
    items = order.get("items", [])
    if not items:
        return "N/A"
    return items[0].get("name", "Unknown")


if __name__ == "__main__":
    sample_order = {
        "customer": {"tier": "platinum"},
        "total": "199.99",
        "items": [],
    }

    print("Discounted total:", apply_discount(sample_order))
    print("Top item:", top_line_item(sample_order))
    exit(0)