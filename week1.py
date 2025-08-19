import streamlit as st
import pandas as pd
import altair as alt

# عنوان التطبيق
st.title("👔 لوحة بيانات الموظفين")

# تحميل الملف المحلي
df = pd.read_csv("employees.csv")

# تنظيف أسماء الأعمدة من الفراغات
df.columns = df.columns.str.strip()

# عرض البيانات الخام (اختياري)
if st.checkbox("📄 عرض بيانات الموظفين"):
    st.dataframe(df)

# عناصر التحكم الجانبية
st.sidebar.header("🛠️ عناصر التحكم")

# فلترة حسب القسم
departments = sorted(df['DEPARTMENT_ID'].dropna().unique())
selected_departments = st.sidebar.multiselect("اختر الأقسام:", departments, default=departments)

# اختيار نوع الرسم البياني
chart_type = st.sidebar.selectbox("نوع الرسم:", ["مخطط أعمدة", "مخطط نقاط"])

# تصفية البيانات
filtered_df = df[df['DEPARTMENT_ID'].isin(selected_departments)]

# عنوان القسم الرئيسي
st.subheader("📊 تحليل الرواتب حسب الأقسام")

# إنشاء الرسم البياني
if chart_type == "مخطط أعمدة":
    chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X('DEPARTMENT_ID:O', title='رقم القسم'),
        y=alt.Y('SALARY:Q', title='الراتب'),
        tooltip=['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']
    ).properties(width=700, height=400)
else:
    chart = alt.Chart(filtered_df).mark_circle(size=100).encode(
        x=alt.X('DEPARTMENT_ID:O', title='رقم القسم'),
        y=alt.Y('SALARY:Q', title='الراتب'),
        color='JOB_ID:N',
        tooltip=['FIRST_NAME', 'LAST_NAME', 'JOB_ID', 'SALARY']
    ).properties(width=700, height=400)

# عرض الرسم البياني
st.altair_chart(chart, use_container_width=True)

# إحصائيات إضافية
st.markdown("### 🧮 إحصائيات إضافية:")
st.write("إجمالي الموظفين:", len(filtered_df))
st.write("متوسط الراتب:", round(filtered_df['SALARY'].mean(), 2))
st.write("أعلى راتب:", filtered_df['SALARY'].max())