def convert_length(from_unit, to_unit, value):
    conversions = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.344,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }
    
    value_in_meters = value * conversions[from_unit]
    value_in_to_unit = value_in_meters / conversions[to_unit]
    return value_in_to_unit
