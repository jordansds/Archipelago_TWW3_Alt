def required_capacity_items(settlement_count: int, capacity_step: int) -> int:
    if settlement_count < 0:
        raise ValueError("Settlement count cannot be negative")
    if capacity_step <= 0:
        raise ValueError("Capacity step must be positive")

    # The first capacity tier is free, so only later tiers are generated as items.
    return max(0, ((settlement_count + capacity_step - 1) // capacity_step) - 1)


def capacity_tiers(received_items: int) -> int:
    if received_items < 0:
        raise ValueError("Received item count cannot be negative")

    return received_items + 1


def settlement_capacity(received_items: int, capacity_step: int) -> int:
    if capacity_step <= 0:
        raise ValueError("Capacity step must be positive")

    return capacity_tiers(received_items) * capacity_step
