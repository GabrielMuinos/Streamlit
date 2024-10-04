import streamlit as st

def calculate_recipe(total, hydration):
    try:
        # Convert inputs to floats
        total = float(total)
        hydration = float(hydration)

        # Calculate tangzhong and preferment
        tangzhong = 0.2 * total
        tangzhongWater = tangzhong / 2
        tangzhongFlour = tangzhong / 2

        preferment = 0.2 * total
        prefermentWater = preferment / 2
        prefermentFlour = preferment / 2

        # Calculate the rest of the ingredients
        pre = preferment + tangzhong
        rest = total - pre

        finalConcentr = hydration / (hydration + 1)
        concentMain = ((finalConcentr * total) - (0.5 * tangzhong) - (0.5 * preferment)) / rest

        water = concentMain * rest
        flour = rest - water

        # Prepare the result as a formatted string
        result = (
            f"This recipe assumes 100% hydration in the tangzhong and the preferment.\n\n"
            f"This recipe will create a bread with a total weight of {total} grams "
            f"and a total hydration of {hydration}.\n\n"
            f"The day before, you need to make tangzhong using {tangzhongFlour:.2f} grams of flour and "
            f"{tangzhongWater:.2f} grams of water.\n"
            f"Also the day before, you need to make the preferment using {prefermentFlour:.2f} grams of flour and "
            f"{prefermentWater:.2f} grams of water with a bit of yeast.\n\n"
            f"On the day, you need to mix salt, yeast, the tangzhong, the preferment, and a total of "
            f"{flour:.2f} grams of flour and {water:.2f} grams of water."
        )

        # Return the result
        return result
    except ValueError:
        return "Input Error: Please enter valid numbers."

# Streamlit app
st.title("Bread Recipe Calculator")

# Input fields
total_weight = st.text_input("Total Weight (in grams):", "")
total_hydration = st.text_input("Total Hydration (as a proportion):", "")

# Calculate button
if st.button("Calculate Recipe"):
    # Perform calculation and show the result
    result = calculate_recipe(total_weight, total_hydration)
    st.write(result)
