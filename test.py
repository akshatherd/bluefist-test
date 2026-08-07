def get_user_discount(order: dict) -> float:
    customer = order.get("customer")
    if not isinstance(customer, dict):
        raise KeyError("Missing or invalid 'customer' data in order")
    
    tier = customer.get("tier")
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
    try:
        total_raw = order.get("total")
        total = float(total_raw)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid total value: {order.get('total')}") from e
        
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

    print("Discounted total:", apply_discount(sample_order))
    print("Top item:", top_line_item(sample_order))