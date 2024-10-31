import streamlit as st

def get_dosage_by_weight(weight, formulation):
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
            dosage_mg = 1.5 * 160
    elif 48 <= weight <= 59:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 10
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 2 * 160
        elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
            dosage_mg = 2 * 160
    elif 60 <= weight <= 71:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 12.5
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 2.5 * 160
        elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
            dosage_mg = 2 * 160
    elif 72 <= weight <= 95:
        if formulation == "Children's Acetaminophen (160 mg / 5 mL)":
            dosage_mL = 15
        elif formulation == "Children's Acetaminophen Chewables (160 mg)":
            dosage_mg = 3 * 160
        elif formulation == "Children's Acetaminophen Dissolvable Packets (160 mg)":
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

    # Warning if dosage_mg or dosage_mL is None (not typically used for this weight)
    if 'dosage_mg' in locals():
        return f"Dosage: {round(dosage_mg / 1000, 2)} g"
    elif 'dosage_mL' in locals():
        return f"Dosage: {round(dosage_mL, 2)} mL"
    else:
