import streamlit as st
from textblob import TextBlob

st.title("Agency Trust & Transparency AI Agent")

st.write("Evaluate recruitment agencies based on user reviews.")

# User Inputs
agency_name = st.text_input("Enter Agency Name")
reviews = st.text_area("Enter User Reviews")

if st.button("Analyze Agency"):

    if reviews:

        # Sentiment Analysis
        analysis = TextBlob(reviews)
        sentiment = analysis.sentiment.polarity

        # Risk Keyword Detection
        risk_keywords = [
            "scam",
            "fraud",
            "fake",
            "unprofessional",
            "never",
            "unresponsive",
            "no response"
        ]

        risk_flag = False

        for word in risk_keywords:
            if word in reviews.lower():
                risk_flag = True

        # Decision Logic
        if risk_flag:
            sentiment_label = "High Risk"
            trust_score = 2.5
            message = "Risk indicators detected in user feedback."

        elif sentiment > 0.3:
            sentiment_label = "Positive"
            trust_score = 8.5
            message = "This agency appears reliable based on feedback."

        elif sentiment < -0.3:
            sentiment_label = "Negative"
            trust_score = 3.5
            message = "This agency may have reliability concerns."

        else:
            sentiment_label = "Neutral"
            trust_score = 6.5
            message = "Mixed reviews. Further verification recommended."

        # Display Results
        st.subheader("Analysis Result")

        st.write(f"Agency Name: {agency_name}")
        st.write(f"Sentiment: {sentiment_label}")
        st.write(f"Trust Score: {trust_score}/10")

        if sentiment_label == "Positive":
            st.success(message + " ✅")

        elif sentiment_label == "Neutral":
            st.warning(message + " ⚠️")

        else:
            st.error(message + " 🚨")

        # Agent Recommendation (Agentic AI decision step)
        st.subheader("Agent Recommendation")

        if trust_score >= 8:
            recommendation = "Recommended Agency"
            st.success(f"Decision: {recommendation}")

        elif trust_score >= 5:
            recommendation = "Verify Before Proceeding"
            st.warning(f"Decision: {recommendation}")

        else:
            recommendation = "Avoid This Agency"
            st.error(f"Decision: {recommendation}")

        # Explainable AI
        st.subheader("AI Explanation")

        if risk_flag:
            st.write("The system detected risk-related keywords in the review.")

        elif sentiment_label == "Positive":
            st.write("The review contains positive language indicating a good user experience.")

        elif sentiment_label == "Neutral":
            st.write("The review contains mixed feedback without strong positive or negative sentiment.")

        else:
            st.write("The review contains negative indicators suggesting potential reliability issues.")

    else:
        st.warning("Please enter a review to analyze.")
