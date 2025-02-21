from altair import Column
import streamlit as st
import random
import time

# Motivational Quotes
quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your only limit is your mind.",
    "The expert in anything was once a beginner.",
    "Believe you can and you're halfway there.",
    "Difficulties strengthen the mind, as labor does the body."
]

# Set Page Configurations
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🚀", layout="centered")
# Theme Toggle in Navigation
theme = st.toggle("🌓 Dark Mode/Light Mood")

# Update CSS to include navbar theme support
st.markdown(
    f"""
    <style>
       
        .quote-box {{
            padding: 20px;
            color: {'white' if theme else 'black'};
            background-color: {'#2E2E2E' if theme else 'white'};
            border-left: 10px solid {'orange' if theme else 'orange'};
            border-right: 10px solid {'orange' if theme else 'orange'};
            font-size: 24px;
            font-weight: bold;
            border-radius: 15px;
            box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }}
        
        .stApp {{
            background-color: {'#1A1A1A' if theme else 'white'};
            color: {'white' if theme else 'black'};
        }}
        
        
        .stTextInput > div > div > input {{
            border: 2px solid {'orange' if theme else 'orange'};
            color: {'white' if theme else 'black'};
            background-color: {'#2E2E2E' if theme else 'white'};
          
           
        }}
        
        
        .stTextArea > div > div > textarea {{
            border: 2px solid {'orange' if theme else 'orange'};
            color: {'white' if theme else 'black'};
            background-color: {'#2E2E2E' if theme else 'white'};
            focus:none;
        }}
        .stButton > button {{
           border:2px solid orange;
           color:orange;

        }}
        .h1 {{
            color:orange;
            text-align:center;
            font-size:3rem;
            font-weight:bold;
        }}
         
    </style>
    """,
    unsafe_allow_html=True
)
h1 = "💫Growth Mindset Challenge";
st.markdown(f"<div class='h1'>{h1}</div>", unsafe_allow_html=True)
st.markdown("""
    <hr style="border: none; height: 5px; background-color:orange; margin-top:2px;">
""", unsafe_allow_html=True)
# App Title
st.title("🌱 Welcome to Your Growth Journey!")
with st.spinner('Loading motivation...'):
    time.sleep(1)

# Display Motivational Quote with Styled Box
st.subheader("✨Motivation Quotes✨")

quote = """Success is not final, failure is not fatal: It is the courage to continue that counts." Winston Churchill"."""
st.markdown(f"<div class='quote-box'>💡 {quote}</div>", unsafe_allow_html=True)


# User Input for Learning Goal
st.subheader("🎯 Set Your Learning Goal")
st.markdown(
    """
    <h2 style="color: orange; font-size: 18px;">
        🎯 Define your learning goal clearly—set a purpose, stay focused, and track progress to achieve success! 🚀
    </h2>
    """,
    unsafe_allow_html=True
)
goal = st.text_input("What new skill or concept do you want to learn this day?")
if goal:
    st.success(f"✅ Amazing! Stay focused on learning:**{goal}**")
    st.balloons()
else:
    st.warning("Please enter a learning goal.")  
# achievements your growth journey
st.header("🏆 Achievements your growth journey 🌟 ")
st.markdown(
    """
    <h2 style="color: orange; font-size: 18px;">
 "Celebrate your achievements—they are milestones in your growth journey, reminding you of how far you’ve come and inspiring you to go further! 🚀🌱"
     </h2>
    """,
    unsafe_allow_html=True
)
achievement = st.text_input("What are you proud of?")
if achievement:
    st.success(f"✅ Amazing! You've achieved: **{achievement}**")
    st.balloons()
else:
    st.info("✨Please enter your big and small achievements.😍")

# User Feedback Section
st.subheader("📝 Reflect on Your Progress")
st.markdown(
    """
    <h2 style="color: orange; font-size: 18px;">
    "Take a moment to reflect on your progress—celebrate small wins, learn from challenges, and keep moving forward! 🚀📈"
    </h2>
    """,
    unsafe_allow_html=True
)
feedback = st.text_area("Write about what you've learned or any challenges faced.", height=150)
if feedback:
    st.success("Your reflection has been recorded. Keep pushing forward!")
    st.balloons()
else:
    st.info("Please enter your feedback to help you grow.")
st.button("🚀 Submit Feedback")

# need more motivation
st.subheader("💫 Need More Motivation?🌠")
if st.button(" Click here for more motivation 💫"):

    new_quote = random.choice(quotes)
    st.markdown(f"<div class='quote-box'>💫 {new_quote}</div>", unsafe_allow_html=True)
    st.balloons()
else:
    st.info("Believe you can and you're halfway there.")
# Encouraging Footer
st.markdown("""
    <hr style="border: none; height:2px; background-color:orange; margin-top: 20px; margin-bottom: 20px;">
""", unsafe_allow_html=True)
st.markdown("### ✨Keep Growing, Keep Learning! 🚀")
# st.markdown("**©All righrs Reserve || Creat By Rimsha Sultan ||**")
st.markdown(
    """
    <style>
        .footer {
            color: orange;
            text-align: center;
            padding: 10px;
            font-size: 16px;
            coursor:pointer;
        }
        .footer a {
            color: #1DA1F2; /* Twitter Blue */
            margin: 0 10px;
            text-decoration: none;
        }
        .footer a:hover {
            color: #ffcc00;
        }
    </style>
    
    <div class="footer">
        <p><b> © All Rights Reserved || Created by Rimsha Sultan</b></p>
        <p>
            <a href="https://www.linkedin.com/in/rimsha-sultan-47215521a/" target="_blank">🔗 LinkedIn</a> |
            <a href="#" target="_blank">🐱 GitHub</a> |
            <a href="https://www.facebook.com/Rimshasultan22/" target="_blank">ⓕ FaceBook</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
