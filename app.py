import streamlit as st

# Define acetaminophen dosing data
dosing_data = {
    "Infant's Acetaminophen (160 mg / 5 mL)": {
        "dose_form": "liquid",
        "concentration": 160 / 5,
        "age_weight_ranges": [
            ((6, 11), (0, 3), 1.25),
            ((12, 17), (4, 11), 2.5),
            ((18, 23), (12, 23), 3.75)
        ],
    },
    "Children's Acetaminophen (160 mg / 5 mL)": {
        "dose_form": "liquid",
        "concentration": 160 / 5,
        "age_weight_ranges": [
            ((24, 35), (24, 35), 5),
            ((36, 47), (4, 5), 7.5),
            ((48, 59), (6, 8), 10),
            ((60, 71), (9, 10), 12.5),
            ((72, 95), (11, 11), 15),
            ((96, float("inf")), (12, float("inf")), 20)
        ],
    },
    "Children's Acetaminophen Chewables (160 mg)": {
        "dose_form": "tablet",
        "concentration": 160,
        "age_weight_ranges": [
            ((24, 35), (2, 3), 1),
            ((36, 47), (4, 5), 1.5),
            ((48, 59), (6, 8), 2),
            ((60, 71), (9, 10), 2.5),
            ((72, 95), (11, 11), 3),
            ((96, float("inf")), (12, float("inf")), 4)
        ],
    },
    "Children's Acetaminophen Dissolvable Packets (160 mg)": {
        "dose_form": "packet",
        "concentration": 160,
        "age_weight_ranges": [
            ((48, 59), (6, 8), 2),
            ((60, 71), (9, 10), 2),
            ((72, 95), (11, 11), 3)
        ],
    },
    "Adult's Acetaminophen Tablets (325 mg)": {
        "dose_form": "tablet",
        "concentration": 325,
        "age_weight_ranges": [
            ((48, 59), (6, 8), 1),
            ((60, 71), (9, 10), 1),
            ((72, 95), (11, 11), 1.5),
            ((96, float("inf")), (12, float("inf")), 2)
        ],
    },
    "Adult's Acetaminophen Tablets (500 mg)": {
        "dose_form": "tablet",
        "concentration": 500,
        "age_weight_ranges": [
            ((72, 95), (11, 11), 1),
            ((96, float("inf")), (12, float("inf")), 1)
        ],
    },
}

# Helper function to calculate dosage based on weight or age
def get_dosage(weight, age, formulation):
    # Retrieve the dosing information for the selected formulation
    if formulation not in dosing_data:
        return "Formulation not found. Please select a valid option."

    formulation_data = dosing_data[formulation]
    for (weight_range, age_range, dose) in formulation_data["age_weight_ranges"]:
        min_weight, max_weight = weight_range
        min_age, max_age = age_range

        # Check if within weight and age range
        if min_weight <= weight <= max_weight or min_age <= age <= max_age:
            # Calculate and return dose
            dose_type = "mL" if formulation_data["dose_form"] == "liquid" else "tablets" if formulation_data["dose_form"] == "tablet" else "packets"
            return f"Dosage: {dose} {dose_type} of {formulation}"

    # Warning if no match found
    return f"Warning: {formulation} is not typically used for this age or weight. Please check your selection."

# Streamlit interface
st.title("Acetaminophen Dosing Calculator")

# User selects dosing by weight or age
dosing_choice = st.selectbox("Would you like to dose by Weight or Age?", ["Weight", "Age"])

if dosing_choice == "Weight":
    unit = st.selectbox("Select units:", ["Pounds", "Kilograms"])
    weight = st.number_input(f"Enter the patient's weight in {unit}:", min_value=0.0, step=0.1)

    # Convert pounds to kilograms if needed
    if unit == "Pounds":
        weight = weight * 0.453592

    age = None  # Not needed for weight-based dosing

elif dosing_choice == "Age":
    age = st.number_input("Enter the patient's age in months:", min_value=0, step=1)
    weight = None  # Not needed for age-based dosing

# Select formulation
formulation = st.selectbox("Select the formulation", list(dosing_data.keys()))

# Calculate dosage when the button is pressed
if st.button("Calculate Dosage"):
    if dosing_choice == "Weight" and weight is None:
        st.write("Please enter a valid weight.")
    elif dosing_choice == "Age" and age is None:
        st.write("Please enter a valid age.")
    else:
        # Display dosage or warning if atypical
        result = get_dosage(weight, age, formulation)
        st.write(result)

    # Additional instructions for acetaminophen use
    st.markdown("""
    **Important Instructions:**
    - Give every 4 to 6 hours if needed for fever or pain.
    - **DO NOT exceed 4 doses in 24 hours.**
    - Avoid using with other medications containing acetaminophen.
    - [Dosing information sourced from HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Ibuprofen-for-Fever-and-Pain.aspx)
    """)

# Restart option
if st.button("Restart Calculator"):
    st.experimental_rerun()

