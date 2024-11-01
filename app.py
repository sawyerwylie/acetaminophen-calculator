import streamlit as st

# Define function to get dosage and warnings based on weight
def get_dosage_by_weight(weight, formulation):
    # Define weight ranges and dosages for each formulation
    warning = ""  # Initialize warning message

    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if weight > 10.99:
            warning = "Warning: Infant's Acetaminophen is not typically used for this weight. Please verify your selection."
        if 3.00 <= weight <= 5.00:
            return "1.25 mL", "40 mg", warning
        elif 5.01 <= weight <= 7.99:
            return "2.5 mL", "80 mg", warning
        elif 8.00 <= weight <= 10.99:
            return "3.75 mL", "120 mg", warning

    elif formulation == "Children's Acetaminophen (160 mg / 5 mL)":
        if weight < 11.00 or weight > 43.99:
            warning = "Warning: Children's Acetaminophen liquid is not typically used for this weight. Please verify your selection."
        if 11.00 <= weight <= 15.99:
            return "5 mL", "160 mg", warning
        elif 16.00 <= weight <= 21.99:
            return "7.5 mL", "240 mg", warning
        elif 22.00 <= weight <= 26.99:
            return "10 mL", "320 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "12.5 mL", "400 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "15 mL", "480 mg", warning
        elif weight >= 44.00:
            return "20 mL", "640 mg", warning

    elif formulation == "Children's Acetaminophen Chewables (160 mg)":
        if weight < 11.00 or weight > 43.99:
            warning = "Warning: Children's Acetaminophen chewables are not typically used for this weight. Please verify your selection."
        if 11.00 <= weight <= 15.99:
            return "1 tablet", "160 mg", warning
        elif 16.00 <= weight <= 21.99:
            return "1.5 tablets", "240 mg", warning
        elif 22.00 <= weight <= 26.99:
            return "2 tablets", "320 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "2.5 tablets", "400 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "3 tablets", "480 mg", warning
        elif weight >= 44.00:
            return "4 tablets", "640 mg", warning

    elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
        if weight < 22.00 or weight > 43.99:
            warning = "Warning: Children's Acetaminophen dissolvable packets are not typically used for this weight. Please verify your selection."
        if 22.00 <= weight <= 26.99:
            return "2 packets", "320 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "2 packets", "320 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "3 packets", "480 mg", warning

    elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
        if weight < 22.00:
            warning = "Warning: Adult Acetaminophen tablets are not typically used for this weight. Please verify your selection."
        if 22.00 <= weight <= 26.99:
            return "1 tablet", "325 mg", warning
        elif 27.00 <= weight <= 32.99:
            return "1 tablet", "325 mg", warning
        elif 33.00 <= weight <= 43.99:
            return "1.5 tablets", "487.5 mg", warning
        elif weight >= 44.00:
            return "2 tablets", "650 mg", warning

    elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
        if weight < 33.00:
            warning = "Warning: Adult Acetaminophen tablets are not typically used for this weight. Please verify your selection."
        if 33.00 <= weight <= 43.99:
            return "1 tablet", "500 mg", warning
        elif weight >= 44.00:
            return "1 tablet", "500 mg", warning

    return "Dose not available", "Please consult a healthcare provider.", warning

# Define function to get dosage by age
def get_dosage_by_age(age, formulation):
    # Define age ranges and dosages for each formulation
    warning = ""  # Initialize warning message

    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if age > 23:
            warning = "Warning: Infant's Acetaminophen is not typically used for this age. Please verify your selection."
        if 0 <= age <= 3:
            return "1.25 mL", "40 mg", warning
        elif 4 <= age <= 11:
            return "2.5 mL", "80 mg", warning
        elif 12 <= age <= 23:
            return "3.75 mL", "120 mg", warning

    elif formulation == "Children's Acetaminophen (160 mg / 5 mL)":
        if age < 24 or age > 143:
            warning = "Warning: Children's Acetaminophen liquid is not typically used for this age. Please verify your selection."
        if 24 <= age <= 35:
            return "5 mL", "160 mg", warning
        elif 36 <= age <= 47:
            return "7.5 mL", "240 mg", warning
        elif 48 <= age <= 71:
            return "10 mL", "320 mg", warning
        elif 72 <= age <= 95:
            return "12.5 mL", "400 mg", warning
        elif 96 <= age <= 143:
            return "15 mL", "480 mg", warning
        elif age >= 144:
            return "20 mL", "640 mg", warning

    elif formulation == "Children's Acetaminophen Chewables (160 mg)":
        if age < 24 or age > 143:
            warning = "Warning: Children's Acetaminophen chewables are not typically used for this age. Please verify your selection."
        if 24 <= age <= 35:
            return "1 tablet", "160 mg", warning
        elif 36 <= age <= 47:
            return "1.5 tablets", "240 mg", warning
        elif 48 <= age <= 71:
            return "2 tablets", "320 mg", warning
        elif 72 <= age <= 95:
            return "2.5 tablets", "400 mg", warning
        elif 96 <= age <= 143:
            return "3 tablets", "480 mg", warning
        elif age >= 144:
            return "4 tablets", "640 mg", warning

    elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
        if age < 48 or age > 95:
            warning = "Warning: Children's Acetaminophen dissolvable packets are not typically used for this age. Please verify your selection."
        if 48 <= age <= 71:
            return "2 packets", "320 mg", warning
        elif 72 <= age <= 95:
            return "3 packets", "480 mg", warning

    elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
        if age < 72:
            warning = "Warning: Adult Acetaminophen tablets are not typically used for this age. Please verify your selection."
        if 72 <= age <= 95:
            return "1.5 tablets", "487.5 mg", warning
        elif age >= 96:
            return "2 tablets", "650 mg", warning

    elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
        if age < 72:
            warning = "Warning: Adult Acetaminophen tablets are not typically used for this age. Please verify your selection."
        if 72 <= age <= 95:
            return "1 tablet", "500 mg", warning
        elif age >= 96:
            return "1 tablet", "500 mg", warning

    return "Dose not available", "Please consult a healthcare provider.", warning

# Streamlit app layout
st.title("Pediatric Acetaminophen Dosing Calculator")

# Select dosing type
choice = st.selectbox("Select Dosing by Weight or Age", ["Weight", "Age"])

# Main input for dosing by weight
if choice == "Weight":
    # Select unit for weight entry
    unit = st.selectbox("Select weight unit", ["kg", "lbs"])

    # Input weight with integer display but allowing for decimal entry
    weight = st.number_input(f"Enter the patient's weight in {unit}:", min_value=0, step=1)

    # Convert weight to kg if entered in lbs
    if unit == "lbs":
        weight = weight * 0.453592  # Convert pounds to kilograms

    formulation = st.selectbox("Select the formulation", [
        "Infant's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen Chewables (160 mg)",
        "Children's Acetaminophen Dissolvable Packets (160 mg)",
        "Adult's Acetaminophen Tablets (325 mg)",
        "Adult's Acetaminophen Tablets (500 mg)"
    ])

    if st.button("Calculate Dosage"):
        dosage, dose, warning = get_dosage_by_weight(weight, formulation)
        if warning:
            st.warning(warning)
        st.write(f"Dosage: {dosage} ({dose})")
        st.write("Give every 4 to 6 hours as needed for fever or pain. Do not exceed 5 doses in 24 hours.")
        st.write("Do not use with any other medicine containing acetaminophen.")

# Main input for dosing by age
elif choice == "Age":
    # Select unit for age entry
    age_unit = st.selectbox("Select age unit", ["Months", "Years"])

    # Enter age
    if age_unit == "Years":
        age = st.number_input("Enter the patient's age in years:", min_value=0, step=1)
        age = age * 12  # Convert years to months
    else:
        age = st.number_input("Enter the patient's age in months:", min_value=0, step=1)

    formulation = st.selectbox("Select the formulation", [
        "Infant's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen Chewables (160 mg)",
        "Children's Acetaminophen Dissolvable Packets (160 mg)",
        "Adult's Acetaminophen Tablets (325 mg)",
        "Adult's Acetaminophen Tablets (500 mg)"
    ])

    if st.button("Calculate Dosage"):
        dosage, dose, warning = get_dosage_by_age(age, formulation)
        if warning:
            st.warning(warning)
        st.write(f"Dosage: {dosage} ({dose})")
        st.write("Give every 4 to 6 hours as needed for fever or pain. Do not exceed 5 doses in 24 hours.")
        st.write("Do not use with any other medicine containing acetaminophen.")

st.write("Note: There are a variety of dosing strategies with acetaminophen, this is one example. Dosing information is sourced from [HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Acetaminophen-for-Fever-and-Pain.aspx).")
