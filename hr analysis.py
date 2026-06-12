import pandas as pd
import sqlite3

# Load and store in SQLite
df = pd.read_csv("HRDataset_v14.csv")
conn = sqlite3.connect("hr.db")
df.to_sql("employees", conn, if_exists="replace", index=False)
print("Database created!")
print("-" * 50)

# Q1 - Headcount and avg salary by department
q1 = """
SELECT Department,
       COUNT(*) as Headcount,
       ROUND(AVG(Salary), 2) as Avg_Salary,
       ROUND(MIN(Salary), 2) as Min_Salary,
       ROUND(MAX(Salary), 2) as Max_Salary
FROM employees
GROUP BY Department
ORDER BY Avg_Salary DESC
"""
print("Q1: Headcount & Salary by Department")
print(pd.read_sql(q1, conn))
print()

# Q2 - Attrition rate by department
q2 = """
SELECT Department,
       COUNT(*) as Total_Employees,
       SUM(Termd) as Terminated,
       ROUND(SUM(Termd) * 100.0 / COUNT(*), 1) as Attrition_Rate_Pct
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate_Pct DESC
"""
print("Q2: Attrition Rate by Department")
print(pd.read_sql(q2, conn))
print()

# Q3 - Performance score distribution
q3 = """
SELECT PerformanceScore,
       COUNT(*) as Employee_Count,
       ROUND(AVG(Salary), 2) as Avg_Salary,
       ROUND(AVG(EmpSatisfaction), 2) as Avg_Satisfaction
FROM employees
GROUP BY PerformanceScore
ORDER BY Employee_Count DESC
"""
print("Q3: Performance Score Distribution")
print(pd.read_sql(q3, conn))
print()

# Q4 - Top 5 termination reasons
q4 = """
SELECT TermReason,
       COUNT(*) as Count
FROM employees
WHERE Termd = 1
GROUP BY TermReason
ORDER BY Count DESC
LIMIT 5
"""
print("Q4: Top 5 Termination Reasons")
print(pd.read_sql(q4, conn))
print()

# Q5 - Salary gap between genders
q5 = """
SELECT Sex,
       COUNT(*) as Headcount,
       ROUND(AVG(Salary), 2) as Avg_Salary,
       ROUND(MIN(Salary), 2) as Min_Salary,
       ROUND(MAX(Salary), 2) as Max_Salary
FROM employees
GROUP BY Sex
"""
print("Q5: Salary Distribution by Gender")
print(pd.read_sql(q5, conn))
print()

# Q6 - Recruitment source effectiveness
q6 = """
SELECT RecruitmentSource,
       COUNT(*) as Total_Hired,
       SUM(Termd) as Terminated,
       ROUND(AVG(PerformanceScore = 'Exceeds'), 2) as Top_Performer_Rate,
       ROUND(SUM(Termd) * 100.0 / COUNT(*), 1) as Attrition_Pct
FROM employees
GROUP BY RecruitmentSource
ORDER BY Total_Hired DESC
"""
print("Q6: Recruitment Source Effectiveness")
print(pd.read_sql(q6, conn))
print()

# Q7 - Absenteeism by department
q7 = """
SELECT Department,
       ROUND(AVG(Absences), 2) as Avg_Absences,
       ROUND(AVG(DaysLateLast30), 2) as Avg_Days_Late,
       COUNT(*) as Headcount
FROM employees
GROUP BY Department
ORDER BY Avg_Absences DESC
"""
print("Q7: Absenteeism by Department")
print(pd.read_sql(q7, conn))
print()

# Q8 - High performers vs low performers salary comparison
q8 = """
SELECT 
    CASE 
        WHEN PerformanceScore = 'Exceeds' THEN 'High Performer'
        WHEN PerformanceScore = 'Fully Meets' THEN 'Meets Expectations'
        ELSE 'Needs Improvement'
    END as Performance_Band,
    COUNT(*) as Count,
    ROUND(AVG(Salary), 2) as Avg_Salary,
    ROUND(AVG(EmpSatisfaction), 2) as Avg_Satisfaction,
    ROUND(AVG(Absences), 2) as Avg_Absences
FROM employees
GROUP BY Performance_Band
ORDER BY Avg_Salary DESC
"""
print("Q8: Performance Band vs Salary & Satisfaction")
print(pd.read_sql(q8, conn))
print()

# Q9 - Engagement survey scores by manager (top 5 and bottom 5)
q9 = """
SELECT ManagerName,
       COUNT(*) as Team_Size,
       ROUND(AVG(EngagementSurvey), 2) as Avg_Engagement,
       ROUND(AVG(EmpSatisfaction), 2) as Avg_Satisfaction
FROM employees
GROUP BY ManagerName
HAVING Team_Size >= 5
ORDER BY Avg_Engagement DESC
LIMIT 5
"""
print("Q9: Top 5 Managers by Team Engagement")
print(pd.read_sql(q9, conn))
print()

# Q10 - Window function: salary rank within each department
q10 = """
SELECT Employee_Name, Department, Salary,
       RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) as Salary_Rank,
       ROUND(AVG(Salary) OVER (PARTITION BY Department), 2) as Dept_Avg_Salary,
       ROUND(Salary - AVG(Salary) OVER (PARTITION BY Department), 2) as Diff_From_Avg
FROM employees
ORDER BY Department, Salary_Rank
LIMIT 20
"""
print("Q10: Salary Ranking Within Each Department (Top 20)")
print(pd.read_sql(q10, conn))
print()

conn.close()
print("All done! hr.db saved.")