
[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-green?logo=streamlit)](https://marketingstrategyabtesting-eu4hug4vbgnflcdfxxdcyh.streamlit.app/)

---

# Marketing Strategy A/B Testing + Conversion Prediction (ML - Logistic Regression model)

---

## 📈 Project Overview

This project analyzes marketing effectiveness through A/B Testing between Public Service Announcements (PSAs) and a new Paid Ad strategy.  
It then builds a Logistic Regression model to **predict customer conversion probability** based on user behavior.

Deployed as a fully interactive **Streamlit Dashboard**.

---

## 🛠 Technologies

- Python
- Streamlit
- Pandas, Scikit-learn, Matplotlib, Seaborn
- Machine Learning (Logistic Regression)

---

## 📊 Key Features

- **A/B Testing Analysis** (Statistical significance testing)
- **Conversion Rates by Hour and Day**
- **Logistic Regression-based Conversion Probability Prediction**
- **Business Impact Estimation in Revenue**
- **Model Evaluation with Confusion Matrix, ROC Curve, Classification Report**

---

## 📂 Project Structure

AB_testing+ML_Prediction/ 

├── streamlit_app.py                                                           
├── train_model.py                                                                                      
├── Marketing_AB_Testing.ipynb                                                                                  
├── data/                                                                                                                  
│ └── Marketing_AB_Testing.csv                                                                                                       
├── images/                                                                                                                           
│ ├── AB Testing Groups plot.png                                                                                                                      
│ ├── Conversion_by_hour&Conversion_by_day.png                                                                                                              
│ ├── LogisticReg_confusion_matrix.png                                                                                                           
│ ├── LogisticReg_roc_curve.png                                                                                                               
│ └── LogisticReg_classification_report.png                                                                                                  
├── model.pkl                                                                                                                                     
├── input_columns.pkl                                                                                                                                    
├── README.md                                                                                                                                                   
├── requirements.txt                                                                                                                      
├── LICENSE                                         

---

## 📋 How to Run Locally?

1. Clone this repo:
  
   git clone https://github.com/SweetySeelam2/Marketing_Strategy_AB_Testing.git

2. Navigate to the project:

   cd AB_testing+ML_Prediction

3. Install libraries:

   pip install -r requirements.txt

4. Run Streamlit app:

   streamlit run streamlit_app.py

✅ Open your local browser at http://localhost:8501/.

---

## 📈 Logistic Regression Results

- AUC Score (ROC Curve): 0.85

- Accuracy: 86%

- Recall for Converters (Class 1): 69%

- Precision: 12%

- Revenue Captured in Test Sample: ~$155,550

---

## 💡 Business Impact

The Logistic Regression model correctly identified 69% of potential converters.

Over $150K in revenue captured just within the test group.

Compared to Random Forest, Logistic Regression is twice as profitable and far more reliable.

High Recall ensures valuable customers are not missed.

Enables smarter ad spending, personalized marketing, and higher ROI.

---

## 🔗 Live App

👉 Launch Streamlit App (https://marketingstrategyabtesting-eu4hug4vbgnflcdfxxdcyh.streamlit.app/)

## 📬 Project Links

GitHub: https://github.com/SweetySeelam2/Marketing_Strategy_AB_Testing

⭐ Star this repo if you found it useful!

---

## 👩‍💼 About the Author    

**Sweety Seelam** | Business Analyst | Aspiring Data Scientist | Passionate about building end-to-end ML solutions for real-world problems                                                                                                      
                                                                                                                                           
Email: sweetyseelam2@gmail.com                                                   

🔗 **Profile Links**                                                                                                                                                                       
[Portfolio Website](https://sweetyseelam2.github.io/SweetySeelam.github.io/)                                                         
[LinkedIn](https://www.linkedin.com/in/sweetyrao670/)                                                                   
[GitHub](https://github.com/SweetySeelam2)                                                             
[Medium](https://medium.com/@sweetyseelam)

---

## 🔐 Proprietary & All Rights Reserved
© 2025 Sweety Seelam. All rights reserved.

This project, including its source code, trained models, datasets (where applicable), visuals, and dashboard assets, is protected under copyright and made available for educational and demonstrative purposes only.

Unauthorized commercial use, redistribution, or duplication of any part of this project is strictly prohibited.
