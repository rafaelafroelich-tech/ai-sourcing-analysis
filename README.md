# AI-Powered Human-Centered Sourcing Analytics
This project analyzes recruiting funnel performance, sourcing effectiveness, and recruiter impact while leveraging AI to support recruiter decision-making.

The objective is not to automate hiring decisions, but to provide explainable insights that help recruiting teams prioritize outreach efforts and improve sourcing outcomes.

## Executive Summary
- Candidates: 601
- Hire Rate: 8.15%

## Business Questions
**1. Which sourcing strategies convert best?**
GitHub was the highest-performing sourcing channel with a hire rate of 10.96%, followed by
Inbound (10.14%) and Hunting (9.33%). Event-based sourcing and referrals produced the lowest
conversion rates in this dataset. Recommendation: Increase investment in GitHub sourcing,
inbound attraction, and targeted hunting strategies.
**2. What signals indicate a higher chance of advancing?**
Candidate engagement was the strongest predictor of success. Of the 49 hires, 48 responded to
recruiter outreach. Additional positive indicators included passing screening stages, completing
assessments, and maintaining communication.
**3. When is it worth persisting with a candidate?**
Candidates who responded within the first week demonstrated the highest conversion rates.
Recruiters should continue follow-up efforts for engaged candidates for up to 7–10 days before
deprioritizing.
**4. When is there a low probability of conversion?**
The largest cause of failure was lack of response. Among candidates who never replied, only one
was eventually hired. Other negative indicators included failed technical assessments, low
engagement, and timing mismatches.
**5. Are there relevant patterns among channels, recruiters, or
profiles?**
Significant differences were observed among recruiters and channels. Bruno achieved the highest
hire rate (15.3%), outperforming several peers. Candidate engagement remained the strongest
behavioral predictor of success. Recommendation: Study and replicate the practices of
top-performing recruiters.

## Responsible AI
Human-in-the-loop recommendations only. No automated hiring decisions.

## Run
pip install -r requirements.txt
streamlit run dashboard/app.py
