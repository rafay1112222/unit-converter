import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])
    else:
        return "Invalid length unit"

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    }
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[to_unit] / weight_units[from_unit])
    else:
        return "Invalid weight unit"

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid temperature unit"

def main():
    st.title("Unit Converter")
    conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    
    if conversion_type == "Length":
        from_unit = st.selectbox("From unit:", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        to_unit = st.selectbox("To unit:", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        if st.button("Convert"):
            st.success(f"Converted value: {length_converter(value, from_unit, to_unit)} {to_unit}")
    
    elif conversion_type == "Weight":
        from_unit = st.selectbox("From unit:", ["grams", "kilograms", "pounds", "ounces"])
        to_unit = st.selectbox("To unit:", ["grams", "kilograms", "pounds", "ounces"])
        if st.button("Convert"):
            st.success(f"Converted value: {weight_converter(value, from_unit, to_unit)} {to_unit}")
    
    elif conversion_type == "Temperature":
        from_unit = st.selectbox("From unit:", ["celsius", "fahrenheit", "kelvin"])
        to_unit = st.selectbox("To unit:", ["celsius", "fahrenheit", "kelvin"])
        if st.button("Convert"):
            st.success(f"Converted value: {temperature_converter(value, from_unit, to_unit)} {to_unit}")

if __name__ == "__main__":
    main()
