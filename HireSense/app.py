import streamlit as st
import textwrap
import joblib

model = joblib.load("hiresense_combined_svm.pkl")
tfidf = joblib.load("hiresense_combined_tfidf.pkl")

st.set_page_config(
    page_title="HireSense",
    page_icon="💼",
    layout="centered"
)

def render_html(html):
    st.markdown(
        textwrap.dedent(html).strip(),
        unsafe_allow_html=True
    )

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top left,
            #e0e7ff 0%,
            transparent 35%
        ),
        radial-gradient(
            circle at top right,
            #fce7f3 0%,
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #f8faff 0%,
            #f5f3ff 50%,
            #fff7fb 100%
        );
}


.block-container {
    max-width: 900px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}


.hero {
    background:
        linear-gradient(
            135deg,
            #4338ca,
            #6366f1,
            #8b5cf6
        );

    padding: 34px 30px;
    border-radius: 24px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow:
        0 12px 35px
        rgba(79, 70, 229, 0.22);
}


.hero-title {
    color: white;
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -1px;
}


.hero-subtitle {
    color: #e0e7ff;
    font-size: 17px;
    margin-top: 8px;
}

.about-box {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #ddd6fe;
    border-radius: 18px;
    padding: 20px 22px;
    margin-bottom: 25px;
    box-shadow:
        0 6px 20px
        rgba(99, 102, 241, 0.08);
}

.about-title {
    color: #4338ca;
    font-size: 18px;
    font-weight: 700;
}

.section-title {
    color: #312e81;
    font-size: 21px;
    font-weight: 750;
    margin-top: 22px;
    margin-bottom: 10px;
}

div[data-testid="stTextInput"] input {
    border-radius: 13px !important;
    border: 1px solid #c7d2fe !important;
    background: white !important;
    min-height: 48px !important;
    padding-left: 15px !important;
}

div[data-testid="stTextArea"] textarea {
    border-radius: 13px !important;
    border: 1px solid #c7d2fe !important;
    background: white !important;
    padding: 14px !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow:
        0 0 0 2px
        rgba(99, 102, 241, 0.15) !important;
}


div[data-testid="stTextArea"] textarea:focus {
    border-color: #6366f1 !important;
    box-shadow:
        0 0 0 2px
        rgba(99, 102, 241, 0.15) !important;
}

.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 13px;
    font-size: 16px;
    font-weight: 700;
    border: 1px solid #c7d2fe;
    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #7c3aed
        );
    color: white;
    box-shadow:
        0 6px 15px
        rgba(79, 70, 229, 0.20);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 9px 20px
        rgba(79, 70, 229, 0.28);
    border-color: #6366f1;
}

.result-card {
    background:
        linear-gradient(
            135deg,
            #eef2ff,
            #f5f3ff,
            #faf5ff
        );
    border: 2px solid #a5b4fc;
    border-radius: 22px;
    padding: 28px;
    text-align: center;
    margin-top: 28px;
    margin-bottom: 25px;
    box-shadow:
        0 10px 30px
        rgba(99, 102, 241, 0.13);
}

.result-label {
    color: #6366f1;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1px;
}

.result-category {
    color: #312e81;
    font-size: 30px;
    font-weight: 850;
    margin-top: 8px;
}

.match-card {
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid #e2e8f0;
    border-left: 6px solid #6366f1;
    border-radius: 14px;
    padding: 16px 18px;
    margin: 10px 0;
    box-shadow:
        0 5px 15px
        rgba(15, 23, 42, 0.06);
}

.match-rank {
    color: #6366f1;
    font-weight: 800;
    font-size: 16px;
}

.match-name {
    color: #1e1b4b;
    font-size: 16px;
    font-weight: 700;
}

.match-score {
    color: #64748b;
    font-size: 13px;
    margin-top: 5px;
}

.stat-card {
    background:
        rgba(255, 255, 255, 0.94);
    border: 1px solid #ddd6fe;
    border-radius: 16px;
    padding: 18px 10px;
    text-align: center;
    min-height: 85px;
    box-shadow:
        0 5px 15px
        rgba(99, 102, 241, 0.06);
}

.stat-number {
    color: #4f46e5;
    font-size: 25px;
    font-weight: 800;
}

.stat-label {
    color: #64748b;
    font-size: 13px;
    margin-top: 4px;
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

hr {
    border-color: #e0e7ff !important;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    margin-top: 35px;
    line-height: 1.7;
}

@media (max-width: 600px) {
    .hero-title {
        font-size: 36px;
    }
    .hero-subtitle {
        font-size: 15px;
    }
    .section-title {
        font-size: 19px;
    }
    .result-category {
        font-size: 24px;
    }
}

</style>
""", unsafe_allow_html=True)

render_html("""
<div class="hero">
<div class="hero-title">💼 HireSense</div>
<div class="hero-subtitle">
AI-Powered Job Category Prediction System
</div>
</div>
""")

render_html("""
<div class="about-box">

<div class="about-title">
✨ Smart Job Classification
</div>

<div style="color:#64748b; margin-top:7px; line-height:1.6;">
Enter candidate skills and a job description to identify
the most relevant technology job category using Machine Learning.
</div>

</div>
""")


st.markdown(
    '<div class="section-title">🛠️ Candidate Skills</div>',
    unsafe_allow_html=True
)


skills_input = st.text_input(
    "Skills",
    placeholder="Python, Pandas, NumPy, SQL",
    label_visibility="collapsed",
    key="skills_input"
)

st.markdown(
    '<div class="section-title">📄 Job Description</div>',
    unsafe_allow_html=True
)

job_summary_input = st.text_area(
    "Job Description",
    placeholder=(
        "Paste the job description here...\n\n"
        "Example: Looking for a backend developer with "
        "Python, Django, REST API and PostgreSQL experience."
    ),
    height=190,
    label_visibility="collapsed",
    key="job_summary_input"
)

def clear_inputs():
    st.session_state.skills_input = ""
    st.session_state.job_summary_input = ""

col1, col2 = st.columns(2)

with col1:

    predict_button = st.button(
        "🚀 Predict Category",
        use_container_width=True
    )


with col2:

    clear_button = st.button(
        "↻ Clear Inputs",
        use_container_width=True,
        on_click=clear_inputs
    )


if predict_button:

    if not skills_input.strip():

        st.warning(
            "Please enter at least one skill."
        )

    elif not job_summary_input.strip():

        st.warning(
            "Please enter a job description."
        )

    else:
        skills = [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ]
        skills_text = " ".join(skills)

        combined_text = (
            skills_text
            + " "
            + job_summary_input
        )

        combined_vector = tfidf.transform(
            [combined_text]
        )

        prediction = model.predict(
            combined_vector
        )[0]

        scores = model.decision_function(
            combined_vector
        ).ravel()


        top_indices = scores.argsort()[::-1][:3]

        render_html(f"""
        <div class="result-card">

        <div class="result-label">
        PREDICTED JOB CATEGORY
        </div>

        <div class="result-category">
        {prediction}
        </div>

        </div>
        """)

        st.markdown(
            '<div class="section-title">📊 Top 3 Model Matches</div>',
            unsafe_allow_html=True
        )


        for rank, i in enumerate(
            top_indices,
            start=1
        ):

            category = model.classes_[i]

            score = scores[i]


            render_html(f"""
            <div class="match-card">

            <span class="match-rank">
            #{rank}
            </span>

            &nbsp;&nbsp;

            <span class="match-name">
            {category}
            </span>

            <div class="match-score">
            Model Score: {score:.3f}
            </div>

            </div>
            """)

        st.markdown(
            '<div class="section-title">📌 Analysis Summary</div>',
            unsafe_allow_html=True
        )


        stat1, stat2, stat3 = st.columns(3)

        with stat1:

            render_html(f"""
            <div class="stat-card">

            <div class="stat-number">
            {len(skills)}
            </div>

            <div class="stat-label">
            Skills Detected
            </div>

            </div>
            """)

        with stat2:

            word_count = len(
                job_summary_input.split()
            )


            render_html(f"""
            <div class="stat-card">

            <div class="stat-number">
            {word_count}
            </div>

            <div class="stat-label">
            Description Words
            </div>

            </div>
            """)

        with stat3:

            render_html(f"""
            <div class="stat-card">

            <div class="stat-number">
            {len(model.classes_)}
            </div>

            <div class="stat-label">
            Job Categories
            </div>

            </div>
            """)

render_html("""
<div class="footer">

HireSense • Machine Learning Job Classification System
<br>
TF-IDF + Linear SVM

</div>
""")