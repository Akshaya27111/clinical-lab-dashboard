
def diabetes_module_full(labs):
    result = {}

    fbs = labs.get("fbs")
    ppbs = labs.get("ppbs")
    rbs = labs.get("rbs")
    hba1c = labs.get("hba1c")
    c_peptide = labs.get("c_peptide")
    urine_ketones = labs.get("urine_ketones")

    # FBS
    if fbs is not None:
        if fbs >= 126:
            result["FBS"] = "Diabetes range"
        elif 100 <= fbs < 126:
            result["FBS"] = "Prediabetes"
        else:
            result["FBS"] = "Normal"

    # PPBS
    if ppbs is not None:
        if ppbs >= 200:
            result["PPBS"] = "Diabetes range"
        elif 140 <= ppbs < 200:
            result["PPBS"] = "Prediabetes"
        else:
            result["PPBS"] = "Normal"

    # HbA1c
    if hba1c is not None:
        if hba1c >= 6.5:
            result["HbA1c"] = "Diabetes range"
        elif 5.7 <= hba1c < 6.5:
            result["HbA1c"] = "Prediabetes"
        else:
            result["HbA1c"] = "Normal"

    # Type suggestion
    if c_peptide is not None:
        if c_peptide < 0.6:
            result["Type Suggestion"] = "Possible Type 1"
        elif c_peptide > 1.8:
            result["Type Suggestion"] = "Likely Type 2"
        else:
            result["Type Suggestion"] = "Indeterminate"

    if urine_ketones:
        result["Ketosis Risk"] = "Ketones detected — DKA risk"

    return result if result else {"status": "No abnormalities detected."}
def cbc_module_advanced(labs, gender="female"):

    result = {}

    hemoglobin = labs.get("hemoglobin")
    rbc = labs.get("rbc")
    hematocrit = labs.get("hematocrit")
    mcv = labs.get("mcv")
    mch = labs.get("mch")
    mchc = labs.get("mchc")
    rdw = labs.get("rdw")

    wbc = labs.get("wbc")
    neutrophils = labs.get("neutrophils")
    lymphocytes = labs.get("lymphocytes")
    eosinophils = labs.get("eosinophils")
    platelets = labs.get("platelets")

    # Hemoglobin
    if hemoglobin is not None:
        if (gender == "male" and hemoglobin < 13) or \
           (gender == "female" and hemoglobin < 12):
            result["Hemoglobin"] = "Low — Anemia detected"
        elif hemoglobin > 17:
            result["Hemoglobin"] = "High — Polycythemia suspected"
        else:
            result["Hemoglobin"] = "Normal"

    # RBC Count
    if rbc is not None:
        if (gender == "male" and rbc < 4.5) or \
           (gender == "female" and rbc < 4.0):
            result["RBC Count"] = "Low — Possible anemia"
        elif rbc > 6.0:
            result["RBC Count"] = "High — Possible polycythemia"
        else:
            result["RBC Count"] = "Normal"

    # Hematocrit
    if hematocrit is not None:
        if (gender == "male" and hematocrit < 41) or \
           (gender == "female" and hematocrit < 36):
            result["Hematocrit"] = "Low — Anemia"
        elif hematocrit > 53:
            result["Hematocrit"] = "High — Polycythemia"
        else:
            result["Hematocrit"] = "Normal"

    # RBC Indices
    if mcv is not None:
        if mcv < 80:
            result["MCV"] = "Low — Microcytic anemia"
        elif mcv > 100:
            result["MCV"] = "High — Macrocytic anemia"
        else:
            result["MCV"] = "Normal"

    if mch is not None:
        if mch < 27:
            result["MCH"] = "Low — Hypochromia"
        else:
            result["MCH"] = "Normal"

    if mchc is not None:
        if mchc < 32:
            result["MCHC"] = "Low — Hypochromic anemia"
        else:
            result["MCHC"] = "Normal"

    if rdw is not None:
        if rdw > 15:
            result["RDW"] = "High — Anisocytosis (Iron deficiency likely)"
        else:
            result["RDW"] = "Normal"

    # WBC Count
    if wbc is not None:
        if wbc > 11000:
            result["WBC"] = "High — Leukocytosis (Infection / Inflammation)"
        elif wbc < 4000:
            result["WBC"] = "Low — Leukopenia"
        else:
            result["WBC"] = "Normal"

    # Differential Count
    if neutrophils is not None:
        if neutrophils > 70:
            result["Neutrophils"] = "High — Bacterial infection likely"
        elif neutrophils < 40:
            result["Neutrophils"] = "Low — Possible viral infection"
        else:
            result["Neutrophils"] = "Normal"

    if lymphocytes is not None:
        if lymphocytes > 40:
            result["Lymphocytes"] = "High — Viral infection likely"
        elif lymphocytes < 20:
            result["Lymphocytes"] = "Low"
        else:
            result["Lymphocytes"] = "Normal"

    if eosinophils is not None:
        if eosinophils > 6:
            result["Eosinophils"] = "High — Allergy / Parasitic infection"
        else:
            result["Eosinophils"] = "Normal"

    # Platelets
    if platelets is not None:
        if platelets < 150000:
            result["Platelets"] = "Low — Thrombocytopenia"
        elif platelets > 450000:
            result["Platelets"] = "High — Thrombocytosis"
        else:
            result["Platelets"] = "Normal"

    return result if result else {"status": "No abnormalities detected."}
def thyroid_module_advanced(labs):

    result = {}

    tsh = labs.get("tsh")
    ft3 = labs.get("ft3")
    ft4 = labs.get("ft4")
    anti_tpo = labs.get("anti_tpo")
    trab = labs.get("trab")

    # TSH Interpretation
    if tsh is not None:
        if tsh > 4.0:
            result["TSH"] = "Elevated — Possible hypothyroidism"
        elif tsh < 0.4:
            result["TSH"] = "Low — Possible hyperthyroidism"
        else:
            result["TSH"] = "Normal"

    # Overt / Subclinical Patterns
    if tsh is not None and ft4 is not None:

        if tsh > 4.0 and ft4 < 0.8:
            result["Diagnosis"] = "Overt Hypothyroidism"
        elif tsh > 4.0 and 0.8 <= ft4 <= 1.8:
            result["Diagnosis"] = "Subclinical Hypothyroidism"
        elif tsh < 0.4 and ft4 > 1.8:
            result["Diagnosis"] = "Overt Hyperthyroidism"
        elif tsh < 0.4 and 0.8 <= ft4 <= 1.8:
            result["Diagnosis"] = "Subclinical Hyperthyroidism"
        elif tsh < 0.4 and ft4 < 0.8:
            result["Diagnosis"] = "Secondary (Central) Hypothyroidism"

    # FT3 specific check
    if ft3 is not None:
        if ft3 > 4.2:
            result["FT3"] = "Elevated — Possible T3 toxicosis"
        else:
            result["FT3"] = "Normal"

    # Autoimmune markers
    if anti_tpo is not None:
        if anti_tpo > 35:
            result["Anti-TPO"] = "Positive — Autoimmune thyroiditis likely"
        else:
            result["Anti-TPO"] = "Negative"

    if trab is not None:
        if trab > 1.75:
            result["TRAb"] = "Positive — Graves' disease likely"
        else:
            result["TRAb"] = "Negative"

    return result if result else {"status": "No abnormalities detected."}
def lipid_module_advanced(labs):

    result = {}

    total_cholesterol = labs.get("total_cholesterol")
    ldl = labs.get("ldl")
    hdl = labs.get("hdl")
    triglycerides = labs.get("triglycerides")

    # =========================
    # Total Cholesterol
    # =========================
    if total_cholesterol is not None:
        if total_cholesterol >= 240:
            result["Total Cholesterol"] = "High"
        elif total_cholesterol >= 200:
            result["Total Cholesterol"] = "Borderline High"
        else:
            result["Total Cholesterol"] = "Desirable"

    # =========================
    # LDL Classification
    # =========================
    if ldl is not None:
        if ldl >= 190:
            result["LDL"] = "Very High"
        elif ldl >= 160:
            result["LDL"] = "High"
        elif ldl >= 130:
            result["LDL"] = "Borderline High"
        else:
            result["LDL"] = "Optimal/Near Optimal"

    # =========================
    # HDL Classification
    # =========================
    if hdl is not None:
        if hdl < 40:
            result["HDL"] = "Low"
        elif hdl >= 60:
            result["HDL"] = "Protective"
        else:
            result["HDL"] = "Normal"

    # =========================
    # Triglycerides
    # =========================
    if triglycerides is not None:
        if triglycerides >= 500:
            result["Triglycerides"] = "Very High"
        elif triglycerides >= 200:
            result["Triglycerides"] = "High"
        elif triglycerides >= 150:
            result["Triglycerides"] = "Borderline High"
        else:
            result["Triglycerides"] = "Normal"

    # =========================
    # Integrated Risk Pattern
    # =========================
    if ldl is not None and hdl is not None:
        if ldl >= 160 and hdl < 40:
            result["Integrated Risk"] = "Atherogenic lipid pattern"

    return result if result else {"status": "No abnormalities detected."}
def micronutrient_module_advanced(labs):

    result = {}

    vitamin_d = labs.get("vitamin_d")
    b12 = labs.get("b12")
    folate = labs.get("folate")
    ferritin = labs.get("ferritin")
    iron = labs.get("iron")
    calcium = labs.get("calcium")
    magnesium = labs.get("magnesium")
    zinc = labs.get("zinc")

    # =========================
    # Vitamin D
    # =========================
    if vitamin_d is not None:
        if vitamin_d < 20:
            result["Vitamin D"] = "Deficient"
        elif vitamin_d < 30:
            result["Vitamin D"] = "Insufficient"
        else:
            result["Vitamin D"] = "Sufficient"

    # =========================
    # Vitamin B12
    # =========================
    if b12 is not None:
        if b12 < 200:
            result["Vitamin B12"] = "Deficient"
        elif b12 < 300:
            result["Vitamin B12"] = "Borderline"
        else:
            result["Vitamin B12"] = "Normal"

    # =========================
    # Folate
    # =========================
    if folate is not None and folate < 3:
        result["Folate"] = "Deficient"

    # =========================
    # Iron Stores
    # =========================
    if ferritin is not None and ferritin < 30:
        result["Ferritin"] = "Low iron stores"

    if iron is not None and iron < 60:
        result["Serum Iron"] = "Low"

    # =========================
    # Electrolyte Micronutrients
    # =========================
    if magnesium is not None and magnesium < 1.7:
        result["Magnesium"] = "Low"

    if zinc is not None and zinc < 70:
        result["Zinc"] = "Low"

    return result if result else {"status": "No abnormalities detected."}
def pcod_module_full(labs):

    result = {}

    lh = labs.get("lh")
    fsh = labs.get("fsh")
    testosterone = labs.get("testosterone")
    dheas = labs.get("dheas")
    prolactin = labs.get("prolactin")
    amh = labs.get("amh")
    ovarian_volume = labs.get("ovarian_volume")
    follicle_count = labs.get("follicle_count")

    # LH/FSH ratio
    if lh and fsh:
        ratio = lh / fsh
        if ratio > 2:
            result["LH/FSH Ratio"] = "Elevated — PCOD suspicion"

    # Androgen excess
    if testosterone and testosterone > 70:
        result["Testosterone"] = "Elevated — Hyperandrogenism"

    if dheas and dheas > 350:
        result["DHEAS"] = "Elevated"

    # AMH
    if amh and amh > 4:
        result["AMH"] = "Elevated — Ovarian reserve high (PCOD pattern)"

    # Ultrasound criteria
    if ovarian_volume and ovarian_volume > 10:
        result["Ovarian Volume"] = "Increased — PCOD morphology"

    if follicle_count and follicle_count >= 12:
        result["Follicle Count"] = "Polycystic ovarian morphology"

    if prolactin and prolactin > 25:
        result["Prolactin"] = "Elevated — Rule out hyperprolactinemia"

    return result if result else {"status": "No abnormalities detected."}
def pcos_module_advanced(labs):

    result = {}

    # --------------------
    # Hormonal Parameters
    # --------------------
    lh = labs.get("lh")                          # IU/L
    fsh = labs.get("fsh")                        # IU/L
    testosterone = labs.get("testosterone")      # ng/dL
    free_testosterone = labs.get("free_testosterone")
    dheas = labs.get("dheas")                    # µg/dL
    prolactin = labs.get("prolactin")            # ng/mL
    tsh = labs.get("tsh")                        # mIU/L

    # --------------------
    # Metabolic Parameters
    # --------------------
    fasting_glucose = labs.get("fasting_glucose")    # mg/dL
    fasting_insulin = labs.get("fasting_insulin")    # µIU/mL
    homa_ir = labs.get("homa_ir")

    # --------------------
    # LH / FSH Ratio
    # --------------------
    if lh is not None and fsh is not None and fsh != 0:
        lh_fsh_ratio = lh / fsh
        result["LH/FSH Ratio"] = round(lh_fsh_ratio, 2)

        if lh_fsh_ratio > 2:
            result["LH/FSH Interpretation"] = "Elevated — Suggestive of PCOS"
        else:
            result["LH/FSH Interpretation"] = "Normal"

    # --------------------
    # Androgens
    # --------------------
    if testosterone is not None:
        if testosterone > 60:
            result["Testosterone"] = "Elevated — Hyperandrogenism"
        else:
            result["Testosterone"] = "Normal"

    if free_testosterone is not None:
        if free_testosterone > 4.5:
            result["Free Testosterone"] = "Elevated — Hyperandrogenism"
        else:
            result["Free Testosterone"] = "Normal"

    if dheas is not None:
        if dheas > 350:
            result["DHEAS"] = "Elevated — Adrenal androgen excess possible"
        else:
            result["DHEAS"] = "Normal"

    # --------------------
    # Prolactin
    # --------------------
    if prolactin is not None:
        if prolactin > 25:
            result["Prolactin"] = "Elevated — Rule out hyperprolactinemia"
        else:
            result["Prolactin"] = "Normal"

    # --------------------
    # Thyroid (Exclusion)
    # --------------------
    if tsh is not None:
        if tsh > 4.0:
            result["TSH"] = "Elevated — Hypothyroidism may mimic PCOS"
        else:
            result["TSH"] = "Normal"

    # --------------------
    # Insulin Resistance
    # --------------------
    if homa_ir is not None:
        if homa_ir > 2.5:
            result["Insulin Resistance"] = "Present — Common in PCOS"
        else:
            result["Insulin Resistance"] = "Absent"

    elif fasting_glucose is not None and fasting_insulin is not None:
        calculated_homa = (fasting_glucose * fasting_insulin) / 405
        result["HOMA-IR (Calculated)"] = round(calculated_homa, 2)

        if calculated_homa > 2.5:
            result["Insulin Resistance"] = "Present — Common in PCOS"
        else:
            result["Insulin Resistance"] = "Absent"

    # --------------------
    # Final Pattern Recognition
    # --------------------
    pcos_flags = 0

    if lh is not None and fsh is not None and (lh / fsh) > 2:
        pcos_flags += 1
    if testosterone is not None and testosterone > 60:
        pcos_flags += 1
    if homa_ir is not None and homa_ir > 2.5:
        pcos_flags += 1

    if pcos_flags >= 2:
        result["Diagnosis"] = "PCOS / PCOD Likely (Based on Lab Pattern)"
    else:
        result["Diagnosis"] = "PCOS Not Strongly Suggested by Labs Alone"

    return result if result else {"status": "No abnormalities detected."}
def liver_module_advanced(labs):

    result = {}

    # --------------------
    # Enzymes
    # --------------------
    ast = labs.get("ast")                    # U/L
    alt = labs.get("alt")                    # U/L
    alp = labs.get("alp")                    # U/L
    ggt = labs.get("ggt")                    # U/L

    # --------------------
    # Bilirubin
    # --------------------
    total_bilirubin = labs.get("total_bilirubin")    # mg/dL
    direct_bilirubin = labs.get("direct_bilirubin")  # mg/dL

    # --------------------
    # Synthetic Function
    # --------------------
    albumin = labs.get("albumin")            # g/dL
    inr = labs.get("inr")

    # --------------------
    # AST / ALT
    # --------------------
    if ast is not None:
        if ast > 40:
            result["AST"] = "Elevated — Hepatocellular injury possible"
        else:
            result["AST"] = "Normal"

    if alt is not None:
        if alt > 40:
            result["ALT"] = "Elevated — Hepatocellular injury possible"
        else:
            result["ALT"] = "Normal"

    # --------------------
    # AST / ALT Ratio
    # --------------------
    if ast is not None and alt is not None and alt != 0:
        ratio = ast / alt
        result["AST/ALT Ratio"] = round(ratio, 2)

        if ratio > 2:
            result["AST/ALT Interpretation"] = "Suggestive of alcoholic liver disease"

    # --------------------
    # ALP
    # --------------------
    if alp is not None:
        if alp > 120:
            result["ALP"] = "Elevated — Cholestasis or biliary obstruction possible"
        else:
            result["ALP"] = "Normal"

    # --------------------
    # GGT
    # --------------------
    if ggt is not None:
        if ggt > 60:
            result["GGT"] = "Elevated — Alcohol use or cholestatic injury possible"
        else:
            result["GGT"] = "Normal"

    # --------------------
    # Bilirubin
    # --------------------
    if total_bilirubin is not None:
        if total_bilirubin > 1.2:
            result["Total Bilirubin"] = "Elevated — Jaundice possible"
        else:
            result["Total Bilirubin"] = "Normal"

    if direct_bilirubin is not None:
        if direct_bilirubin > 0.3:
            result["Direct Bilirubin"] = "Elevated — Conjugated hyperbilirubinemia"
        else:
            result["Direct Bilirubin"] = "Normal"

    # --------------------
    # Albumin
    # --------------------
    if albumin is not None:
        if albumin < 3.5:
            result["Albumin"] = "Low — Reduced liver synthetic function"
        else:
            result["Albumin"] = "Normal"

    # --------------------
    # INR
    # --------------------
    if inr is not None:
        if inr > 1.2:
            result["INR"] = "Prolonged — Impaired liver synthetic function"
        else:
            result["INR"] = "Normal"

    # --------------------
    # Pattern Recognition
    # --------------------
    if ast is not None and alt is not None:
        if ast > 40 and alt > 40:
            result["Pattern"] = "Hepatocellular injury pattern"

    if alp is not None and ggt is not None:
        if alp > 120 and ggt > 60:
            result["Pattern"] = "Cholestatic injury pattern"

    if ast is not None and alt is not None:
        if ast > 2 * alt and ast > 40:
            result["Pattern"] = "Alcohol-related liver injury pattern"

    if albumin is not None and inr is not None:
        if albumin < 3.5 and inr > 1.2:
            result["Pattern"] = "Impaired liver synthetic function"

    return result if result else {"status": "No abnormalities detected."}
def renal_module_advanced(labs, gender="female"):

    result = {}

    # =========================
    # Parameter Extraction
    # =========================
    creatinine = labs.get("creatinine")      # mg/dL
    urea = labs.get("urea")                  # mg/dL
    bun = labs.get("bun")                    # mg/dL
    egfr = labs.get("egfr")                  # mL/min/1.73m2

    sodium = labs.get("sodium")              # mEq/L
    potassium = labs.get("potassium")        # mEq/L
    chloride = labs.get("chloride")          # mEq/L
    bicarbonate = labs.get("bicarbonate")    # mEq/L

    calcium = labs.get("calcium")            # mg/dL
    phosphorus = labs.get("phosphorus")      # mg/dL
    albumin = labs.get("albumin")            # g/dL

    urine_albumin = labs.get("urine_albumin")  # mg/g (ACR preferred)
    urine_rbc = labs.get("urine_rbc")
    urine_casts = labs.get("urine_casts")

    # =========================
    # Creatinine Interpretation (Gender-Specific)
    # =========================
    if creatinine is not None:
        if (gender == "male" and creatinine > 1.3) or \
           (gender == "female" and creatinine > 1.1):
            result["Creatinine"] = "Elevated — Reduced renal filtration suspected"
        else:
            result["Creatinine"] = "Normal"

    # =========================
    # Urea / BUN
    # =========================
    if urea is not None:
        result["Urea"] = "Elevated" if urea > 40 else "Normal"

    if bun is not None:
        result["BUN"] = "Elevated" if bun > 20 else "Normal"

    # =========================
    # KDIGO eGFR Staging
    # =========================
    if egfr is not None:
        if egfr < 15:
            stage = "G5 — Kidney Failure"
        elif egfr < 30:
            stage = "G4 — Severe Decrease"
        elif egfr < 45:
            stage = "G3b — Moderate-Severe"
        elif egfr < 60:
            stage = "G3a — Moderate"
        elif egfr < 90:
            stage = "G2 — Mild Decrease"
        else:
            stage = "G1 — Normal"

        result["CKD Stage (eGFR)"] = stage

    # =========================
    # Electrolytes
    # =========================
    if potassium is not None:
        if potassium > 5.5:
            result["Potassium"] = "Hyperkalemia — Cardiac risk"
        elif potassium < 3.5:
            result["Potassium"] = "Hypokalemia"
        else:
            result["Potassium"] = "Normal"

    if sodium is not None:
        if sodium < 135:
            result["Sodium"] = "Hyponatremia"
        elif sodium > 145:
            result["Sodium"] = "Hypernatremia"
        else:
            result["Sodium"] = "Normal"

    if bicarbonate is not None:
        if bicarbonate < 22:
            result["Acid-Base Status"] = "Metabolic Acidosis — Renal cause possible"
        else:
            result["Acid-Base Status"] = "Normal"

    # =========================
    # CKD Mineral Bone Disorder
    # =========================
    if phosphorus is not None and phosphorus > 4.5:
        result["Phosphorus"] = "Elevated — CKD-MBD risk"

    if calcium is not None and calcium < 8.5:
        result["Calcium"] = "Low — Possible CKD mineral imbalance"

    # =========================
    # Albumin (Synthetic / Nephrotic Clue)
    # =========================
    if albumin is not None:
        if albumin < 3.5:
            result["Albumin"] = "Low — Possible nephrotic loss or chronic disease"
        else:
            result["Albumin"] = "Normal"

    # =========================
    # Urine Findings
    # =========================
    if urine_albumin is not None:
        if urine_albumin >= 300:
            result["Albuminuria Category"] = "A3 — Severe"
        elif urine_albumin >= 30:
            result["Albuminuria Category"] = "A2 — Moderate"
        else:
            result["Albuminuria Category"] = "A1 — Normal/Mild"

    if urine_rbc is not None and urine_rbc > 3:
        result["Hematuria"] = "Present — Glomerular pathology possible"

    if urine_casts is not None:
        if urine_casts.lower() == "rbc":
            result["Casts"] = "RBC Casts — Suggests glomerulonephritis"
        elif urine_casts.lower() == "granular":
            result["Casts"] = "Granular Casts — Tubular injury"

    # =========================
    # Integrated Risk Pattern
    # =========================
    if egfr is not None and urine_albumin is not None:
        if egfr < 60 and urine_albumin >= 30:
            result["Integrated Risk"] = "CKD Confirmed (Reduced eGFR + Albuminuria)"

    return result if result else {"status": "No abnormalities detected."}

def run_all_modules(labs, gender="female"):
    analysis_results = {}
    analysis_results["Diabetes"] = diabetes_module_full(labs)
    analysis_results["CBC"] = cbc_module_advanced(labs, gender)
    analysis_results["Thyroid"] = thyroid_module_advanced(labs)
    # Using the advanced PCOS module and adapting its output for the prompt's expected format
    pcos_analysis = pcos_module_advanced(labs)
    if "Diagnosis" in pcos_analysis:
        analysis_results["PCOD"] = {"status": pcos_analysis["Diagnosis"]}
    elif pcos_analysis:
        analysis_results["PCOD"] = {"status": "Findings present, see detailed PCOD analysis."}
    else:
        analysis_results["PCOD"] = {"status": "No abnormalities detected."}


    analysis_results["Vitamins"] = micronutrient_module_advanced(labs)
    analysis_results["Renal"] = renal_module_advanced(labs, gender)
    analysis_results["Liver"] = liver_module_advanced(labs)
    analysis_results["Lipid"] = lipid_module_advanced(labs)
    return analysis_results
import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Clinical AI Dashboard",
    layout="wide",
    page_icon="🩺"
)

# ---------------- CUSTOM BLACK THEME ----------------
st.markdown("""
<style>

/* Whole app background */
.stApp {
    background-color: black;
}

/* Main text headings */
h1, h2, h3, h4, h5, h6, p {
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: black;
}

/* Sidebar labels */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: white !important;
}

/* Dropdown select box */
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}

/* Dropdown selected text */
div[data-baseweb="select"] span {
    color: black !important;
}

/* Dropdown menu options */
ul {
    background-color: white !important;
}

li {
    color: black !important;
    background-color: white !important;
}

/* Number input box */
.stNumberInput input {
    background-color: white !important;
    color: black !important;
}

/* Labels above inputs */
.stNumberInput label {
    color: white !important;
}

/* Buttons */
/* Generate button */
div.stButton > button {
    width: 100%;
    background-color: white !important;
    color: black !important;
    font-weight: bold !important;
    font-size: 16px !important;
    border-radius: 12px !important;
    padding: 10px !important;
    border: none !important;
}

/* Button text */
div.stButton > button p,
div.stButton > button span {
    color: black !important;
}

/* Output interpretation section */
[data-testid="stMarkdownContainer"] {
    color: white !important;
}

/* st.write outputs */
div[data-testid="stText"] {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🩺 Clinical Lab Interpretation Dashboard")
st.write("AI Powered Multi-System Lab Analysis")

# ---------------- SIDEBAR ----------------
module = st.sidebar.selectbox(
    "Choose Clinical Module",
    [
        "Diabetes",
        "CBC",
        "Thyroid",
        "PCOD",
        "Vitamins",
        "Renal",
        "Liver",
        "Lipid"
    ]
)

labs = {}

# ---------------- DIABETES ----------------
if module == "Diabetes":
    st.header("🩸 Diabetes Panel")
    col1, col2 = st.columns(2)

    with col1:
        labs["fbs"] = st.number_input("Fasting Blood Sugar (FBS)", min_value=0.0)
        labs["ppbs"] = st.number_input("PPBS", min_value=0.0)
        labs["rbs"] = st.number_input("Random Blood Sugar (RBS)", min_value=0.0)

    with col2:
        labs["hba1c"] = st.number_input("HbA1c", min_value=0.0)
        labs["fasting_insulin"] = st.number_input("Fasting Insulin", min_value=0.0)
        labs["homa_ir"] = st.number_input("HOMA-IR", min_value=0.0)

# ---------------- CBC ----------------
elif module == "CBC":
    st.header("🩸 Complete Blood Count")
    col1, col2 = st.columns(2)

    with col1:
        labs["hemoglobin"] = st.number_input("Hemoglobin")
        labs["rbc"] = st.number_input("RBC Count")
        labs["wbc"] = st.number_input("WBC Count")
        labs["platelets"] = st.number_input("Platelets")

    with col2:
        labs["hematocrit"] = st.number_input("Hematocrit")
        labs["mcv"] = st.number_input("MCV")
        labs["mch"] = st.number_input("MCH")
        labs["mchc"] = st.number_input("MCHC")

# ---------------- THYROID ----------------
elif module == "Thyroid":
    st.header("🦋 Thyroid Panel")
    labs["tsh"] = st.number_input("TSH")
    labs["ft3"] = st.number_input("Free T3")
    labs["ft4"] = st.number_input("Free T4")
    labs["anti_tpo"] = st.number_input("Anti-TPO")

# ---------------- PCOD ----------------
elif module == "PCOD":
    st.header("🌸 PCOD / PCOS Panel")
    col1, col2 = st.columns(2)

    with col1:
        labs["lh"] = st.number_input("LH")
        labs["fsh"] = st.number_input("FSH")
        labs["testosterone"] = st.number_input("Total Testosterone")
        labs["dheas"] = st.number_input("DHEAS")

    with col2:
        labs["prolactin"] = st.number_input("Prolactin")
        labs["amh"] = st.number_input("AMH")
        labs["fasting_glucose"] = st.number_input("Fasting Glucose")
        labs["fasting_insulin"] = st.number_input("Fasting Insulin")

# ---------------- VITAMINS ----------------
elif module == "Vitamins":
    st.header("💊 Vitamins / Micronutrients")
    labs["vitamin_d"] = st.number_input("Vitamin D")
    labs["b12"] = st.number_input("Vitamin B12")
    labs["folate"] = st.number_input("Folate")
    labs["ferritin"] = st.number_input("Ferritin")
    labs["iron"] = st.number_input("Iron")

# ---------------- RENAL ----------------
elif module == "Renal":
    st.header("🧪 Renal Panel")
    col1, col2 = st.columns(2)

    with col1:
        labs["urea"] = st.number_input("Urea")
        labs["bun"] = st.number_input("BUN")
        labs["creatinine"] = st.number_input("Creatinine")
        labs["egfr"] = st.number_input("eGFR")

    with col2:
        labs["sodium"] = st.number_input("Sodium")
        labs["potassium"] = st.number_input("Potassium")
        labs["phosphorus"] = st.number_input("Phosphorus")
        labs["urine_albumin"] = st.number_input("Urine ACR")

# ---------------- LIVER ----------------
elif module == "Liver":
    st.header("🫀 Liver Panel")
    labs["alt"] = st.number_input("ALT")
    labs["ast"] = st.number_input("AST")
    labs["alp"] = st.number_input("ALP")
    labs["ggt"] = st.number_input("GGT")
    labs["albumin"] = st.number_input("Albumin")
    labs["total_bilirubin"] = st.number_input("Total Bilirubin")

# ---------------- LIPID ----------------
elif module == "Lipid":
    st.header("❤️ Lipid Profile")
    labs["total_cholesterol"] = st.number_input("Total Cholesterol")
    labs["ldl"] = st.number_input("LDL")
    labs["hdl"] = st.number_input("HDL")
    labs["triglycerides"] = st.number_input("Triglycerides")

# ---------------- BUTTON ----------------
if st.button("🩺 Generate Clinical Interpretation"):

    result = run_all_modules(labs)

    st.subheader("📋 Interpretation Output")

    for section, values in result.items():
        st.write(f"### {section}")
        if isinstance(values, dict):
            for k, v in values.items():
                st.write(f"• {k}: {v}")
        else:
            st.write(values)