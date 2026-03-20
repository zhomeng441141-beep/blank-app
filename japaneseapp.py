import streamlit as st
import random
import datetime
import time

# ==============================
# 🎨 网页配置与样式
# ==============================
st.set_page_config(page_title="宅建士 & N3 学习助手", page_icon="🏠", layout="wide")

# ==============================
# 📚 数据仓库 (建议后期放入 GitHub 随时更新)
# ==============================
if 'vocab_list' not in st.session_state:
    st.session_state.vocab_list = [
        {"word": "重要事項説明", "reading": "じゅうようじこうせつめい", "meaning": "35条书面说明", "example": "契約の前に重要事項说明を行います。"},
        {"word": "増える", "reading": "ふえる", "meaning": "增加", "example": "人口が増えている。"},
        {"word": "瑕疵担保", "reading": "かしたんぽ", "meaning": "瑕疵担保（质量保证）", "example": "品確法による10年の義務です。"},
        {"word": "比べる", "reading": "くらべる", "meaning": "比较", "example": "二つの案を比べる。"},
    ]

# ==============================
# 🧠 逻辑函数
# ==============================
def get_daily_task():
    now = datetime.datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        return "🌅 早上好！现在的任务是：【N3 & 宅建词汇】"
    elif 12 <= hour < 18:
        return "📰 中午好！现在的任务是：【房产新闻阅读】"
    else:
        return "🌙 晚上好！现在的任务是：【会话实战练习】"

# ==============================
# 🖥️ 网页布局
# ==============================
st.title("🚀 宅建士 & 日语学习自动化助手")
st.write(f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# --- 顶部状态栏 ---
status_msg = get_daily_task()
st.info(status_msg)

# --- 核心功能区 ---
tab1, tab2, tab3 = st.tabs(["📚 词汇卡片", "📰 行业新闻", "💬 智能对话"])

with tab1:
    st.header("今日精选词汇")
    if st.button("换一批单词"):
        words = random.sample(st.session_state.vocab_list, 2)
        for w in words:
            with st.expander(f"📌 {w['word']} ({w['reading']})"):
                st.write(f"**意思：** {w['meaning']}")
                st.write(f"**例文：** {w['example']}")

with tab2:
    st.header("东京房产快讯")
    st.write("【2026/03/20】 东京核心区地价持续上涨，港区塔楼成交价突破 2 亿日元。")
    st.caption("关键词：上昇（じょうしょう）= 上涨 | 成約（せいやく）= 成交")

with tab3:
    st.header("会话模拟器")
    user_input = st.text_input("👉 尝试用『です/ます』回答：今天的心情如何？")
    if user_input:
        if "です" in user_input or "ます" in user_input:
            st.success("👍 非常专业的表现！")
        else:
            st.warning("👉 提示：作为宅建士，建议使用敬语哦。")

# --- 侧边栏：定时任务状态 ---
st.sidebar.header("⏰ 定时器状态")
st.sidebar.write("✅ 08:00 词汇推送：已就绪")
st.sidebar.write("✅ 14:00 新闻更新：进行中")
st.sidebar.write("⏳ 21:00 模拟面试：待触发")

if st.sidebar.button("立即手动触发所有任务"):
    st.sidebar.snow()
    st.toast("所有任务已重置并推送！")