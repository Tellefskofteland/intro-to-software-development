def find_average(liste):
    return sum(liste) / len(liste)


def gardners_equation(velocity: float) -> float:
    a = 0.31
    b = 0.25

    # Calculate density using Gardner's equation
    density = a * (velocity**b)
    return density
