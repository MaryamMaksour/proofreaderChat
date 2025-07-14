import streamlit as st
from openai import OpenAI
from arabic_support import support_arabic_text
from dotenv import load_dotenv

import os


support_arabic_text(all=True)

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=apiKey)

PROMPT_ID = "pmpt_68720deb98ac819598b1e84c9d098eff03cef1062df71381"
VERSION = "1"


c1, c2 = st.columns(2)
c2.markdown("**المدقق اللغوي الخاص بك**")
c1.image("Graident Ai Robot.jpg", width = 200)

c2.markdown("أدخل النص في الأسفل لتحصل على نتيجة بعد التدقيق اللغوي ",)


user_input = st.text_area(
    label=" أدخل نصك هنا", 
    height=150, 
    placeholder="اكتب النص هنا..."
)


if st.button(" إرسال"):
    if not user_input.strip():
        st.warning("يرجى إدخال نص قبل الإرسال.")
    else:
        try:
            with st.spinner("جارٍ جلب الاستجابة..."):
                response = client.responses.create(
                     prompt={
                        "id": PROMPT_ID,
                        "version": VERSION
                    },
                    input= user_input
                )


            generated_text = "".join(
                part.text for msg in response.output for part in msg.content if hasattr(part, "text")
            )

            st.success(" الاستجابة:")
            
            st.markdown(
                f"""
                <div dir="rtl" style="text-align: right; border: 3px solid #004030; padding: 25px;">
                {generated_text.strip()}
                </div>
                """, unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f" خطأ: {e}")
    



