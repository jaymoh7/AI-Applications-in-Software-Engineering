#2.1 Ai-Powered Code Completion
#AI-Suggested Version (GitHub Copilot) (Test 1)
def sort_dicts(data, key):
    return sorted(data, key=lambda x: x[key])

def manual_sort_dicts(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

sample_data = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 85}
]

print("AI-Suggested Version:", sort_dicts(sample_data, "score"))
print("Manual Version:", manual_sort_dicts(sample_data.copy(), "score"))


#2.2 Automated Testing with AI
#Selenium Test Script (Test 2)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔧 SETUP
options = Options()
# Comment this line below if you want to see the browser (non-headless)
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://github.com/login")
    time.sleep(2)  # wait for page to load

    # 🔑 Fill username
    username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    driver.execute_script("arguments[0].scrollIntoView(true);", username)
    time.sleep(0.5)
    username.clear()
    username.send_keys("your_username")  # Replace with your username

    # 🔐 Fill password using JS to avoid 'not interactable' issue
    password = driver.find_element(By.ID, "password")
    driver.execute_script("arguments[0].value = arguments[1];", password, "your_password")  # Replace with your password

    # ✅ Click login
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "commit")))
    login_button.click()

    # ⏳ Wait and print result
    time.sleep(5)
    print("✅ Login attempted. Current URL:", driver.current_url)

except Exception as e:
    print("❌ Error:", str(e))

finally:
    driver.quit()

#2.3 Predictive Analytics for Resource Allocation
#Modeling Using the Breast Cancer Dataset (Test 3)
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# ✅ Load dataset from sklearn
cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = pd.Series(cancer.target)  # Already binary: 0 = malignant, 1 = benign

# ✅ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"✅ Accuracy: {accuracy:.2f}")
print(f"✅ F1 Score: {f1:.2f}")

