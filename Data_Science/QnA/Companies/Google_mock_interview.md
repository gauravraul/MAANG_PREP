# 🎤 Mock Interview Walkthroughs – Senior Data Scientist (Google Style)

Each walkthrough below is formatted with:
- 🔹 Question
- 🧠 Thought Process
- 🧩 Structured Answer (Framework)
- ✅ What the interviewer is looking for

---

## 1. 🎯 Product Case: YouTube Shorts – Drop in Engagement

### 🔹 Question:
> "YouTube Shorts team notices a sudden drop in engagement rate. How would you investigate?"

### 🧠 Thought Process:
- Metrics Deep-Dive → Funnel → Segment → Experiments → External Factors

### 🧩 Framework Answer:
1. **Clarify Metrics**: What defines “engagement”? (likes, comments, watch-through rate?)
2. **Time & Scope**: When did the drop start? Specific regions, devices, creators?
3. **Funnel Analysis**:
   - Is it fewer views? Lower watch time? Click-through drop?
   - Compare across cohorts (device, OS, geography).
4. **User Behavior Changes**: 
   - Drop in uploads? Shift in creator behavior?
5. **Experiment Rollouts**: 
   - Check recent A/B tests or code pushes.
6. **External Events**: 
   - Holidays, server outages, policy change?
7. **Next Steps**: 
   - Suggest logs, dashboards, correlation plots, rolling back feature flag if needed.

### ✅ Interviewer Wants:
- Structured thinking
- Ability to correlate metrics to user behavior
- Confidence with ambiguity

---

## 2. 🧪 Experimentation: Gmail Smart Compose A/B Test

### 🔹 Question:
> "You ran an A/B test on Gmail’s Smart Compose feature. Engagement improved, but revenue dipped. What do you do?"

### 🧠 Thought Process:
- Trade-off Analysis → Confounding Factors → Root Cause → Stakeholder Decision

### 🧩 Framework Answer:
1. **Validate Statistical Significance**:
   - Check if revenue dip is statistically significant or noise.
2. **Analyze Segment Impact**:
   - Revenue drop in which user groups? New users? Mobile users?
3. **Understand Mechanism**:
   - Are users replying faster but clicking fewer ads?
4. **Cross-Metric Tradeoff**:
   - Consider engagement lifetime value vs short-term ad revenue.
5. **Stakeholder Input**:
   - Product wants usage, Ads team wants revenue — align long-term impact.
6. **Action**:
   - Recommend refining Smart Compose targeting, run a follow-up experiment.

### ✅ Interviewer Wants:
- Business impact awareness
- Confidence in navigating conflict between metrics
- Cross-functional thinking

---

## 3. 📊 SQL + Metrics: Google Drive Retention Metric

### 🔹 Question:
> "Write a SQL query to find weekly retention of Google Drive users over the last 3 months."

### 🧠 Thought Process:
- Need to use cohorting logic and date_diff-style retention tracking

### 🧩 Skeleton SQL:
```sql
WITH user_cohorts AS (
  SELECT user_id, MIN(DATE_TRUNC('week', activity_date)) AS cohort_week
  FROM drive_activity
  WHERE activity_date >= CURRENT_DATE - INTERVAL '3 months'
  GROUP BY user_id
),
weekly_activity AS (
  SELECT user_id, DATE_TRUNC('week', activity_date) AS activity_week
  FROM drive_activity
  WHERE activity_date >= CURRENT_DATE - INTERVAL '3 months'
)
SELECT 
  c.cohort_week,
  w.activity_week,
  COUNT(DISTINCT w.user_id) AS retained_users
FROM user_cohorts c
JOIN weekly_activity w ON c.user_id = w.user_id
GROUP BY 1, 2
ORDER BY 1, 2;
