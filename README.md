# 🤖 AI Applications in Software Engineering

This project demonstrates theoretical knowledge, practical implementation, and ethical reflection on the use of AI in software engineering. Tasks include AI-assisted code generation, automated testing, predictive modeling, and proposing an innovative AI tool.

---

## 📚 Contents

1. [Theoretical Analysis](#theoretical-analysis)
2. [Practical Implementation](#practical-implementation)
   - [AI Code Completion](#ai-code-completion)
   - [Automated Testing with Selenium](#automated-testing-with-selenium)
   - [Predictive Analytics (ML Model)](#predictive-analytics-ml-model)
3. [Ethical Reflection](#ethical-reflection)
4. [Innovation Proposal](#innovation-proposal)
5. [Setup Instructions](#setup-instructions)
6. [Screenshots](#screenshots)

---

## 🧠 Theoretical Analysis

- Benefits and limitations of AI code generation tools like GitHub Copilot.
- Comparison between supervised and unsupervised learning for bug detection.
- Importance of bias mitigation in AI-powered personalization.
- AIOps case study highlighting automated deployment benefits.

---

## 💻 Practical Implementation

### AI Code Completion

Python function to sort a list of dictionaries by key:
- ✅ Copilot-suggested version using `sorted()`
- ✅ Manual implementation using nested loops
- ✅ 200-word analysis comparing both

### Automated Testing with Selenium

Automates login test cases using:
- Valid and invalid credentials
- AI-enhanced testing discussion
- Test script and analysis

> 📎 *Screenshots of results provided in report.*

### Predictive Analytics (ML Model)

- Dataset: Kaggle Breast Cancer Dataset
- Preprocessing, training using Random Forest
- Evaluation: Accuracy & F1 Score
- Python code included

---

## 🤖 Ethical Reflection

- Identified dataset bias (e.g., gender imbalance)
- Fairness techniques from IBM AI Fairness 360
- Reflection on ethical deployment in resource allocation

---

## 🧪 Innovation Proposal

### 🔧 Tool: `AutoDocAI`

**Purpose**: Automatically generate Python documentation using NLP and AST.  
**Workflow**:
1. Parse code → extract function and structure
2. Use AI model to summarize logic
3. Output docstrings and Markdown

**Impact**:
- Saves time
- Improves consistency and maintainability

---

## ⚙️ Setup Instructions

```bash
# Install dependencies
pip install pandas scikit-learn selenium

# Run Python scripts
python sort_comparison.py
python selenium_login_test.py
python breast_cancer_model.py
