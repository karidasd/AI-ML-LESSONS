import streamlit as st
from textblob import TextBlob

# Ρυθμίσεις σελίδας
st.set_page_config(page_title="Sentiment Tool", page_icon="🎭")

st.title("🎭 Sentiment Analysis Tool")
st.markdown("---")

# Είσοδος κειμένου
user_input = st.text_area("Εισάγετε το κείμενό σας στα Αγγλικά:", placeholder="π.χ. I am having a wonderful day!")

if st.button("Ανάλυση"):
    if user_input:
        analysis = TextBlob(user_input)
        score = analysis.sentiment.polarity
        
        if score > 0:
            st.success(f"Θετικό Συναίσθημα 😊 (Score: {score:.2f})")
        elif score < 0:
            st.error(f"Αρνητικό Συναίσθημα 😡 (Score: {score:.2f})")
        else:
            st.info(f"Ουδέτερο Συναίσθημα 😐 (Score: {score:.2f})")
    else:
        st.warning("Παρακαλώ γράψτε κάτι πρώτα!")
