import streamlit as st

# Define function for dosing by weight and formulation
def get_dosage_by_weight(weight, formulation):
    # Initialize variables for dosage
    dosage_mL = None
    dosage_mg = None
    
    # Calculate the dose based on weight and formulation
    if 6 <= weight <= 11:
        dosage_mL = 1.25 if formulation == "Infant's Acetaminophen (160 mg / 5 mL)" else None
    elif 12 <= weight <= 17:
        dosage_mL = 2.5 if formulation == "Infant's Acetaminophen (160 mg / 5 mL)" else None
    elif 18 <= weight <= 23:
        dosage_mL = 3.75 if formulation == "Infant's Acetaminophen (160 mg / 5 mL)" else None
    elif 24 <= weight <= 35:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 5
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 160
    elif 36 <= weight <= 47:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 7.5
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 1.5 * 160
    elif 48 <= weight <= 59:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 10
        elif formulation in ["Children's Acetaminophen Chewables (160 mg)", "Children's Acetaminophen Dissolvable Packets (160 mg)"]:
            dosage_mg = 2 * 160
    elif 60 <= weight <= 71:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 12.5
        elif formulation in ["Children's Acetaminophen Chewables (160 mg)", "Children's Acetaminophen Dissolvable Packets (160 mg)"]:
            dosage_mg = 2.5 * 160
    elif 72 <= weight <= 95:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 15
        elif formulation in ["Children's Acetaminophen Chewables (160 mg)", "Children's Acetaminophen Dissolvable Packets (160 mg)"]:
            dosage_mg = 3 * 160
    elif weight >= 96:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 20
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 4 * 160
        elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
            dosage_mg = 2 * 325
        elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
            dosage_mg = 500

    # Return dosage in mL or mg, or warning if dosage not recommended
    if dosage_mg is not None:
        return f"Dosage: {round(dosage_mg / 1000, 2)} g ({dosage_mg} mg)"
    elif dosage_mL is not None:
        return f"Dosage: {round(dosage_mL, 2)} mL"
    else:
        return "Warning: This formulation is not typically used for the given weight."

# Streamlit integration for user inputs
st.title("Acetaminophen Dosing Calculator")

# Weight input with validation
weight = st.number_input("Enter the patient's weight (in lbs):", min_value=0.0, step=0.1)
formulation = st.selectbox("Select the formulation", [
    "Infant's Acetaminophen (160 mg / 5 mL)", 
    "Children's Acetaminophen (160 mg / 5 mL)",
    "Children's Acetaminophen Chewables (160 mg)", 
    "Children's Acetaminophen Dissolvable Packets (160 mg)", 
    "Adult's Acetaminophen Tablets (325 mg)", 
    "Adult's Acetaminophen Tablets (500 mg)"
])

if st.button("Calculate Dosage"):
    # Display the dosage based on weight and formulation
    result = get_dosage_by_weight(weight, formulation)
    st.write(result)
    # Additional information
    st.markdown("""
    **Important Instructions:**
    - Give every 4 to 6 hours if needed for fever or pain.
    - **DO NOT EXCEED 4 doses in 24 hours.**
    - Avoid using with other medicines containing acetaminophen.
    - [Dosing information sourced from HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Ibuprofen-for-Fever-and-Pain.aspx)
    """)
