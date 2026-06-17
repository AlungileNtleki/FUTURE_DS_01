# Customer Retention & Churn Analysis (Task 2)

## What this project is about
For my second task with Future Interns, I dug into a telecom company's customer data to figure out why people were cancelling their subscriptions and what could be done about it. I worked entirely in Excel, building PivotTables and a dashboard from scratch to turn raw customer records into insights a business could actually act on.

## What I was trying to answer
- How many customers are leaving, and how bad is the problem really?
- Which types of customers are most likely to churn?
- How long do people usually stay before they cancel?
- What could the business do differently to keep more customers around?

## Tools
Microsoft Excel — PivotTables, formulas, charts, and a one-page dashboard.

## The data
I used the Telco Customer Churn dataset from Kaggle (7,043 customers, 21 columns covering demographics, services, billing, and whether they churned).
Link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## What I found

| What I looked at | What the data showed |
|---|---|
| Overall churn rate | 26.54% of customers have left |
| Month-to-month contracts | 42.7% churn rate |
| One-year contracts | 11.3% churn rate |
| Two-year contracts | 2.8% churn rate |
| Senior citizens | 41.7% churn rate |
| Non-senior customers | 23.6% churn rate |
| Fiber optic internet users | 41.9% churn rate |
| DSL users | 19.0% churn rate |
| No internet service | 7.4% churn rate |
| Avg. monthly charge — churned customers | R76.28 |
| Avg. monthly charge — retained customers | R60.81 |
| Churned within first 12 months | 1,037 customers (55% of everyone who left) |

A few things stood out to me. Month-to-month customers churn at almost the same rate as fiber optic customers and senior citizens — three very different groups all landing around 42%, which made me think there might be overlapping reasons behind it (low commitment, high expectations, and possibly less support for older customers). The tenure numbers were the most striking part though — more than half of all churn happens in a customer's first year, which says a lot about onboarding and first impressions.

## What I would recommend to the business

1. **Get month-to-month customers onto longer contracts.** This group churns the most by far, so offering a discount or perk for switching to a 1-2 year plan could make a real dent in the numbers.
2. **Look into what's going wrong with fiber optic.** These customers pay the most and still leave at a high rate — that's usually a sign the service isn't matching the price.
3. **Build something specifically for senior customers.** Simpler plans, better support, maybe a dedicated help line — anything that reduces friction for this group.
4. **Focus harder on the first year.** Since most churn happens early, better onboarding and check-ins in the first few months could catch problems before customers give up.
5. **Don't lose sight of high-paying customers.** They're churning more than average, and they're the ones the business can least afford to lose.

## The dashboard
I built a one-page dashboard summarising everything visually:
- Overall churn rate (pie chart)
- Churn by contract type
- Churn by internet service type
- Churn by age group
- Churn by how long someone had been a customer

## Files in this folder
- `Telco_Churn_Analysis.xlsx` — the full workbook (raw data, PivotTables, dashboard)
- `Dashboard_Screenshot.png` — a quick preview image of the dashboard
