import streamlit as st
import json

# Load questions
with open("questions.json", "r") as file:
    questions = json.load(file)

# Initialize session state
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answers = []

st.set_page_config(page_title="Quiz Game", page_icon="🧠", layout="centered")

st.markdown(
    """
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧠 Interactive Quiz Game")

if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.subheader(f"Q{st.session_state.current_q + 1}: {q['question']}")

    selected = st.radio("Choose an answer:", q["options"], key=f"q{st.session_state.current_q}")

    if st.button("Next"):
        st.session_state.answers.append(selected)

        if selected == q["answer"]:
            st.session_state.score += 1

        st.session_state.current_q += 1
        st.experimental_rerun()
else:
    st.subheader("✅ Quiz Completed!")
    st.success(f"Your Score: {st.session_state.score} / {len(questions)}")

    # Review Answers
    with st.expander("Review your answers"):
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.markdown(f"Your answer: `{st.session_state.answers[i]}`")
            st.markdown(f"Correct answer: `{q['answer']}`")
            st.markdown("---")

    if st.button("Restart Quiz"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answers = []
        st.experimental_rerun()
