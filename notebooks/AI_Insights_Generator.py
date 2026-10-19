import pandas as pd

# Sample environmental data
data = {
    "Temperature_Change": 2.4,
    "NDVI_Change": -8,
    "Risk": "Moderate"
}

df = pd.DataFrame([data])

temperature = df.loc[0, "Temperature_Change"]
ndvi = df.loc[0, "NDVI_Change"]
risk = df.loc[0, "Risk"]

summary = f"""
EarthPulse AI Environmental Summary

Surface temperature increased by {temperature}°C compared to historical averages.

Vegetation levels decreased by {abs(ndvi)}%.

Current environmental risk level: {risk}.

These indicators may suggest increasing environmental stress and should be monitored over time.
"""

print(summary)

print("\n✅ AI Insight Generation Prototype Complete")
