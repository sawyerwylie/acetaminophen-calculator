import streamlit as st

# Define functions to get dosage based on weight or age
def get_dosage_by_weight(weight, formulation):
    # Define weight ranges and dosages for each formulation
    if formulation == "Infant's Acetaminophen (160 mg / 5 mL)":
        if 3.00 <= weight <= 5.00:
            return "1.25 mL", "40 mg"
        elif 5.01 <= weight <= 7.99:
            return "2.5 mL", "80 mg"
        elif 8.00 <= weight <= 10.99:
            return "3.75 mL", "120 mg"

    elif formulation == "Children's Acetaminophen (160 mg / 5 mL)":
        if 11.00 <= weight <= 15.99:
            return "5 mL", "160 mg"
        elif 16.00 <= weight <= 21.99:
            return "7.5 mL", "240 mg"
        elif 22.00 <= weight <= 26.99:
            return "10 mL", "320 mg"
        elif 27.00 <= weight <= 32.99:
            return "12.5 mL", "400 mg"
        elif 33.00 <= weight <= 43.99:
            return "15 mL", "480 mg"
        elif weight >= 44.00:
            return "20 mL", "640 mg"

    elif formulation == "Children's Acetaminophen Chewables (160 mg)":
        if 11.00 <= weight <= 15.99:
            return "1 tablet", "160 mg"
        elif 16.00 <= weight <= 21.99:
            return "1.5 tablets", "240 mg"
        elif 22.00 <= weight <= 26.99:
            return "2 tablets", "320 mg"
        elif 27.00 <= weight <= 32.99:
            return "2.5 tablets", "400 mg"
        elif 33.00 <= weight <= 43.99:
            return "3 tablets", "480 mg"
        elif weight >= 44.00:
            return "4 tablets", "640 mg"

    elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
        if 22.00 <= weight <= 26.99:
            return "2 packets", "320 mg"
        elif 27.00 <= weight <= 32.99:
            return "2 packets", "320 mg"
        elif 33.00 <= weight <= 43.99:
            return "3 packets", "480 mg"

    elif formulation == "Adult's Acetaminophen Tablets (325 mg)":
        if 22.00 <= weight <= 26.99:
            return "1 tablet", "325 mg"
        elif 27.00 <= weight <= 32.99:
            return "1 tablet", "325 mg"
        elif 33.00 <= weight <= 43.99:
            return "1.5 tablets", "487.5 mg"
        elif weight >= 44.00:
            return "2 tablets", "650 mg"

    elif formulation == "Adult's Acetaminophen Tablets (500 mg)":
        if 33.00 <= weight <= 43.99:
            return "1 tablet", "500 mg"
        elif weight >= 44.00:
            return "1 tablet", "500 mg"

    return "Dose not available", "Please consult a healthcare provider."

# Streamlit app layout
st.title("Pediatric Acetaminophen Dosing Calculator")

# Select dosing type
choice = st.selectbox("Select Dosing by Weight or Age", ["Weight", "Age"])

# Main input for dosing by weight
if choice == "Weight":
    weight = st.number_input("Enter the patient's weight in kg:", min_value=0.0, step=0.01)
    formulation = st.selectbox("Select the formulation", [
        "Infant's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen Chewables (160 mg)",
        "Children's Acetaminophen Dissolvable Packets (160 mg)",
        "Adult's Acetaminophen Tablets (325 mg)",
        "Adult's Acetaminophen Tablets (500 mg)"
    ])

    if st.button("Calculate Dosage"):
        dosage, dose = get_dosage_by_weight(weight, formulation)
        st.write(f"Dosage: {dosage} ({dose})")

# Main input for dosing by age
elif choice == "Age":
    age_years = st.number_input("Enter the patient's age in years:", min_value=0, step=1)
    age_months = age_years * 12
    formulation = st.selectbox("Select the formulation", [
        "Infant's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen (160 mg / 5 mL)",
        "Children's Acetaminophen Chewables (160 mg)",
        "Children's Acetaminophen Dissolvable Packets (160 mg)",
        "Adult's Acetaminophen Tablets (325 mg)",
        "Adult's Acetaminophen Tablets (500 mg)"
    ])

    if st.button("Calculate Dosage"):
        # Converting age to months and fetching dosage based on age ranges
        dosage, dose = get_dosage_by_weight(age_months, formulation) # Implement get_dosage_by_age if needed
        st.write(f"Dosage: {dosage} ({dose})")

st.write("Note: Dosing information is sourced from [HealthyChildren.org](https://www.healthychildren.org/English/safety-prevention/at-home/medication-safety/Pages/Acetaminophen-for-Fever-and-Pain.aspx).")
