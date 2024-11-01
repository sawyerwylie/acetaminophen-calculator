import streamlit as st

# Function to calculate dosage based on weight in kilograms
def get_dosage_by_weight(weight_kg, formulation):
    # Set dosage amounts for Infant's Acetaminophen (160 mg / 5 mL) based on weight in kilograms
    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if 2.7 <= weight_kg <= 5:
            return "Dosage: 1.25 mL (40 mg)"
        elif 5.1 <= weight_kg <= 7.7:
            return "Dosage: 2.5 mL (80 mg)"
        elif 8 <= weight_kg <= 10.4:
            return "Dosage: 3.75 mL (120 mg)"
    
    # Set dosage amounts for Children's Acetaminophen (160 mg / 5 mL) based on weight in kilograms
    elif formulation == "Children's Acetaminophen (160 mg / 5 mL)":
        if 10.9 <= weight_kg <= 15.9:
            return "Dosage: 5 mL (160 mg)"
        elif 16.4 <= weight_kg <= 21.3:
            return "Dosage: 7.5 mL (240 mg)"
        elif 21.8 <= weight_kg <= 26.8:
            return "Dosage: 10 mL (320 mg)"
        elif 27.3 <= weight_kg <= 32.2:
            return "Dosage: 12.5 mL (400 mg)"
        elif 32.7 <= weight_kg <= 43.1:
            return "Dosage: 15 mL (480 mg)"
        elif weight_kg >= 43.2:
            return "Dosage: 20 mL (640 mg)"

    # Set dosage amounts for Children's Acetaminophen Chewables (160 mg) based on weight in kilograms
    elif formulation == "Children's Acetaminophen Chewables (160 mg)":
        if 10.9 <= weight_kg <= 15.9:
            return "Dosage: 1 tablet (160 mg)"
        elif 16.4 <= weight_kg <= 21.3:
            return "Dosage: 1.5 tablets (240 mg)"
        elif 21.8 <= weight_kg <= 26.8:
            return "Dosage: 2 tablets (320 mg)"
        elif 27.3 <= weight_kg <= 32.2:
            return "Dosage: 2.5 tablets (400 mg)"
        elif 32.7 <= weight_kg <= 43.1:
            return "Dosage: 3 tablets (480 mg)"
        elif weight_kg >= 43.2:
            return "Dosage: 4 tablets (640 mg)"

    # Set dosage amounts for Children's Acetaminophen Dissolvable Packets (160 mg) based on weight in kilograms
    elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
        if 21.8 <= weight_kg <= 26.8:
            return "Dosage: 2 packets (320 mg)"
        elif 27.3 <= weight_kg <= 32.2:
            return "Dosage: 2 packets (320 mg)"
        elif 32.7 <= weight_kg <= 43.1:
            return "Dosage: 3 packets (480 mg)"

    # Set dosage amounts for Adult's Acetaminophen Tablets (325 mg) based on weight in kilograms
    elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
        if 21.8 <= weight_kg <= 26.8:
            return "Dosage: 1 tablet (325 mg)"
        elif 27.3 <= weight_kg <= 32.2:
            return "Dosage: 1 tablet (325 mg)"
        elif 32.7 <= weight_kg <= 43.1:
            return "Dosage: 1.5 tablets (487.5 mg)"
        elif weight_kg >= 43.2:
            return "Dosage: 2 tablets (650 mg)"

    # Set dosage amounts for Adult's Acetaminophen Tablets (500 mg) based on weight in kilograms
    elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
        if 32.7 <= weight_kg <= 43.1:
            return "Dosage: 1 tablet (500 mg)"
        elif weight_kg >= 43.2:
            return "Dosage: 1 tablet (500 mg)"

    # If no valid dosage is found, return a warning message
    return f"Warning: {formulation} is not typically used for this weight. Please check your selection."

# Function to calculate dosage based on age in months
def get_dosage_by_age(age, formulation):
    # Set dosages for Infant's Acetaminophen (160 mg / 5 mL) based on age in months
    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if 0 <= age <= 3:
            return "Dosage: 1.25 mL (40 mg)"
        elif 4 <= age <= 11:
            return "Dosage: 2.5 mL (80 mg)"
        elif 12 <= age <= 23:
            return "Dosage: 3.75 mL (120 mg)"
    
    # Set dosages for Children's Acetaminophen (160 mg / 5 mL) based on age in months
    elif formulation == "Children's Acetaminophen (160 mg / 5 mL)":
        if 24 <= age <= 35:
            return "Dosage: 5 mL (160 mg)"
        elif 36 <= age <= 47:
            return "Dosage: 7.5 mL (240 mg)"
        elif 48 <= age <= 59:
            return "Dosage: 10 mL (320 mg)"
        elif 60 <= age <= 71:
            return "Dosage: 12.5 mL (400 mg)"
        elif 72 <= age <= 95:
            return "Dosage: 15 mL (480 mg)"
        elif age >= 96:
            return "Dosage: 20 mL (640 mg)"

    # Set dosages for Children's Acetaminophen Chewables (160 mg) based on age in months
    elif formulation == "Children's Acetaminophen Chewables (160 mg)":
        if 24 <= age <= 35:
            return "Dosage: 1 tablet (160 mg)"
        elif 36 <= age <= 47:
            return "Dosage: 1.5 tablets (240 mg)"
        elif 48 <= age <= 59:
            return "Dosage: 2 tablets (320 mg)"
        elif 60 <= age <= 71:
            return "Dosage: 2.5 tablets (400 mg)"
        elif 72 <= age <= 95:
            return "Dosage: 3 tablets (480 mg)"
        elif age >= 96:
            return "Dosage: 4 tablets (640 mg)"

    # Set dosages for Children's Acetaminophen Dissolvable Packets (160 mg) based on age in months
    elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
        if 48 <= age <= 59:
            return "Dosage: 2 packets (320 mg)"
        elif 60 <= age <= 71:
            return "Dosage: 2 packets (320 mg)"
        elif 72 <= age <= 95:
            return "Dosage: 3 packets (480 mg)"

    # Set dosages for Adult's Acetaminophen Tablets (325 mg) based on age in months
    elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
        if 48 <= age <= 59:
            return "Dosage: 1 tablet (325 mg)"
        elif 60 <= age <= 71:
            return "Dosage: 1 tablet (325 mg)"
        elif 72 <= age <= 95:
            return "Dosage: 1.5 tablets (487.5 mg)"
        elif age >= 96:
            return "Dosage: 2 tablets (650 mg)"

    # Set dosages for Adult's Acetaminophen Tablets (500 mg) based on age in months
    elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
        if 72 <= age <= 95:
            return "Dosage: 1 tablet (500 mg)"
        elif age >= 96:
            return "Dosage: 1 tablet (500 mg)"

    # If no valid dosage is found, return a warning message
    return f"Warning: {formulation} is not typically used for this age. Please check your selection."

# Streamlit interface
st.title("Pediatric Acetaminophen Dosing Calculator")

# User selects dosing by weight or age
dosing_choice = st.selectbox("Would you like to dose by Weight or Age?", ["Weight", "Age"])

# If dosing by weight
if dosing_choice == "Weight":
    # Get weight input in pounds or kilograms with a simple "0" starting value
    unit = st.selectbox("Select units:", ["Pounds", "Kilograms"])
    weight = st.number_input("Enter the patient's weight:", min_value=0.0, step=0.1, format="%g")

    # Convert pounds to kilograms if needed
    if unit == "Pounds":
        weight_kg = weight * 0.453592
    else:
        weight_kg = weight
    age = None  # Age not needed if dosing by weight

# If dosing by age
elif dosing_choice == "Age":
    # Get age input and allow selection between months and years
    age_unit = st.selectbox("Enter age in:", ["Months", "Years"])
    if age_unit == "Years":
        age = st.number_input("Enter the patient's age in years:", min_value=0, step=1) * 12
    else:
        age = st.number_input("Enter the patient's age in months:", min_value=0, step=1)
    weight_kg = None  # Weight not needed if dosing by age

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
        result = get_dosage_by_weight(weight_kg, formulation)
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
    - [Dosing information sourced from HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Acetaminophen-for-Fever-and-Pain.aspx)
    """)

