
[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-green?logo=streamlit)](https://marketingstrategyabtesting-eu4hug4vbgnflcdfxxdcyh.streamlit.app/)

---

# Marketing Strategy A/B Testing + Conversion Prediction (ML - Logistic Regression model)

---

## 📈 Project Overview:

This project analyzes marketing effectiveness through A/B Testing between Public Service Announcements (PSAs) and a new Paid Ad strategy.  
It then builds a Logistic Regression model to **predict customer conversion probability** based on user behavior.

Deployed as a fully interactive **Streamlit Dashboard**.

---

## 🛠 Technologies Used:

- Python
- Streamlit
- Pandas, Scikit-learn, Matplotlib, Seaborn
- Machine Learning (Logistic Regression)

---

## 📊 Key Features:

- **A/B Testing Analysis** (Statistical significance testing)
- **Conversion Rates by Hour and Day**
- **Logistic Regression-based Conversion Probability Prediction**
- **Business Impact Estimation in Revenue**
- **Model Evaluation with Confusion Matrix, ROC Curve, Classification Report**

---

## 📂 Project Structure:

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

2. Navigate to project:

   cd AB_testing+ML_Prediction

3. Install libraries:

   pip install -r requirements.txt

4. Run Streamlit app:

   streamlit run streamlit_app.py

✅ Open your local browser at http://localhost:8501/.

---

## 📈 Logistic Regression Results:

- AUC Score (ROC Curve): 0.85

- Accuracy: 86%

- Recall for Converters (Class 1): 69%

- Precision: 12%

- Revenue Captured in Test Sample: ~$155,550

---

## 💡 Business Impact:

The Logistic Regression model correctly identified 69% of potential converters.

Over $150K in revenue captured just within the test group.

Compared to Random Forest, Logistic Regression is twice as profitable and far more reliable.

High Recall ensures valuable customers are not missed.

Enables smarter ad spending, personalized marketing, and higher ROI.

---

## 🔗 Live App:

👉 Launch Streamlit App (https://marketingstrategyabtesting-eu4hug4vbgnflcdfxxdcyh.streamlit.app/)

---

## 📬 Connect with Me:

Name: Sweety Seelam

Email: sweetyseelam2@gmail.com

LinkedIn: https://www.linkedin.com/in/sweetyrao670/

GitHub: https://github.com/SweetySeelam2/Marketing_Strategy_AB_Testing

My Portfolio: https://sweetyseelam2.github.io/SweetySeelam.github.io/

⭐ Star this repo if you found it useful!

---

## 🏆 My Contribution at Amazon

At Amazon, I led this conversion uplift analysis using A/B testing and machine learning. My analysis helped unlock a 43.09% conversion uplift, saving ~$2.1M/year in ad waste and improving campaign ROI across multiple business units. The success was featured in our Quarterly Business Review and adopted across Prime Video, Kindle, and Fresh.

---

## 📜 License & Usage:

MIT License

Copyright (c) 2025 Sweety Seelam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
