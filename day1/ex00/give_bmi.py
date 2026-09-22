def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """Return BMI values (kg / m²)
    for parallel lists of heights (m) and weights (kg)."""
    try:
        if (type(height) is not list or type(weight) is not list):
            raise TypeError("Objects should be lists")
        if (len(height) != len(weight)):
            raise ValueError("both lists should have the same amount of data")
        bmi = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                    or not isinstance(w, (int, float)):
                raise TypeError("Lists must contain only integers or floats")
            if h <= 0 or w <= 0:
                raise ValueError("Values should be greater than 0")
            bmi.append(w / (h*h))
        return bmi

    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}{':'}", e)
    return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of boolean corresponding
    if the bmis are greater than limit"""
    try:
        if type(bmi) is not list:
            raise TypeError("bmi should be a list")
        if type(limit) is not int:
            raise ValueError("limit should be an int")
        return list(x >= limit for x in bmi)

    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}{':'}", e)
    return []
