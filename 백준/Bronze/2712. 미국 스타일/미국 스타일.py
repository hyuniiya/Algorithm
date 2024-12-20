CONVERSION_RATES = {
    "kg": (2.2046, "lb"),
    "lb": (0.4536, "kg"),
    "l": (0.2642, "g"),
    "g": (3.7854, "l")
}

def convert_unit(value, unit):
    rate, target_unit = CONVERSION_RATES[unit]
    return round(value * rate, 4), target_unit

t = int(input())
results = []

for _ in range(t):
    data = input().split()
    value = float(data[0])
    unit = data[1]
    converted_value, converted_unit = convert_unit(value, unit)
    results.append(f"{converted_value:.4f} {converted_unit}")

print("\n".join(results))