import streamlit as st

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="YK Governance Engine",
    page_icon="⚖️",
    layout="centered"
)

# ── RETRO ZINE CSS ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Special+Elite&family=DM+Mono:ital,wght@0,400;0,500;1,400&display=swap');

/* BASE */
html, body, .stApp {
    background-color: #F4EFE0 !important;
    color: #1C1B18 !important;
    font-family: 'Special Elite', serif !important;
    background-image:
        repeating-linear-gradient(0deg, transparent, transparent 27px, rgba(0,0,0,0.04) 28px),
        repeating-linear-gradient(90deg, transparent, transparent 27px, rgba(0,0,0,0.02) 28px) !important;
    background-size: 28px 28px !important;
}

.block-container {
    max-width: 680px !important;
    padding-top: 3.5rem !important;
    padding-bottom: 5rem !important;
    margin: 0 auto !important;
}

/* MASTHEAD */
.retro-masthead {
    text-align: center;
    border-top: 5px solid #1C1B18;
    border-bottom: 3px double #1C1B18;
    padding: 28px 0 20px;
}

.retro-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #1C1B18;
    opacity: 0.45;
    margin-bottom: 10px;
}

.retro-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(60px, 11vw, 96px);
    line-height: 0.9;
    letter-spacing: 2px;
    color: #1C1B18;
    margin: 0;
}

.retro-title .outline {
    -webkit-text-stroke: 2.5px #1C1B18;
    color: transparent;
}

.retro-tagline {
    font-size: 14px;
    color: #1C1B18;
    opacity: 0.68;
    line-height: 1.65;
    margin: 20px auto 0;
    max-width: 460px;
    border-left: 4px solid #F2C229;
    padding-left: 14px;
    text-align: left;
    display: inline-block;
}

/* TICKER */
.retro-ticker-wrap {
    background: #1C1B18;
    overflow: hidden;
    padding: 9px 0;
    margin-top: 0;
}

.retro-ticker {
    display: inline-flex;
    white-space: nowrap;
    animation: rticker 24s linear infinite;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #F2C229;
}

.retro-ticker span { padding: 0 28px; }
.retro-ticker span::before { content: "✦  "; }

@keyframes rticker {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

/* FORM LABEL */
.retro-form-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #1C1B18;
    opacity: 0.45;
    text-align: center;
    margin-top: 36px;
    margin-bottom: 10px;
}

/* TEXTAREA */
div[data-baseweb="textarea"] {
    background-color: #FBF8F0 !important;
    border: 2.5px solid #1C1B18 !important;
    border-radius: 0 !important;
    box-shadow: 5px 5px 0 #1C1B18 !important;
    transition: box-shadow 0.15s ease, border-color 0.15s ease !important;
}

div[data-baseweb="textarea"]:focus-within {
    box-shadow: 6px 6px 0 #C8391B !important;
    border-color: #C8391B !important;
    background-color: #FFFFFF !important;
}

textarea {
    font-family: 'Special Elite', serif !important;
    color: #1C1B18 !important;
    font-size: 15px !important;
    padding: 1.1rem 1.3rem !important;
    line-height: 1.6 !important;
    background: transparent !important;
}

textarea::placeholder {
    color: #1C1B18 !important;
    opacity: 0.3 !important;
    font-style: italic !important;
}

/* BUTTON */
div.stButton {
    display: flex !important;
    justify-content: center !important;
    text-align: center !important;
    margin-top: 24px !important;
    margin-bottom: 20px !important;
}

div.stButton > button:first-child {
    background-color: #C8391B !important;
    color: #F4EFE0 !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 22px !important;
    letter-spacing: 3px !important;
    border-radius: 0 !important;
    border: 2.5px solid #1C1B18 !important;
    padding: 0.4rem 3rem !important;
    box-shadow: 5px 5px 0 #1C1B18 !important;
    transition: all 0.12s ease !important;
    cursor: pointer !important;
}

div.stButton > button:first-child:hover {
    background-color: #1C1B18 !important;
    color: #F2C229 !important;
    box-shadow: 7px 7px 0 #C8391B !important;
    transform: translate(-1px, -1px) !important;
}

div.stButton > button:first-child:active {
    box-shadow: 2px 2px 0 #1C1B18 !important;
    transform: translate(3px, 3px) !important;
}

/* DIVIDER */
hr {
    border: none !important;
    border-top: 3px double #1C1B18 !important;
    margin: 2rem 0 1.5rem !important;
}

/* RESULT CARD */
.retro-result {
    border: 2.5px solid #1C1B18;
    padding: 28px 32px 24px;
    position: relative;
    box-shadow: 5px 5px 0 #1C1B18;
    overflow: hidden;
}

.retro-result-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 100px;
    line-height: 1;
    opacity: 0.055;
    position: absolute;
    bottom: 4px;
    right: 12px;
    pointer-events: none;
    color: #1C1B18;
}

.retro-stamp {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 5px 12px;
    border: 2px solid currentColor;
    transform: rotate(-2.5deg);
    margin-bottom: 16px;
}

.retro-result-heading {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 40px;
    letter-spacing: 1px;
    line-height: 1.0;
    color: #1C1B18;
    margin-bottom: 12px;
}

.retro-result-desc {
    font-family: 'Special Elite', serif;
    font-size: 15px;
    color: #1C1B18;
    opacity: 0.82;
    line-height: 1.7;
}

.retro-ref {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0.4;
    margin-top: 18px;
}

/* STATUS COLORS */
.stamp-prohibited { color: #C8391B; }
.stamp-high       { color: #A85500; }
.stamp-limited    { color: #857000; }
.stamp-minimal    { color: #2A7F6F; }

.result-prohibited { border-left: 6px solid #C8391B !important; }
.result-high       { border-left: 6px solid #A85500 !important; }
.result-limited    { border-left: 6px solid #F2C229 !important; }
.result-minimal    { border-left: 6px solid #2A7F6F !important; }

/* WARNING BOX */
div[data-baseweb="notification"] {
    background: #FBF8F0 !important;
    border: 2px solid #1C1B18 !important;
    border-radius: 0 !important;
    font-family: 'Special Elite', serif !important;
    color: #1C1B18 !important;
}

/* FOOTER */
.retro-footer {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    color: #1C1B18;
    opacity: 0.3;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-align: center;
    margin-top: 5rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(28,27,24,0.18);
}
</style>
""", unsafe_allow_html=True)


# ── MASTHEAD ──────────────────────────────────────────────────
st.markdown("""
<div class="retro-masthead">
    <div class="retro-eyebrow">EU AI Act Compliance Engine — Vol. I, Issue 2025</div>
    <div class="retro-title">YK<br><span class="outline">GOVERNANCE</span></div>
    <div style="text-align:center">
        <p class="retro-tagline">
            Automating global regulatory compliance verification pipelines.
            We redefine corporate workflows where engineering accuracy meets risk minimization.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TICKER ────────────────────────────────────────────────────
st.markdown("""
<div class="retro-ticker-wrap">
    <div class="retro-ticker">
        <span>EU AI Act</span><span>Article 5</span><span>High Risk</span>
        <span>Compliance</span><span>Audit Trail</span><span>Governance</span>
        <span>Risk Matrix</span><span>Regulatory Checks</span><span>YK Legal</span>
        <span>EU AI Act</span><span>Article 5</span><span>High Risk</span>
        <span>Compliance</span><span>Audit Trail</span><span>Governance</span>
        <span>Risk Matrix</span><span>Regulatory Checks</span><span>YK Legal</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── INPUT ─────────────────────────────────────────────────────
st.markdown('<div class="retro-form-label">// Submit Operational Payload</div>', unsafe_allow_html=True)

user_input = st.text_area(
    label="Specifications Payload",
    label_visibility="collapsed",
    placeholder="Describe your system functionalities or dataset specifications...",
    height=140
)

# ── BUTTON + CLASSIFICATION LOGIC ────────────────────────────
if st.columns([1, 2, 1])[1].button("⚖  Run Audit Blueprint"):
    if user_input.strip() == "":
        st.warning("Please submit an operational payload structure.")
    else:
        text = user_input.lower()

        prohibited_keywords = [
            "social scoring", "biometric identification", "subliminal manipulation",
            "behavioral manipulation", "predictive policing"
        ]
        high_risk_keywords = [
            "credit scoring", "recruitment", "resume screening", "employment evaluation",
            "critical infrastructure", "judicial", "law enforcement", "border control",
            "medical device"
        ]
        limited_risk_keywords = [
            "chatbot", "deepfake", "generative text", "image generation",
            "ai writer", "customer support assistant"
        ]

        st.markdown("<hr>", unsafe_allow_html=True)

        if any(kw in text for kw in prohibited_keywords):
            st.markdown("""
            <div class="retro-result result-prohibited">
                <div class="retro-stamp stamp-prohibited">⬛ Unacceptable Risk</div>
                <div class="retro-result-num">01</div>
                <div class="retro-result-heading">Deployment Prohibited.</div>
                <div class="retro-result-desc">
                    Operational parameters conflict directly with statutory boundaries
                    outlined in Article 5 of the EU AI Act framework. Discontinue active
                    codebase iteration immediately and consult legal counsel before proceeding.
                </div>
                <div class="retro-ref">Ref: EU AI Act — Art. 5 // Prohibited AI Practices</div>
            </div>
            """, unsafe_allow_html=True)

        elif any(kw in text for kw in high_risk_keywords):
            st.markdown("""
            <div class="retro-result result-high">
                <div class="retro-stamp stamp-high">⬛ High Risk</div>
                <div class="retro-result-num">02</div>
                <div class="retro-result-heading">Mandatory Actions Flagged.</div>
                <div class="retro-result-desc">
                    System architectures operate within high-stakes human data fields.
                    Integration mandates continuous performance logs, human-override triggers,
                    conformity assessments, and official framework registration before deployment.
                </div>
                <div class="retro-ref">Ref: EU AI Act — Annex III // High-Risk AI Systems</div>
            </div>
            """, unsafe_allow_html=True)

        elif any(kw in text for kw in limited_risk_keywords):
            st.markdown("""
            <div class="retro-result result-limited">
                <div class="retro-stamp stamp-limited">⬛ Limited Risk</div>
                <div class="retro-result-num">03</div>
                <div class="retro-result-heading">Transparency Required.</div>
                <div class="retro-result-desc">
                    Generative or synthetic pipelines detected. Interfaces must explicitly
                    disclose AI-generated output to human consumers at all interaction steps.
                    Failure to disclose constitutes a direct regulatory breach.
                </div>
                <div class="retro-ref">Ref: EU AI Act — Art. 50 // Transparency Obligations</div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="retro-result result-minimal">
                <div class="retro-stamp stamp-minimal">⬛ Minimal Risk</div>
                <div class="retro-result-num">04</div>
                <div class="retro-result-heading">Exempt Baseline. Clear.</div>
                <div class="retro-result-desc">
                    System operations sit securely clear of all systemic risk markers.
                    No statutory mandates apply at this classification tier.
                    Align with standard internal scaling and optimization baselines.
                </div>
                <div class="retro-ref">Ref: EU AI Act — Recital 48 // Minimal Risk Category</div>
            </div>
            """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────
st.markdown('<div class="retro-footer">© YK Legal • Beyond Boundaries • Est. 2024</div>', unsafe_allow_html=True)
