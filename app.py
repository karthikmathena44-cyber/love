import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from streamlit_drawable_canvas import st_canvas
import os, random, textwrap

# ================= CONFIG =================
LOVE_PASSWORD = "27-04-2025"
WHATSAPP_NUMBER = "91" + "7780265835"

st.set_page_config(page_title="Only For Bujji ❤️", layout="centered")

# ================= SESSION STATES =================
if "unlock" not in st.session_state:
    st.session_state.unlock = False
if "show_memories" not in st.session_state:
    st.session_state.show_memories = False
if "said_yes" not in st.session_state:
    st.session_state.said_yes = False
if "love_message" not in st.session_state:
    st.session_state.love_message = ""

# ================= PASSWORD =================
if not st.session_state.unlock:
    st.markdown("""
    <style>
    body {background: linear-gradient(135deg,#ff9a9e,#fad0c4);}
    .lock {
        background: rgba(255,255,255,0.4);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="lock"><h2>🔐 Private Love Space</h2><p>Only for Bujji ❤️</p></div>', unsafe_allow_html=True)
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
@keyframes fall {0%{top:-10%}100%{top:110%}}
.rose {position:fixed; top:-10%; font-size:22px; animation:fall linear infinite;}
@keyframes explode {0%{transform:scale(0)}100%{transform:scale(4);opacity:0}}
.firework {position:fixed; font-size:28px; animation:explode 1.4s ease-out forwards;}
.glass {
  background: rgba(255,255,255,0.55);
  backdrop-filter: blur(12px);
  border-radius: 30px;
  padding: 30px;
  box-shadow: 0 20px 45px rgba(0,0,0,0.25);
}
.gallery {display:flex; overflow-x:auto; gap:25px;}
.card {
  min-width:260px;
  background: linear-gradient(135deg,#ff9a9e,#fad0c4);
  border-radius:25px; padding:12px;
  box-shadow:0 15px 30px rgba(0,0,0,0.3);
}
.quote {text-align:center; font-style:italic; color:#7a003c; font-weight:600;}
.neon button {
  background: linear-gradient(135deg,#ff0844,#ffb199)!important;
  color:white!important;
  border-radius:30px!important;
  font-size:18px!important;
  padding:12px 30px!important;
  box-shadow:0 0 25px #ff4d6d;
}
</style>
""", unsafe_allow_html=True)

# ================= ROSES =================
for _ in range(15):
    st.markdown(
        f'<div class="rose" style="left:{random.randint(0,100)}%;'
        f'animation-duration:{random.randint(6,12)}s;">🌹</div>',
        unsafe_allow_html=True
    )

# ================= HEADER =================
st.title("🎉 Happy New Year Bujji ❤️")

st.markdown("""
<div class="glass">
<h3>Bujji 💕</h3>
<p>
This New Year isn’t about fireworks outside…<br>
It’s about the fire you lit inside my heart ❤️<br><br>
<b>I want a future with YOU.</b>
</p>
</div>
""", unsafe_allow_html=True)

# ================= MEMORIES =================
st.markdown('<div class="neon">', unsafe_allow_html=True)
if st.button("📸 Our Memories"):
    st.session_state.show_memories = True
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.show_memories:
    st.subheader("💞 Our Love Moments")
    quotes = [
        "The moment my heart choose you ❤️",
        "My peace has your smile 💕",
        "You make life feel softer 💖",
        "Love looks like this 🌸",
        "Always you ❤️",
        "You are my everything 🥹",
        "Your presence make my day special",
        "Be with me like this"
        
    ]
        if not os.path.exists("photos"):
        st.warning("📂 Our memories folder is empty right now 💕")
    else:
        photos = sorted([
            p for p in os.listdir("photos")
            if p.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
        ])

        if len(photos) == 0:
            st.info("✨ Add our photos to the 'photos' folder to see magic ✨")
        else:
            st.markdown('<div class="gallery">', unsafe_allow_html=True)
            for i, photo in enumerate(photos):
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(Image.open(f"photos/{photo}"), use_container_width=True)
                st.markdown(
                    f'<div class="quote">{quotes[i % len(quotes)]}</div>',
                    unsafe_allow_html=True
                )
                st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# ================= PROPOSAL =================
st.markdown("## 💍 My Question")
st.markdown("""
<div class="glass">
<p>
I don’t promise a fairytale,<br>
I promise effort, loyalty, affection, care<br>
and forever support — only for you Bujji ❤️
</p>
<b>Will you walk with me through this New Year and all the years ahead?</b>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="neon">', unsafe_allow_html=True)
if st.button("💖 YES"):
    st.session_state.said_yes = True
st.markdown('</div>', unsafe_allow_html=True)

# ================= YES EFFECTS =================
if st.session_state.said_yes:
    for _ in range(25):
        st.markdown(
            f'<div class="firework" style="left:{random.randint(10,90)}%;top:{random.randint(10,80)}%;">🎆</div>',
            unsafe_allow_html=True
        )
    st.success("She said YES 💍❤️")

    # 💌 MESSAGE BOX
    st.subheader("💌 Message From Your Heart")
    st.session_state.love_message = st.text_area(
        "Write something for Me💕",
        placeholder="Write your feelings here...",
        height=150
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
    key="canvas",
)

# ================= PDF =================
if st.button("💝 Download Our Forever Promise"):
    if canvas_result.image_data is None:
        st.warning("Please sign first 🥹")
    else:
        Image.fromarray(canvas_result.image_data.astype("uint8")).save("signature.png")

        pdf = canvas.Canvas("Forever_With_You.pdf", pagesize=A4)
        pdf.setFont("Helvetica-Bold", 26)
        pdf.drawCentredString(300, 800, "FOREVER WITH YOU 💍")

        pdf.setFont("Helvetica", 15)
        pdf.drawString(50, 740, "Karthik ❤️ Bujji")
        pdf.drawString(50, 710, "Promise to love, respect and choose each other forever.")

        pdf.drawString(50, 660, "Message from Bujji:")
        y = 630
        for line in textwrap.wrap(st.session_state.love_message, 80):
            pdf.drawString(50, y, line)
            y -= 18

        pdf.drawString(50, y-20, "Signed by:")
        pdf.drawString(50, y-45, name)
        pdf.drawImage("signature.png", 50, y-140, width=240, height=120)

        pdf.save()

        with open("Forever_With_You.pdf", "rb") as f:
            st.download_button("⬇️ Download Forever PDF", f)

# ================= FOOTER =================
st.markdown("""
---
🌈 **Made with endless love — Karthik**  
💍 🌹 🎆
""")

