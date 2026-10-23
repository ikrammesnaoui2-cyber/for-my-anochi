import streamlit as st

# 1. Aha saịtị na ngalaba nchọgharị (Tab)
st.set_page_config(
    page_title="For My Anochi ❤️", page_icon="💖", layout="centered"
)

# 🎵 Egwu azụ (ọ bụrụ na faịlụ ahụ dị)
try:
    with open("relaxing_music.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
except FileNotFoundError:
    pass

# 2. Isi okwu n'elu peeji ahụ
st.title("✨ For My Anochi")
st.write(
    "Take a deep breath and relax... This small space is made especially for you, Anass."
)
st.write("🌸 ✨ ☕")

# Mpaghara ozi
if "show_letter" not in st.session_state:
    st.session_state.show_letter = False

# Bọtịnụ mepe ozi
if not st.session_state.show_letter:
    if st.button("✉️ Open Your Letter", use_container_width=True):
        st.session_state.show_letter = True
        st.rerun()

# Ngosipụta ozi
if st.session_state.show_letter:
    st.markdown("---")
    st.subheader("✨ To My Dearest Anass,")

    st.write(
        """
        Words often fall short when I try to express how much you truly mean to me. 
        From the moment you entered my life, you brought a warmth, strength, and light that changed everything.

        **Anass**, you are not just my boyfriend—you are my safe haven, my quiet in the chaos, and my biggest source of joy. 
        The bravery and kindness you carry in your heart inspire me every single day. Even when distance or duty keeps us apart, 
        my thoughts are always with you, and my heart beats in rhythm with yours.

        Thank you for being my anchor, my support, and my home. No matter where life takes us, 
        I want you to know that I am forever proud of you and eternally grateful to walk this journey by your side.

        **Forever and always yours,**  
        *Lbgira dyalk* 🐮💖
        """
    )

    st.balloons()