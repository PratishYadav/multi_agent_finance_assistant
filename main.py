from fastapi import FastAPI
from agents import api_agent, scraping_agent, analysis_agent, language_agent

app = FastAPI()

@app.get("/brief")
def get_market_brief():
    data = api_agent.get_asia_tech_allocation(["TSM", "SSNLF"])
    earnings = scraping_agent.get_earnings_news()
    risk = analysis_agent.analyze_risk(data)
    summary = language_agent.generate_summary(risk, earnings)
    return {"summary": summary}
