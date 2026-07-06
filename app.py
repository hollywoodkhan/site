import streamlit as st

st.set_page_config(page_title="My First Streamlit App", page_icon="🌐", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #f0f2f5 0%, #dbeafe 100%);
        }
        .box {
            border: 2px solid #2563eb;
            border-radius: 12px;
            padding: 16px;
            text-align: center;
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Hello! My website is working!")
st.write("This is my first custom page, not WordPress.")

if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#f0f2f5"

if st.button("Change color"):
    st.session_state.bg_color = "#fef3c7" if st.session_state.bg_color == "#f0f2f5" else "#f0f2f5"

st.markdown(
    f"""
    <div style="background-color:{st.session_state.bg_color}; padding:20px; border-radius:12px;">
        <p style="margin:0;">The background color has been updated in this Streamlit app.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='box'><h3>Box 1</h3><p>Streamlit content</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='box'><h3>Box 2</h3><p>Ready to deploy</p></div>", unsafe_allow_html=True)
