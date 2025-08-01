import os
import streamlit as st
from agent.DrugAgentSystem import DrugAgentSystem
from agent.model import ModelName  # Import ModelName from agent.model
import time
# Thiết lập tiêu đề giao diện
st.set_page_config(page_title="Drug Chatbot", layout="centered")
st.title("Chatbot Tư Vấn Thuốc")
st.write("🤖 Hỏi đáp về thuốc và dược phẩm")

# Khởi tạo agent
with st.spinner("🚀 Initializing agent system..."):
    agent = DrugAgentSystem()
    time.sleep(1)
st.success("✅ Agent sẵn sàng!")
model_options_name = [getattr(ModelName, name) for name in dir(ModelName) if not name.startswith('__')]

# Hoặc
# model_options = list(ModelName.__dict__.values())

model_option = st.selectbox(
    'Chọn mô hình LLM:',
    model_options_name
)

# Thực hiện switch model khi người dùng chọn
if st.button("Chuyển mô hình") and model_option:
    with st.spinner(f"Đang chuyển mô hình LLM thành {model_option}..."):
        agent.switch_model(model_name_main=model_option)
        time.sleep(2) 
        st.success(f"✅ Mô hình LLM đã được chuyển thành: {model_option}")

question = st.text_input("💬 Hỏi câu hỏi về thuốc:", placeholder="e.g. Công dụng của Piratam Inj. 3g?")

if st.button("Gửi") and question.strip():
    with st.spinner("Đang suy nghĩ..."):
        start_time = time.time()
        try:
            answer = agent.question(question)
            end_time = time.time()
            response_time = end_time - start_time
            st.success(f"{model_option}")
            st.write(answer)
            st.info(f"Thời gian phản hồi: {response_time:.2f} giây")
        except Exception as e:
            end_time = time.time()
            response_time = end_time - start_time
            st.error("Có lỗi xảy ra trong quá trình xử lý câu hỏi. ")
            st.error(f"❌ Error: {str(e)}")
            st.info(f"Thời gian phản hồi: {response_time:.2f} giây")

# elif question.strip():
#     # Nếu nhập nhưng chưa bấm nút, vẫn xử lý luôn
#     with st.spinner("Thinking..."):
#         try:
#             answer = agent.question(question)
#             st.success("Here's the answer:")
#             st.write(answer)
#         except Exception as e:
#             st.success("Có lỗi xảy ra trong quá trình xử lý câu hỏi.")
#             st.write("Vui lòng thử lại.")
#             st.error(f"❌ Error: {str(e)}")
