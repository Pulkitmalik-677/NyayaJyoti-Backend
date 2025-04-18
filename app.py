from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from docx import Document
import pandas as pd
import os
import tempfile

app = Flask(__name__)
CORS(app)

CSV_PATH = 'datasets/Verified_50_Loan_Clause_Examples_final_fixed.csv'
TEMPLATE_PATH = 'templates/loan_agreement.docx'

def fill_placeholders(doc, context):
    for p in doc.paragraphs:
        for key, value in context.items():
            if f"[{key}]" in p.text:
                p.text = p.text.replace(f"[{key}]", str(value))
    return doc

@app.route('/generate', methods=['POST'])
def generate_agreement():
    data = request.json
    if not data:
        return jsonify({"error": "No input data received"}), 400

    try:
        df = pd.read_csv(CSV_PATH)
        context = {k: v for k, v in data.items()}

        special_clause = context.get("Special_Clauses", "")
        context["Special_Clauses"] = special_clause if special_clause else "N/A"

        doc = Document(TEMPLATE_PATH)
        filled_doc = fill_placeholders(doc, context)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            filled_doc.save(tmp.name)
            tmp_path = tmp.name

        return send_file(tmp_path, as_attachment=True, download_name="Loan_Agreement.docx")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return "Loan Agreement AI Backend is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
