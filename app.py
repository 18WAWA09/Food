import streamlit as st
import pandas as pd
import random

# โหลดข้อมูล
file_path = "Lineman_Shops_Final_Clean.csv"
df = pd.read_csv(file_path)

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="แนะนำเมนูอาหารเย็น", page_icon="🍽️", layout="wide")

# Sidebar สำหรับตัวกรอง
st.sidebar.header("🎯 ตัวกรองเมนูอาหาร")
price_levels = df["price_level"].dropna().unique()
categories = df["category"].dropna().unique()

filter_type = st.sidebar.radio("เลือกประเภทการกรอง", ["ระดับราคา 💰", "หมวดหมู่อาหาร 🍽️"])

if filter_type == "ระดับราคา 💰":
    choice = st.sidebar.selectbox("เลือกระดับราคา", price_levels)
    filtered_df = df[df["price_level"] == choice]
else:
    choice = st.sidebar.selectbox("เลือกหมวดหมู่อาหาร", categories)
    filtered_df = df[df["category"] == choice]

# ส่วนหลักของหน้าเว็บ
st.title("🍽️ แนะนำเมนูอาหารเย็น")
st.markdown("เลือกตัวกรองจาก Sidebar ด้านซ้าย แล้วกดปุ่มเพื่อสุ่มเมนูที่เหมาะกับคุณ!")

# ปุ่มแสดงเมนู
if st.button("🔄 สุ่มเมนูแนะนำ", use_container_width=True):
    if not filtered_df.empty:
        sampled_df = filtered_df.sample(n=min(5, len(filtered_df)))
        
        col1, col2 = st.columns(2)
        for i, (index, row) in enumerate(sampled_df.iterrows()):
            with col1 if i % 2 == 0 else col2:
                st.markdown(
                    f"""
                    <div style='background-color:#f9f9f9; padding:15px; border-radius:10px; margin-bottom:10px;'>
                        <h3 style='color:#ff6347;'>🍜 {row['name']}</h3>
                        <p><strong>หมวดหมู่:</strong> {row['category']}</p>
                        <p><strong>ระดับราคา:</strong> {row['price_level']}</p>
                        <a href='{row['url']}' target='_blank'>🔗 ดูเพิ่มเติม</a>
                    </div>
                    """, unsafe_allow_html=True
                )
    else:
        st.warning("❌ ไม่พบเมนูที่ตรงกับเงื่อนไขของคุณ ลองเปลี่ยนตัวกรองดูนะ!")

# Footer
st.sidebar.markdown("""
---
📌 **วิธีใช้**
1. เลือกตัวกรองจาก Sidebar
2. กดปุ่ม "🔄 สุ่มเมนูแนะนำ"
3. คลิกที่ "ดูเพิ่มเติม" เพื่อดูข้อมูลร้าน
""")
