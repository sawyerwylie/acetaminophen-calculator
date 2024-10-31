import streamlit as st

# Concentrations for formulations
formulation_concentrations = {
    "Infant's Acetaminophen (160 mg / 5 mL)": (160, 'mg/5 mL'),
    "Children's Acetaminophen (160 mg / 5 mL)": (160, 'mg/5 mL'),
    "Children's Acetaminophen Chewables (160 mg)": (160, 'mg/tablet'),
    "Children's Acetaminophen Dissolvable Packets (160 mg)": (160, 'mg/packet'),
    "Adult's Acetaminophen Tablets (325 mg)": (325, 'mg/tablet'),
    "Adult's Acetaminophen Tablets (500 mg)": (500, 'mg/tablet')
}

# Function to get dosage by weight
def get_dosage_by_weight(weight, formulation):
    # Initialize dosage
    dosage_mL = None
    dosage_mg = None
    
    # Determine dosage based on weight and formulation
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
            dosage_mg = 1 * 160
    elif 36 <= weight <= 47:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 7.5
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 
