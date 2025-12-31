import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from streamlit_drawable_canvas import st_canvas
import os, random, textwrap, urllib.parse

# ================= CONFIG =================
LOVE_PASSWORD = "27-04-2025"
KARTHIK_WHATSAPP = "91XXXXXXXXXX"  # <-- PUT YOUR NUMBER (NO +)

st.set_page_config(page_title="Only For Bujji ❤️", layout="centered")

# ================= SESSION STATES =================
for key in ["unlock", "show_memories", "said_yes", "love_message", "pdf_ready"]:
    if key not in st.session_state:
        st.session_state[key] = False if key != "love_message" else ""

# ================= PASSWORD =================
if not st.session_state.unlock:
    st.markdown("""
    <style>
    body {background: linear-gradient(135deg,#ff9a9e,#fad0c4);}
    .lock {
        background:rgba(255,255,255,0.6);
        padding:30px;
        border-radius:25px;
        text-align:center;
        box-shadow:0 15px 40px rgba(0,0,0,0.3);
    }
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
  0% {top:-10%; opacity:0;}
  10% {opacity:1;}
  100% {top:110%; opacity:0;}
}

.love-fall {
  position:fixed;
  top:-10%;
  font-size:22px;
  color:#FFD700;
  font-weight:bold;
  text-shadow:0 0 10px rgba(255,215,0,0.9);
  animation:fall linear infinite;
}

.gallery {
  display:flex;
  overflow-x:auto;
  gap:25px;
  padding:15px;
}

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
  margin-top:8px;
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
  border:none!important;
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

# ================= FALLING LOVE =================
for _ in range(18):
    st.markdown(
        f"<div class='love-fall' style='left:{random.randint(0,100)}%;animation-duration:{random.randint(6,12)}s;'>I Love You ❤️</div>",
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
    photos = sorted([p for p in os.listdir("photos") if p.lower().endswith(("jpg","png","jpeg","webp"))])

    quotes = [
        "The moment my heart chose you ❤️",
        "Every smile of yours heals me 💕",
        "Be with me like this 🌸",
        "Love looks perfect when it’s you 💖",
        "My favorite place is beside you 🥹",
        "You make my world softer 💫",
        "Every memory with you is precious ✨",
        "I see forever in your eyes 💍",
        "You are my home ❤️",
        "With you, life feels complete 🌈"
    ]

    if len(quotes) < len(photos):
        quotes += [f"You are my forever memory ❤️ {i}" for i in range(len(photos) - len(quotes))]

    st.markdown('<div class="gallery">', unsafe_allow_html=True)
    for photo, quote in zip(photos, quotes):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(Image.open(f"photos/{photo}"), use_container_width=True)
        st.markdown(f"<div class='quote'>{quote}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= PROPOSAL =================
st.markdown("## 💍 My Question")
st.markdown("""
<div class="glass">
I promise my love, care, respect, loyalty and support.<br>
Not just today — but every day, Bujji ❤️<br><br>
<b>Will you walk with me through this New Year and all the years ahead?</b>
</div>
""", unsafe_allow_html=True)

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
    You choose *us*, *love*, and *forever* 💍❤️<br><br>
    I promise to choose you every single day Bujjilu.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.love_message = st.text_area(
        "💌 Write something for Karthik",
        placeholder="Your words will be saved in our forever agreement..."
    )

# ================= SIGNATURE =================
st.subheader("✍️ Sign Our Love Agreement")
name = st.text_input("Your Name", "Bujji")

canvas_result = st_canvas(
    stroke_width=3,
    stroke_color="#ff0844",
    background_color="#fff0f5",
    height=200,
    drawing_mode="freedraw",
    key="canvas"
)

# ================= PDF =================
if st.button("💝 Create & Download Agreement PDF"):
    if canvas_result.image_data is not None:
        Image.fromarray(canvas_result.image_data.astype("uint8")).save("signature.png")

        pdf = canvas.Canvas("Forever_With_You.pdf", pagesize=A4)
        pdf.setFont("Helvetica-Bold", 26)
        pdf.drawCentredString(300, 800, "FOREVER WITH YOU 💍")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(50, 760, "Karthik ❤️ Bujji")

        y = 720
        for line in textwrap.wrap(st.session_state.love_message, 80):
            pdf.drawString(50, y, line)
            y -= 18

        pdf.drawString(50, y-20, f"Signed by: {name}")
        pdf.drawImage("signature.png", 50, y-150, width=240, height=120)
        pdf.save()

        st.session_state.pdf_ready = True

# ================= DOWNLOAD & WHATSAPP =================
if st.session_state.pdf_ready:
    with open("Forever_With_You.pdf", "rb") as f:
        st.download_button("⬇️ Download Signed Agreement (PDF)", f)

    message = "I signed our love agreement ❤️\nThis New Year I choose YOU 💍\nForever yours,\nBujji 💕"
    encoded = urllib.parse.quote(message)
    whatsapp_link = f"https://wa.me/{KARTHIK_WHATSAPP}?text={encoded}"

    st.markdown(f"""
    <div class="neon" style="text-align:center;">
      <a href="{whatsapp_link}" target="_blank">
        <button>💚 Send Agreement Message to Karthik (WhatsApp)</button>
      </a>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("🌈 **Made with endless love — Karthik** 💍❤️")
