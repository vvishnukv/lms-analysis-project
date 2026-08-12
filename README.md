# LMS Accessibility & Student Success Analysis

## 📊 Live Dashboard
**[Click Here to View the Interactive Tableau Dashboard](https://public.tableau.com/app/profile/vishnu.kaushik.varma.vuddaraju/viz/LMSAccessibilityStudentEngagementAnalysis/Dashboard1?publish=yes)**

## 🎯 Objective
As learning management systems (LMS) become the primary vehicle for education, ensuring WCAG 2.1 accessibility compliance is critical. This project analyzes a simulated dataset of 10,000 student records to determine if highly accessible courses correlate with better academic outcomes and higher student engagement.

## 🛠️ Tech Stack
* **Data Engineering:** Python (Pandas, NumPy, Faker)
* **Database:** PostgreSQL (Containerized via Docker)
* **Data Visualization:** Tableau Public

## 💡 Key Business Insights
1. **Academic Performance:** Courses in the "Fully Compliant" tier (>90 WCAG score) saw an average final grade increase of ~8.5% compared to "High Risk" courses.
2. **Student Engagement:** Forum engagement doubled in courses with highly accessible text and screen-reader-friendly layouts.
3. **Actionable Recommendation:** Mandate basic WCAG accessibility audits for all STEM courses, as this department showed the highest variance in accessibility scores and the sharpest drop-off in video watch time when captions were missing.