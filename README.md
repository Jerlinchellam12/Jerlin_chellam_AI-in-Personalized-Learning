# 📘 AI Personalized Learning System

An AI-powered personalized learning prototype that adapts educational
recommendations based on learner behavior and provides analytics support
for teachers.

This project was developed as part of **Module E: AI Applications --
Individual Open Project**.

------------------------------------------------------------------------

## 🎯 Project Overview

Traditional education follows a one-size-fits-all approach.\
This project demonstrates how **Artificial Intelligence can be used to
personalize learning experiences** by:

-   Analyzing student learning behavior\
-   Classifying learner profiles using Machine Learning\
-   Providing personalized recommendations\
-   Supporting teachers with analytics dashboards

------------------------------------------------------------------------

## ✨ Key Features

### 👩‍🎓 Student View

-   Input learner behavior (accuracy, engagement, hint usage, etc.)\
-   Adaptive learner profiling\
-   Personalized learning recommendations\
-   AI-generated feedback\
-   PDF report generation

### 👨‍🏫 Teacher Dashboard

-   Class-level performance analytics\
-   Student comparison table\
-   Top performers & at-risk students\
-   Individual student progress charts

------------------------------------------------------------------------

## 🧠 AI Techniques Used

-   Supervised Machine Learning (Random Forest Classifier)\
-   Synthetic learner behavior dataset\
-   Rule-based recommendation system\
-   Streamlit for interactive UI

------------------------------------------------------------------------

## 📂 Project Structure

    ai_personalized_learning/
    │
    ├── AI_Personalized_Learning_Rubric_Format.ipynb   # Primary evaluation notebook
    ├── app/                                           # Application logic
    ├── utils/                                         # Logging, report generation
    ├── data/                                          # Logs (optional)
    ├── README.md                                      # Project documentation
    ├── .gitignore                                     # Environment protection

------------------------------------------------------------------------

## 🚀 How to Run the Project Locally

### 1. Clone the repository

    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name

### 2. Create virtual environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Run Streamlit app

    streamlit run app/ui_streamlit.py

------------------------------------------------------------------------

## 📊 Dataset

-   The project uses **synthetic student behavior data**
-   This avoids privacy issues and simulates realistic learner
    interactions
-   Features include:
    -   Accuracy\
    -   Response time\
    -   Engagement\
    -   Hesitation\
    -   Hint usage

------------------------------------------------------------------------

## ⚖️ Ethical Considerations

-   No real student data used (privacy-safe)\
-   AI supports teachers, does not replace them\
-   Predictions should not permanently label students\
-   Responsible AI principles considered (fairness, transparency)

------------------------------------------------------------------------

## 📈 Future Improvements

-   Use real-world datasets (EdNet, ASSISTments)\
-   Add emotion-aware learning features\
-   Long-term student tracking\
-   Improve adaptive recommendation logic\
-   Deploy as a real-world educational platform

------------------------------------------------------------------------

## 📌 Note for Evaluators

The primary evaluation artifact for this project is:

**AI_Personalized_Learning_Rubric_Format.ipynb**

It contains: - Full project explanation\
- Data preparation\
- Model training\
- Evaluation\
- Ethics\
- Conclusions

------------------------------------------------------------------------

## 👤 Author

Jerlin Chellam J

Module E 
