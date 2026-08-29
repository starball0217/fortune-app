import os
from dotenv import load_dotenv
from anthropic import Anthropic
import streamlit as st
from datetime import datetime

load_dotenv()

client = Anthropic(
    base_url=os.getenv("ANTHRPIC_BASE_URL"),
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def ask_ai(prompt):
    res = client.messages.create(
        model="claude-haiku", max_tokens=1024,
        messages=[{"role": "user", "content" : prompt}]
    )
    return res.content[0].text

st.set_page_config(page_title="나의 운세 & 별자리 앱", layout="centered")

st.markdown("# 🌟 나의 운세 & 별자리 앱 🌙")

zodiac_signs = [
    "양자리 (3.21-4.19)",
    "황소자리 (4.20-5.20)",
    "쌍둥이자리 (5.21-6.20)",
    "게자리 (6.21-7.22)",
    "사자리 (7.23-8.22)",
    "처녀자리 (8.23-9.22)",
    "천칭자리 (9.23-10.22)",
    "전갈자리 (10.23-11.21)",
    "사수자리 (11.22-12.21)",
    "염소자리 (12.22-1.19)",
    "물병자리 (1.20-2.18)",
    "물고기자리 (2.19-3.20)",
]

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 이름", placeholder="이름을 입력해주세요")

with col2:
    birth_date = st.date_input(
        "📅 생년월일",
        value=datetime.now(),
        min_value=datetime(1800, 1, 1),
        max_value=datetime.now()
    )

zodiac = st.selectbox("♈ 별자리 선택", zodiac_signs)

st.markdown("---")

if st.button("🔮 운세 보기", use_container_width=True, type="primary"):
    if not name:
        st.error("이름을 입력해주세요! 😊")
    else:
        with st.spinner("✨ 오늘의 운세를 준비 중입니다..."):
            prompt = f"""
당신은 밝고 친근한 말투로 운세를 풀어주는 신비로운 점술사입니다.
다음 정보를 바탕으로 오늘의 운세를 재미있게 4~5줄로 작성해주세요.

이름: {name}
생년월일: {birth_date.strftime('%Y년 %m월 %d일')}
별자리: {zodiac}

운세는 다음 요소들을 포함해서 작성해주세요:
- 오늘의 운세 (긍정적이고 희망적인 내용)
- 운세 점수 (0~100점)
- 럭키 조언 (간단한 팁이나 격려)

따뜻하고 위로가 되는 느낌으로, 사용자가 즐겁게 읽을 수 있게 해주세요!
"""
            fortune = ask_ai(prompt)

            st.success("✨ 오늘의 운세입니다! ✨")
            st.markdown(f"""
### {name}님의 {zodiac} 운세

{fortune}
""")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
✨ 이 운세는 재미 목적입니다. 밝은 하루 되세요! ✨
</div>
""", unsafe_allow_html=True)
