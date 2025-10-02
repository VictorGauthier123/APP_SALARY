from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle XGBoost
model = joblib.load("best_xgb_model.pkl")
columns = model.feature_names_in_.tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    # Extraire dynamiquement les options depuis les colonnes du modèle
    countries = sorted([col.split('_', 1)[1] for col in columns if col.startswith("Country_")])
    languages = sorted([col for col in ["Python", "JavaScript", "SQL", "C++", "Java"] if col in columns])
    platforms = sorted([col for col in [
        "Amazon Web Services (AWS)", "Microsoft Azure", "Google Cloud"
    ] if col in columns])
    edlevels = sorted([col.split('_', 1)[1] for col in columns if col.startswith("EdLevel_")])
    orgsizes = sorted([col.split('_', 1)[1] for col in columns if col.startswith("OrgSize_")])
    devtypes = sorted([col.split('_', 1)[1] for col in columns if col.startswith("DevType_")])
    employments = sorted([col for col in [
        "Employed, full-time", "Employed, part-time", "Independent contractor, freelancer, or self-employed"
    ] if col in columns])
    industries = sorted([col.split('_', 1)[1] for col in columns if col.startswith("Industry_")])
    remotework = sorted([col.split('_', 1)[1] for col in columns if col.startswith("RemoteWork_")])

    if request.method == "POST":
        form = request.form  # garder le MultiDict

        # Initialiser toutes les colonnes à 0
        row = {col: 0 for col in columns}

        # Champ numérique
        row["YearsCodePro"] = float(form.get("YearsCodePro", 0))

        # Champs uniques
        for prefix in ["Country", "EdLevel", "OrgSize", "Industry", "RemoteWork"]:
            val = form.get(prefix)
            key = f"{prefix}_{val}"
            if key in row:
                row[key] = 1

        # Champs multichoix
        for field in ["DevType", "Employment", "LanguageHaveWorkedWith", "PlatformHaveWorkedWith"]:
            values = form.getlist(field)
            for val in values:
                key = f"{field}_{val}" if field == "DevType" else val
                if key in row:
                    row[key] = 1

        # Compte des plateformes
        if "PlatformCount" in row:
            row["PlatformCount"] = len(form.getlist("PlatformHaveWorkedWith"))

        # Construire DataFrame et faire la prédiction
        input_df = pd.DataFrame([row])
        prediction = round(model.predict(input_df)[0], 2)

    return render_template(
        "index.html",
        countries=countries,
        languages=languages,
        platforms=platforms,
        edlevels=edlevels,
        orgsizes=orgsizes,
        devtypes=devtypes,
        employments=employments,
        industries=industries,
        remotework=remotework,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)
