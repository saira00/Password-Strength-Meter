import re
import streamlit as st

# Apply custom CSS for gradient background
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #ff7e5f, #feb47b, #86a8e7, #7f7fd5);
            background-size: cover;
            height: 100vh;
            padding: 20px;
        }
        .stTextInput input {
            background-color: white;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Password storage
saved_passwords = []

def check_password_strength(password):
    strength_score = 0
    feedback = []
    
    # Criteria checks
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("Include at least one number.")
    
    if re.search(r"[@$!%*?&]", password):
        strength_score += 1
    else:
        feedback.append("Include at least one special character (@$!%*?&).")
    
    # Strength Levels
    if strength_score == 5:
        strength = "Strong"
    elif strength_score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {"strength": strength, "score": strength_score, "feedback": feedback}

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        result = check_password_strength(password)
        st.write(f"### Strength: {result['strength']}")
        st.progress(result['score'] / 5)
        
        if result['feedback']:
            st.write("#123SairaKanwal456#@")
            for tip in result['feedback']:
                st.write(f"- {tip}")
    else:
        st.warning("Please enter a password to check.")

if st.button("Save Password"):
    if password:
        saved_passwords.append(password)
        st.success("Password saved successfully!")
    else:
        st.warning("Please enter a password before saving.")
