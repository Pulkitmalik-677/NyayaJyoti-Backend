
---

# 🧠 Nyaya Jyoti – AI-Powered Legal Document Generator (Backend)

Welcome to the **backend repository** of **Nyaya Jyoti**, a Design Thinking & Innovation project developed at Bennett University. This repository contains the codebase for AI-driven legal document generation, trained using dynamic clause templates and a clause-generation language model (GPT-Neo 1.3B).

---

## 📁 Folder Structure

Each folder in this repository corresponds to a specific legal document type. Every folder contains:

- A **.ipynb notebook** (Google Colab ready) – For document generation and clause matching
- A **.csv file** – Prompt registry for legal clause templates with parameter mappings
- A **.docx template** – The base template used for final document generation with placeholders

---

### 🔹 `Loan agreement/`
- **Purpose:** Generates a formal loan agreement between lender and borrower.
- **Features:**
  - Clause injection from CSV prompt registry
  - Special clause generation using GPT-Neo
  - Parameterized placeholder filling (e.g., Loan Amount, Interest Rate, Borrower Name)
  - Dynamic document creation and download

---

### 🔹 `friendly loan/`
- **Purpose:** Drafts a legal notice for friendly loan recovery.
- **Features:**
  - Includes advocate vs. lender mode toggle
  - GPT-based fallback for unmatched special requests
  - Clause matching from CSV clause registry
  - Legally formatted notice output in `.docx`

---

### 🔹 `Lease rent agreement/`
- **Purpose:** Automates rental/lease agreement between landlord and tenant.
- **Features:**
  - Property-related clause generation
  - Support for tenant rights, rent duration, security deposit clauses
  - Interactive chatbot-style input flow

---

### 🔹 `House sell/`
- **Purpose:** Generates a **house sale deed agreement** between buyer and seller.
- **Features:**
  - Custom sale clauses, price terms, possession date
  - Dynamic clause prompting
  - Legally formatted `.docx` with editable terms

---

### 🔹 `will/`
- **Purpose:** Creates a personal **Last Will & Testament**.
- **Features:**
  - Clauses for executor, property distribution, legal declarations
  - GPT clause fallback when no registry match is found
  - Fully personalized based on family structure

---

### 📄 `requirements.txt`
- **Purpose:** Contains Python dependencies needed to run the notebooks locally or on Colab.
- **Includes:**
  - `transformers`, `sentence-transformers`, `python-docx`, `torch`, `pandas`, etc.

---

## 🚀 Usage Instructions

> Each folder is **self-contained** and can be run independently.

1. Open the respective `.ipynb` file on **Google Colab** or your preferred Python environment.
2. Upload the `template.docx` and `clauses.csv` file when prompted.
3. The chatbot will guide you through a Q&A to populate document fields.
4. Optionally add a **Special Clause** using natural language – the AI will handle it.
5. Final `.docx` will be generated and made available for download.

---

## 👨‍💻 Contributors

- **Pulkit Malik** – AI model development & backend integration  
- **Bilal Sadiq** – Frontend & deployment  
- **Sanskar Sengar** – Blockchain document verification  
- **Ansh Sindhu** – Dataset collection and preprocessing

---

## 🌐 Live Demo Integration

Each backend model is designed to work with the **Nyaya Jyoti Website** frontend:
> [https://github.com/bilalsadiq03/nyaya-jyoti.git](https://github.com/bilalsadiq03/nyaya-jyoti.git)

Signature model :-
https://github.com/SanskarSinghSengar/signature-verification-system.git

---

## 📌 Note

All notebooks are currently **Colab-compatible** due to GPU and RAM requirements. Final production hosting will include Render/HuggingFace integration and dynamic API endpoints.

