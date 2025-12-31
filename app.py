import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from streamlit_drawable_canvas import st_canvas
import os, random, textwrap

# ================= CONFIG =================
LOVE_PASSWORD = "27-04-2025"
st.set_page_config(page_title="Only For Bujji ❤️", layout="centered")

# ================= SESSION STATES =================
for key in ["unlock", "show_memories", "said_yes", "love_message"]:
    if key not in st.session_state:
        st.session_state[key] = False if key != "love_message" else ""

# ================= PASSWORD =================
if not st.session_state.unlock:
    st.markdown("""
    <style>
    body {background: linear-gradient(135deg,#ff9a9e,#fad0c4);}
    .lock {background:rgba(255,255,255,0.6);padding:30px;border-radius:25px;text-align:center;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='lock'><h2>🔐 Private Love Space</h2><p>Only for Bujji ❤️</p></div>", unsafe_allow_html=True)
    pwd = st.text_input("Enter secret password 💕", type="password")

    if st.button("💗 Unlock My Heart"):
        if pwd == LOVE_PASSWORD:
            st.session_state.unlock = True
            st.rerun()
        else:
            st.error("Wrong password 🥹")
    st.stop()

# ================= CSS =================
st.markdown("""
<style>
body {background: linear-gradient(135deg,#ffecd2,#fcb69f);}

@keyframes fall {
  0% {top:-10%; opacity:1;}
  100% {top:110%; opacity:0;}
}

.love-fall {
  position:fixed;
  top:-10%;
  font-size:20px;
  color:#ff0844;
  font-weight:bold;
  animation:fall linear infinite;
}

.gallery {display:flex;overflow-x:auto;gap:25px;}
.card {
  min-width:260px;
  background:linear-gradient(135deg,#ff9a9e,#fad0c4);
  border-radius:25px;
  padding:12px;
  box-shadow:0 15px 30px rgba(0,0,0,0.3);
}
.quote {
  text-align:center;
  font-style:italic;
  color:#7a003c;
  font-weight:600;
}

.glass {
  background:rgba(255,255,255,0.6);
  backdrop-filter:blur(12px);
  border-radius:30px;
  padding:30px;
  box-shadow:0 20px 45px rgba(0,0,0,0.25);
}

.neon button {
  background:linear-gradient(135deg,#ff0844,#ffb199)!important;
  color:white!important;
  border-radius:30px!important;
  font-size:18px!important;
  padding:12px 30px!important;
  box-shadow:0 0 25px #ff4d6d;
}

.arrow {
  text-align:center;
  font-size:26px;
  animation:bounce 1.2s infinite;
  color:#ff0844;
}

@keyframes bounce {
  0%,100% {transform:translateY(0)}
  50% {transform:translateY(-10px)}
}

.heartbeat {
  font-size:90px;
  text-align:center;
  color:#ff0844;
  animation:beat 1s infinite;
}

@keyframes beat {
  0%{transform:scale(1)}
  25%{transform:scale(1.2)}
  40%{transform:scale(1)}
  60%{transform:scale(1.3)}
  100%{transform:scale(1)}
}

.yes-message {
  background:linear-gradient(135deg,#ffdde1,#ee9ca7);
  padding:30px;
  border-radius:30px;
  font-size:20px;
  font-weight:600;
  color:#7a003c;
  text-align:center;
  box-shadow:0 20px 40px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# ================= FALLING LOVE TEXT =================
for _ in range(18):
    st.markdown(
        f"<div class='love-fall' style='left:{random.randint(0,100)}%;"
        f"animation-duration:{random.randint(6,12)}s;'>I Love You ❤️</div>",
        unsafe_allow_html=True
    )

# ================= HEADER =================
st.title("🎉 Happy New Year Bujji ❤️")
st.markdown("""
<div class="glass">
This New Year isn’t about fireworks outside…<br>
It’s about the fire you lit inside my heart ❤️<br><br>
<b>I want a future with YOU.</b>
</div>
""", unsafe_allow_html=True)

# ================= MEMORIES =================
st.markdown('<div class="arrow">⬇️ Click here to see our memories ⬇️</div>', unsafe_allow_html=True)
st.markdown('<div class="neon">', unsafe_allow_html=True)
if st.button("📸 Our Memories"):
    st.session_state.show_memories = True
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.show_memories and os.path.exists("photos"):
    base_quotes = [
        "The day my heart found its home ❤️",
        "Your smile is my favorite place 💕",
        "This moment lives forever in my soul ✨",
        "Your presence make my day special 💖",
        "Every memory with you is precious 🥹",
        "Love looks beautiful when it’s you 🌸",
        "Be with me like this",
        "Forever starts with moments like this ❤️",
        "My heart chose you silently 💫",
        "Every picture holds a promise 💍"
    ]

    photos = [p for p in os.listdir("photos") if p.lower().endswith(("jpg","png","jpeg","webp"))]

    # generate extra unique quotes if photos > quotes
    while len(base_quotes) < len(photos):
        base_quotes.append(f"My heart beats for you more each day ❤️ {len(base_quotes)+1}")

    st.markdown('<div class="gallery">', unsafe_allow_html=True)
    for i, photo in enumerate(photos):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(Image.open(f"photos/{photo}"), use_container_width=True)
        st.markdown(f"<div class='quote'>{base_quotes[i]}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= PROPOSAL =================
st.markdown("## 💍 My Question")
st.markdown("""
<div class="glass">
I promise my love, loyalty, care, affection and support ❤️<br>
Not just today — but forever Bujjilu ❤️<br><br>
<b>Will you walk with me through this New Year and all the years ahead?</b>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="arrow">⬆️ Click YES from your heart ⬆️</div>', unsafe_allow_html=True)
st.markdown('<div class="neon">', unsafe_allow_html=True)
if st.button("💖 YES"):
    st.session_state.said_yes = True
st.markdown('</div>', unsafe_allow_html=True)

# ================= YES EFFECT =================
if st.session_state.said_yes:
    st.markdown("<div class='heartbeat'>❤️</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="yes-message">
    You didn’t just click YES…<br><br>
    You chose *us*, *love*, and *forever* 💍❤️<br><br>
    Thank you for trusting my heart with yours, Bujji.<br>
    <b>I promise to choose you every single day.</b>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💌 Message From Your Heart")
    st.session_state.love_message = st.text_area(
        "Write something for Karthik 💕",
        placeholder="Write your feelings here..."
    )

# ================= SIGNATURE =================
st.subheader("✍️ Your Signature")
name = st.text_input("Your Name 💕", "Bujji")

canvas_result = st_canvas(
    stroke_width=3,
    stroke_color="#ff0844",
    background_color="#fff0f5",
    height=200,
    drawing_mode="freedraw",
    key="canvas"
)

# ================= PDF =================
if st.button("💝 Download Our Forever Promise"):
    if canvas_result.image_data is not None:
        Image.fromarray(canvas_result.image_data.astype("uint8")).save("signature.png")
        pdf = canvas.Canvas("Forever_With_You.pdf", pagesize=A4)
        pdf.setFont("Helvetica-Bold", 26)
        pdf.drawCentredString(300, 800, "FOREVER WITH YOU 💍")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(50, 740, "Karthik ❤️ Bujji")
        y = 700
        for line in textwrap.wrap(st.session_state.love_message, 80):
            pdf.drawString(50, y, line)
            y -= 18
        pdf.drawImage("signature.png", 50, y-120, width=240, height=120)
        pdf.save()

        with open("Forever_With_You.pdf", "rb") as f:
            st.download_button("⬇️ Download Forever PDF", f)

# ================= FOOTER =================
st.markdown("---\n🌈 **Made with endless love — Karthik** 💍❤️")
