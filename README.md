# Marketing_Strategy_AB_Testing

## Project Overview
This project evaluates the effectiveness of a new marketing strategy using A/B testing.

## Dataset
- Source: Marketing A/B Testing dataset
- Columns:
  - `user id`: Unique user identifier
  - `test group`: psa or ad group
  - `converted`: Whether the user converted (1 = Yes, 0 = No)

## Steps
1. Data Loading & Cleaning
2. Exploratory Data Analysis (EDA)
3. Statistical Hypothesis Testing
4. Interpretation and Conclusion

## Results
- The p-value obtained through running the two-sample t-test is 0.00 which is lower than the significance level p_value of 0.05, determining that the new strategy - psa (Public Service Announcement) is statistically significant. Thus, we conclude that the new marketing strategy significantly impacts the conversion rates.

## Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- SciPy (Two-sample t-test)
