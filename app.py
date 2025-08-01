import streamlit as st

st.title("🎧 EchoVerse - AI Audiobook Generator")

text_input = st.text_area("Enter your text or upload a .txt file")
tone = st.selectbox("Select Tone", ["Neutral", "Suspenseful", "Inspiring"])
voice = st.selectbox("Select Voice", ["Lisa", "Michael", "Allison"])

if st.button("Generate Audio"):
    st.success("✔️ Audio will be generated here!")  # Placeholder for actual logic
