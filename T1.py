import streamlit as st
import pandas as pd
import altair as alt

# إعداد الصفحة
st.set_page_config(page_title="Employee Dashboard", layout="wide")

# العنوان
st.title("📊 HR Employee Dashboard")
st.markdown("This dashboard provides insights about employee distribution and salary data.")

# تحميل البيانات
df = pd.read_csv("employees.csv")
df.columns = df.columns.str.strip()

# تقسيم الصفحة إلى أعمدة لعرض الإحصائيات
col1, col2, col3 = st.columns(3)

with col1:
    total_employees = df['EMPLOYEE_ID'].nunique()
    st.metric("👥 Total Employees", total_employees)

with col2:
    avg_salary = df['SALARY'].mean()
    st.metric("💰 Average Salary", f"${round(avg_salary,2)}")

with col3:
    max_salary = df['SALARY'].max()
    min_salary = df['SALARY'].min()
    st.metric("📈 Highest Salary", f"${max_salary}")
    st.caption(f"Lowest Salary: ${min_salary}")

st.markdown("---")

# توزيع عدد الموظفين حسب الأقسام
st.subheader("Department Analysis")

dept_counts = df['DEPARTMENT_ID'].value_counts().reset_index()
dept_counts.columns = ['Department', 'Employees']

bar_chart = alt.Chart(dept_counts).mark_bar(color="#4e79a7").encode(
    x=alt.X('Department:O', title="Department ID"),
    y=alt.Y('Employees:Q', title="Number of Employees"),
    tooltip=['Department', 'Employees']
).properties(
    title="Number of Employees per Department",
    width=600
)

st.altair_chart(bar_chart, use_container_width=True)

st.markdown("---")

# توزيع الرواتب حسب القسم باستخدام boxplot
st.subheader("Salary Distribution per Department")

box_chart = alt.Chart(df).mark_boxplot(extent='min-max').encode(
    x=alt.X('DEPARTMENT_ID:O', title="Department ID"),
    y=alt.Y('SALARY:Q', title="Salary"),
    color=alt.Color('DEPARTMENT_ID:O', legend=None),
    tooltip=['DEPARTMENT_ID', 'SALARY']
).properties(
    width=600
)

st.altair_chart(box_chart, use_container_width=True)

st.markdown("---")

# توزيع الوظائف
st.subheader("Job Roles Distribution")

job_counts = df['JOB_ID'].value_counts().reset_index()
job_counts.columns = ['Job Role', 'Employees']

job_chart = alt.Chart(job_counts).mark_bar(color="#f28e2b").encode(
    x=alt.X('Job Role:O', sort='-y'),
    y=alt.Y('Employees:Q'),
    tooltip=['Job Role', 'Employees']
).properties(
    width=800,
    title="Number of Employees per Job Role"
)

st.altair_chart(job_chart, use_container_width=True)