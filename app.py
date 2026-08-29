import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Page settings
st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="✦",
    layout="wide"
)

# =========================
# CUSTOM AESTHETIC DESIGN
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background-color: #080a14;

    background-image:
        radial-gradient(
            circle at 15% 15%,
            rgba(125, 92, 255, 0.16),
            transparent 25%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(77, 166, 255, 0.12),
            transparent 25%
        ),
        radial-gradient(
            circle at 70% 85%,
            rgba(180, 90, 255, 0.10),
            transparent 25%
        ),
        linear-gradient(
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        );

    background-size:
        auto,
        auto,
        auto,
        35px 35px,
        35px 35px;

    background-attachment: fixed;
}

/* Main container */
.block-container {
    max-width: 1150px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Decorative top line */
.top-decoration {
    text-align: center;
    color: #8b7cff;
    font-size: 0.9rem;
    letter-spacing: 12px;
    margin-bottom: 0.8rem;
}

/* Main title */
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    text-align: center;
    font-size: 3.4rem;
    font-weight: 700;

    background: linear-gradient(
        90deg,
        #a78bfa,
        #60a5fa,
        #c084fc
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    letter-spacing: -1px;
}

/* Subtitle */
.hero-subtitle {
    text-align: center;
    color: #858ba3;
    font-size: 1rem;
    margin-top: 0.3rem;
    margin-bottom: 2.2rem;
}

/* Welcome glass card */
.welcome-card {
    background: linear-gradient(
        135deg,
        rgba(139, 92, 246, 0.10),
        rgba(59, 130, 246, 0.06)
    );

    border: 1px solid rgba(139, 92, 246, 0.20);

    border-radius: 22px;

    padding: 1.3rem 1.6rem;

    margin-bottom: 1.8rem;

    box-shadow:
        0 15px 45px rgba(0,0,0,0.20),
        inset 0 1px rgba(255,255,255,0.04);
}

.welcome-title {
    color: #ddd6fe;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.15rem;
    font-weight: 600;
}

.welcome-text {
    color: #8f95aa;
    margin-top: 0.3rem;
}

/* Section titles */
.section-title {
    color: #c4b5fd;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {

    background: rgba(8, 10, 20, 0.97);

    border-right:
        1px solid rgba(139, 92, 246, 0.18);
}

/* Sidebar title */
.sidebar-title {

    font-family: 'Space Grotesk', sans-serif;

    font-size: 1.35rem;

    font-weight: 700;

    color: #c4b5fd;
}

/* Sidebar headings */
section[data-testid="stSidebar"] h3 {

    color: #a78bfa !important;

}

/* Sidebar text */
section[data-testid="stSidebar"] p {

    color: #9298ad !important;

}

/* Select box */
div[data-baseweb="select"] > div {

    background:
        rgba(17, 20, 34, 0.9);

    border:
        1px solid rgba(139, 92, 246, 0.25);

    border-radius: 13px;

}

/* Text area */
textarea {

    background:
        rgba(10, 13, 24, 0.95) !important;

    border:
        1px solid rgba(139, 92, 246, 0.25) !important;

    border-radius:
        16px !important;

    color:
        #e5e7eb !important;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.18) !important;

}

/* Text area focus */
textarea:focus {

    border:
        1px solid #8b5cf6 !important;

    box-shadow:
        0 0 0 2px rgba(139,92,246,0.10),
        0 10px 35px rgba(0,0,0,0.25) !important;

}

/* Buttons */
.stButton > button {

    border-radius:
        14px;

    border:
        1px solid rgba(139,92,246,0.25);

    background:
        rgba(17,20,34,0.85);

    color:
        #c9cce0;

    font-family:
        'Space Grotesk', sans-serif;

    font-weight:
        600;

    padding:
        0.72rem 1rem;

    transition:
        all 0.25s ease;

    box-shadow:
        0 7px 25px rgba(0,0,0,0.18);

}

/* Button hover */
.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            rgba(139,92,246,0.20),
            rgba(59,130,246,0.12)
        );

    border-color:
        #8b5cf6;

    color:
        #ffffff;

    transform:
        translateY(-3px);

    box-shadow:
        0 12px 30px rgba(100,80,200,0.20);

}

/* Code output */
pre {

    background:
        rgba(10,13,24,0.95) !important;

    border:
        1px solid rgba(139,92,246,0.16) !important;

    border-radius:
        14px !important;

}

/* Markdown output */
.stMarkdown {

    color:
        #c9cce0;

}

/* Success messages */
div[data-testid="stAlert"] {

    border-radius:
        13px;

}

/* Dividers */
hr {

    border-color:
        rgba(139,92,246,0.15);

}

/* Footer */
.footer {

    text-align:
        center;

    color:
        #565c73;

    font-size:
        0.8rem;

    margin-top:
        2.5rem;

}

/* Decorative corner symbols */
.corner-decoration {

    text-align:
        center;

    color:
        #555b78;

    font-size:
        0.75rem;

    margin-top:
        0.8rem;

}

</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">✦ AI Code Explainer</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("### ✦ How it works")

    st.write("01  Select your language")
    st.write("02  Paste your code")
    st.write("03  Choose an action")
    st.write("04  Get your AI result")

    st.divider()

    st.markdown("### ✦ Supported Languages")

    st.write("🐍  Python")
    st.write("⚙️  C")
    st.write("⚡  C++")
    st.write("☕  Java")
    st.write("🌐  JavaScript")

    st.divider()

    st.markdown("### ✦ Features")

    st.write("⌁  Explain Code")
    st.write("✦  Improve Code")
    st.write("⚡  Optimize Code")

    st.divider()

    st.caption(
        "Built with Python • Streamlit • Gemini"
    )


# =========================
# MAIN PAGE
# =========================

st.markdown(
    '<div class="top-decoration">✦ · ˚ ✧ · ˚ ✦</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">AI Code Explainer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'understand your code • one explanation at a time'
    '</div>',
    unsafe_allow_html=True
)


# Welcome card

st.markdown("""
<div class="welcome-card">

<div class="welcome-title">
✦ Welcome, coder.
</div>

<div class="welcome-text">
Paste your code below and let your AI coding companion
explain, improve and optimize it.
</div>

</div>
""", unsafe_allow_html=True)


# Language

st.markdown(
    '<div class="section-title">⌘  Programming Language</div>',
    unsafe_allow_html=True
)

language = st.selectbox(
    "Language",
    ["Python", "C", "C++", "Java", "JavaScript"],
    label_visibility="collapsed"
)


# Code

st.markdown(
    '<div class="section-title">⌦  Your Code</div>',
    unsafe_allow_html=True
)

code = st.text_area(
    "Code",
    height=320,

    placeholder="""Paste your code here...

Example:

numbers = [1, 2, 3, 4, 5]

total = 0

for number in numbers:
    total += number

print(total)""",

    label_visibility="collapsed"
)

st.write("")


# =========================
# BUTTONS
# =========================

col1, col2, col3 = st.columns(3)


# EXPLAIN

with col1:

    if st.button(
        "⌁  Explain Code",
        use_container_width=True
    ):

        if code.strip() == "":
            st.warning("Please enter some code.")

        else:

            prompt = f"""
You are a programming teacher helping a beginner.

Explain this {language} code in simple language.

Code:

{code}

Give the explanation under these headings:

## What does this code do?

## How does it work?

Explain step by step.

## Time Complexity

## Space Complexity

## Important Functions and Variables

Explain the important functions and variables.
"""

            with st.spinner("✦ Understanding your code..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

            st.success(
                "Explanation generated ✦"
            )

            st.markdown(response.text)


# IMPROVE

with col2:

    if st.button(
        "✦  Improve Code",
        use_container_width=True
    ):

        if code.strip() == "":
            st.warning("Please enter some code.")

        else:

            prompt = f"""
You are a programming teacher.

Improve the following {language} code.

Code:

{code}

Make the code:

- Cleaner
- Easier to understand
- Properly formatted
- Beginner-friendly

Give the improved code first.

Then explain the changes you made.
"""

            with st.spinner("✦ Improving your code..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

            st.success(
                "Improved version generated ✦"
            )

            st.markdown(response.text)


# OPTIMIZE

with col3:

    if st.button(
        "⚡  Optimize Code",
        use_container_width=True
    ):

        if code.strip() == "":
            st.warning("Please enter some code.")

        else:

            prompt = f"""
You are an experienced programmer.

Optimize the following {language} code.

Code:

{code}

Try to improve its efficiency while keeping
the code understandable.

Give the answer under these headings:

## Optimized Code

## Improvements Made

## Time Complexity

## Space Complexity
"""

            with st.spinner("⚡ Optimizing your code..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

            st.success(
                "Optimized version generated ⚡"
            )

            st.markdown(response.text)


# Footer

st.markdown(
    '<div class="corner-decoration">'
    '· · ·  ✦  · · ·'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    'AI Code Explainer  ·  Python × Streamlit × Gemini'
    '</div>',
    unsafe_allow_html=True
)