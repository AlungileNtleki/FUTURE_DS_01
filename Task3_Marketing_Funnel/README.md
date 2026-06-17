# Task 3 — Marketing Funnel & Conversion Performance Analysis

## What this project is about
I analyzed marketing and lead funnel data to see how users move through the journey from visiting a site, to engaging with it, to actually converting. The aim was to find where people drop off, compare how different channels perform, and come up with practical recommendations to improve conversion rates.

## Dataset
**Google Analytics Customer Revenue Prediction** (Kaggle)
https://www.kaggle.com/c/google-analytics-customer-revenue-prediction

I used a sample of 50,000 website sessions, which included data on traffic channel, device type, traffic source, and revenue.

## Tools Used
- **Python (VS Code)** — for cleaning the data, parsing nested JSON columns, calculating funnel metrics, and building charts (pandas, matplotlib, seaborn)
- **Tableau Public** — for building an interactive dashboard to present the findings

## What I found

| Metric | Value |
|--------|-------|
| Total Visits | 50,000 |
| Engaged Sessions | 25,360 (50.7%) |
| Bounce Rate | 49.3% |
| Conversions | 651 (1.30%) |

### Channel performance
- **Referral** converted the best by far, at around 5.5%, and brought in the most revenue
- **Organic Search** brought in the most traffic, but converted poorly at under 1%
- **Social** had a lot of visits but barely any conversions (0.06%)
- **Affiliates** didn't convert a single visitor

### Device insights
- Desktop made up 73.2% of all visits
- Mobile wasn't far behind at 23.5%, which is too big a chunk to ignore
- Tablet was minimal at 3.3%

## My recommendations
1. Put more budget into Referral marketing since it's clearly the strongest performer
2. Rethink the Social media strategy — lots of traffic isn't translating into sales
3. Reconsider the Affiliates program given it generated zero conversions
4. Pay more attention to the mobile experience since it makes up almost a quarter of traffic
5. Look into why almost half of visitors bounce immediately, possibly page speed or landing page design

## Dashboard
Here's the live interactive Tableau dashboard:
[Marketing Funnel & Conversion Performance Dashboard](https://public.tableau.com/app/profile/alungile.ntleki/viz/Marketing_Funnel_Analysis/Dashboard1?publish=yes)

## Files in this folder
## Files in this folder
- `funnel_analysis.py` — the Python script I used to clean and analyze the data
- `funnel_summary.csv` — the cleaned dataset that feeds into the Tableau dashboard
- `Chart1_Funnel.png` — funnel visualization
- `Chart2_Funnel.png` — conversion rate by channel
- `Chart3_Funnel.png` — visits by device type
- `Chart4_Funnel.png` — revenue by channel

## About
This was completed as part of the Future Interns Data Science & Analytics internship.
