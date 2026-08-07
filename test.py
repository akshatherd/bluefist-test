def get_user_discount(order: dict) -> float:
    tier = order.get('customer', {}).get('tier', None)
    if tier not in ['gold', 'silver', 'bronze']:
        tier = 'bronze'  # Default to bronze if unknown tier

    discounts = {
        "gold": 0.2,
        "silver": 0.1,
        "bronze": 0.05,
    }

    return discounts.get(tier, 0.05)  # Return default discount if unknown tier


def apply_discount(order: dict) -> float:
    discount = get_user_discount(order)
    total = float(order['total'])
    return total - (total * discount)


def top_line_item(order: dict) -> str:
    items = order.get('items', [])
    return items[0].get('name', 'No item') if items else 'No item'


if __name__ == "__main__":
    sample_order = {
        "customer": {"tier": "platinum"},
        "total": "199.99",
        "items": [],
    }

    print("Discounted total:", apply_discount(sample_order))
    print("Top item:", top_line_item(sample_order))