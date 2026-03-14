# Agency Trust & Transparency AI Agent

## Overview
This project demonstrates a prototype AI agent designed to evaluate recruitment agencies based on user reviews. The system performs sentiment analysis and risk keyword detection to generate a trust score that helps users identify reliable agencies.

The goal of this prototype is to showcase how AI agents can improve transparency and decision-making in recruitment platforms such as the Job Search Optimiser (JSO).

## Features
- Analyze recruitment agency reviews
- Perform sentiment analysis using NLP
- Detect risk-related keywords
- Generate a trust score for agencies
- Provide explainable AI output
- Interactive interface using Streamlit

## Technologies Used
- Python
- Streamlit
- TextBlob (NLP Sentiment Analysis)

## How It Works
1. User enters the agency name.
2. User submits a review about the agency.
3. The system performs sentiment analysis on the review.
4. Risk keywords such as fraud, scam, or unprofessional behavior are detected.
5. A trust score is generated based on sentiment and risk indicators.
6. The system displays the sentiment, trust score, and explanation.

## Example Use Cases
Positive Review:
"This agency helped me find a job quickly and the consultants were very supportive."

Neutral Review:
"The consultants were polite but the hiring process took longer than expected."

Negative Review:
"This agency promised job opportunities but never followed up and the consultants were unresponsive."

## How to Run the Project

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Run the Application
```
streamlit run agency_trust_agent.py
```

### 3. Open the App
Streamlit will automatically open the application in your browser.

## Project Structure
```
project-folder/
│

├── agency_trust_agent.py
├── requirements.txt
└── README.md
```

## Purpose
This prototype demonstrates the concept of an **Agency Trust & Transparency AI Agent**, which can be integrated into recruitment platforms to improve trust and transparency for job seekers.

## Future Improvements
- Analyze multiple reviews per agency
- Use advanced NLP models for sentiment analysis
- Integrate with recruitment platform databases
- Deploy the system as a scalable AI service
