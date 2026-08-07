def get_user_discount(order: dict) -> float:
    customer = order.get("customer")
    if not isinstance(customer, dict):
        raise KeyError("Missing or invalid 'customer' data in order")
    
    tier = customer.get("tier")
    if not isinstance(tier, str):
        raise KeyError("Missing or invalid 'tier' in customer data")

    discounts = {
        "gold": 0.20,
        "silver": 0.10,
        "bronze": 0.05,
    }

    if tier not in discounts:
        return 0.0
    
    return discounts[tier]


def apply_discount(order: dict) -> float:
    discount = get_user_discount(order)
    
    raw_total = order.get("total")
    try:
        total = float(raw_total)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid total value: {raw_total}")
        
    return total - (total * discount)


def top_line_item(order: dict) -> str:
    items = order.get("items")
    if not isinstance(items, list) or len(items) == 0:
        return ""
    
    first_item = items[0]
    if not isinstance(first_item, dict):
        return ""
        
    return str(first_item.get("name", ""))


if __name__ == "__main__":
    sample_order = {
        "customer": {"tier": "platinum"},
        "total": "199.99",
        "items": [],
    }

    try:
        print("Discounted total:", apply_discount(sample_order))
        print("Top item:", top_line_item(sample_order))
    except Exception as e:
        import sys
        sys.exit(1)