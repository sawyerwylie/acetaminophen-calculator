import streamlit as st

# Function to calculate dosage based on weight
def get_dosage_by_weight(weight, formulation):
    # Set dosage amounts for Infant's Acetaminophen (160 mg / 5 mL) based on weight in kilograms
    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if 2.7 <= weight <= 5:
            return "Dosage: 1.25 mL"
        elif 5.1 <= weight <= 7.7:
            return "Dosage: 2.5 mL"
        elif 8 <= weight <= 10.4:
            return "Dosage: 3.75 mL"
    
    # Set dosage amounts for Children's Acetaminophen (160 mg / 5 mL) based on weight in kilograms
    elif formulation == "Children's Acetaminophen (160 mg / 5 mL)":
        if 10.9 <= weight <= 15.9:
            return "Dosage: 5 mL"
        elif 16.4 <= weight <= 21.3:
            return "Dosage: 7.5 mL"
        elif 21.8 <= weight <= 26.8:
            return "Dosage: 10 mL"
        elif 27.3 <= weight <= 32.2:
            return "Dosage: 12.5 mL"
        elif 32.7 <= weight <= 43.1:
            return "Dosage: 15 mL"
        elif weight >= 43.2:
            return "Dosage: 20 mL (10 mL + 10 mL)"

    # Set dosage amounts for Children's Acetaminophen Chewables (160 mg) based on weight in kilograms
    elif formulation == "Children's Acetaminophen Chewables (160 mg)":
        if 10.9 <= weight <= 15.9:
            return "Dosage: 1 tablet"
        elif 16.4 <= weight <= 21.3:
            return "Dosage: 1.5 tablets"
        elif 21.8 <= weight <= 26.8:
            return "Dosage: 2 tablets"
        elif 27.3 <= weight <= 32.2:
            return "Dosage: 2.5 tablets"
        elif 32.7 <= weight <= 43.1:
            return "Dosage: 3 tablets"
        elif weight >= 43.2:
            return "Dosage: 4 tablets"

    # Set dosage amounts for Children's Acetaminophen Dissolvable Packets (160 mg) based on weight in kilograms
    elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
        if 21.8 <= weight <= 26.8:
            return "Dosage: 2 packets"
        elif 27.3 <= weight <= 32.2:
            return "Dosage: 2 packets"
        elif 32.7 <= weight <= 43.1:
            return "Dosage: 3 packets"

    # Set dosage amounts for Adult's Acetaminophen Tablets (325 mg) based on weight in kilograms
    elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
        if 21.8 <= weight <= 26.8:
            return "Dosage: 1 tablet"
        elif 27.3 <= weight <= 32.2:
            return "Dosage: 1 tablet"
        elif 32.7 <= weight <= 43.1:
            return "Dosage: 1.5 tablets"
        elif weight >= 43.2:
            return "Dosage: 2 tablets"

    # Set dosage amounts for Adult's Acetaminophen Tablets (500 mg) based on weight in kilograms
    elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
        if 32.7 <= weight <= 43.1:
            return "Dosage: 1 tablet"
        elif weight >= 43.2:
            return "Dosage: 1 tablet"

    # If no valid dosage is found, return a warning message
    return f"Warning: {formulation} is not typically used for this weight. Please check your selection."

# Function to calculate dosage based on age
def get_dosage_by_age(age, formulation):
    # Convert age in years to months for consistency in calculations
    if age > 12:
        age = age * 12
    
    # Set dosages for Infant's Acetaminophen (160 mg / 5 mL) based on age in months
    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if 0 <= age <= 3:
            return "Dosage: 1.25 mL"
        elif 4 <= age <= 11:
            return "Dosage: 2.5 mL"
        elif 12 <= age <= 23:
            return "Dosage: 3.75 mL"
    
    # Additional formulations can be added here with specific age ranges as needed
    return f"Warning: {formulation} is not typically used for this age. Please check your selection."

# Streamlit interface
st.title("Acetaminophen Dosing Calculator")

# User selects dosing by weight or age
dosing_choice = st.selectbox("Would you like to dose by Weight or Age?", ["Weight", "Age"])

# If dosing by weight
if dosing_choice == "Weight":
    # Get weight input in kilograms
    weight = st.number_input("Enter the patient's weight in kilograms (kg):", min_value=0.0, step=0.1)
    age = None  # Age not needed if dosing by weight

# If dosing by age
elif dosing_choice == "Age":
    # Get age input and allow selection between months and years
    age_unit = st.selectbox("Enter age in:", ["Months", "Years"])
    if age_unit == "Years":
        age = st.number_input("Enter the patient's age in years:", min_value=0, step=1) * 12
    else:
        age = st.number_input("Enter the patient's age in months:", min_value=0, step=1)
    weight = None  # Weight not needed if dosing by age

# Select formulation
formulation = st.selectbox("Select the formulation", [
    "Infant's Acetaminophen (160 mg / 5 mL)", 
    "Children's Acetaminophen (160 mg / 5 mL)",
    "Children's Acetaminophen Chewables (160 mg)", 
    "Children's Acetaminophen Dissolvable Packets (160 mg)", 
    "Adult's Acetaminophen Tablets (325 mg)", 
    "Adult's Acetaminophen Tablets (500 mg)"
])

# Calculate dosage when button is pressed
if st.button("Calculate Dosage"):
    if dosing_choice == "Weight":
        result = get_dosage_by_weight(weight, formulation)
    else:
        result = get_dosage_by_age(age, formulation)
    
    # Display the result
    st.write(result)

    # Additional instructions
    st.markdown("""
    **Important Instructions:**
    - Give every 4 to 6 hours if needed for fever or pain.
    - **DO NOT exceed 4 doses in 24 hours.**
    - Avoid using with other medications containing acetaminophen.
    """)

# Restart option
if st.button("Restart Calculator"):
    st.experimental_rerun()
