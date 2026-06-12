# HR Workforce Analytics — SQL Case Study

**Tools:** Python · SQLite · Pandas  
**Dataset:** HR Dataset v14 — 311 employees, 36 columns  

---

## Project Overview

I analysed an HR dataset of 311 employees across 6 departments 
to answer real workforce business questions using SQL. Data was 
loaded into SQLite via Python and queried using advanced SQL 
including window functions, CASE statements, CTEs and aggregations.

---

## Business Questions Answered

| # | Question |
|---|---|
| Q1 | How are headcount and salaries distributed across departments? |
| Q2 | Which departments have the highest attrition rates? |
| Q3 | How does performance score relate to salary and satisfaction? |
| Q4 | Why are employees actually leaving? |
| Q5 | Is there a salary gap between male and female employees? |
| Q6 | Which recruitment sources bring the best quality hires? |
| Q7 | Which departments have the highest absenteeism? |
| Q8 | Do high performers earn more and feel better about their jobs? |
| Q9 | Which managers have the most engaged teams? |
| Q10 | How does each employee's salary rank within their department? |

---

## Key Findings

- Production has a **39.7% attrition rate** — nearly 4 in 10 employees have left
- **Employee Referrals** have the lowest attrition (16.1%) and highest top performer rate
- Discounts above 20% and unhappiness account for **25% of all terminations**
- A **4.2% gender salary gap** exists and warrants further investigation
- Top manager Kelley Spirea's team scores **4.48/5 on engagement**
- IT/IS salary range spans from $50K to $220K within the same department

---

## Files

| File | Description |
|---|---|
| `hr_analysis.py` | Python script — loads data into SQLite and runs all 10 queries |
| `HRDataset_v14.csv` | Raw dataset (311 employees, 36 columns) |
| `hr.db` | SQLite database file |

---

## SQL Concepts Used

- GROUP BY, ORDER BY, HAVING
- CASE WHEN statements
- Aggregate functions (AVG, COUNT, SUM, MIN, MAX)
- Window functions — RANK() OVER (PARTITION BY)
- Subqueries and filtering

---

## How to Run

```bash
pip install pandas
python hr_analysis.py
```
