from datetime import date

from config.campaign_config import Campaign, Question


campaign = Campaign(
    name="Sample Campaign",
    campaign_id=1,
    campaign_date=date.today(),
    questions=[
        Question(
            segment_id=1,
            segment_name="Active Customers",
            customer_types=["Existing"],
            recency=["Active"],
            min_frequency=2,
            min_revenue=1000
        ),
        Question(
            segment_id=2,
            segment_name="Lapsed Customers",
            recency=["Lapsed"],
            min_frequency=1
        )
    ]
)