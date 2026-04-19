def calculate_rate(numerator, denominator, digits=3):
    if not denominator:
        return None
    return round(numerator / denominator, digits)
