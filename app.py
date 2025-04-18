
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from docx import Document
import pandas as pd
import os
import tempfile
from clause_generator import get_best_clause

app = Flask(__name__)
CORS(app)

CSV_PATH = 'datasets/Verified_50_Loan_Clause_Examples_final_fixed.csv'
TEMPLATE_PATH = 'templates/loan_agreement.docx'

def fill_placeholders(doc, context):
    for p in doc.paragraphs:
        for key, value in context.items():
            if f"[{key}]" in p.text:
                print(f"📄 Updated Line:\n\nBefore: {p.text}\n\nAfter: {p.text.replace(f'[{key}]', str(value))}\n")
                p.text = p.text.replace(f"[{key}]", str(value))
    return doc

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data received"}), 400

        df = pd.read_csv(CSV_PATH)
        context = {k: v for k, v in data.items()}

        raw_clause = context.get("Special_Clauses", "").strip()
        if raw_clause and len(raw_clause.split()) < 10:
            best_clause = get_best_clause(raw_clause, df)
            print(f"📄 Inserted Special Clause: {best_clause}\n")
            context["Special_Clauses"] = best_clause
        elif not raw_clause:
            context["Special_Clauses"] = "N/A"

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
    return "Nyaya Jyoti AI Clause Backend is running."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
