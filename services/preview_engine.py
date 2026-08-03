from config.campaign_config import Campaign
from services.sql_builder import SQLBuilder
from database.repository import Repository

class PreviewEngine:
    def __init__(self, repository, sql_builder):
        self.repository = repository
        self.sql_builder = sql_builder

    def run(self, campaign):
        for question in campaign.questions:
            if not question.enabled:
                continue
            
            sql = self.sql_builder.build(question)
            df = self.repository.fetch_dataframe(sql)
        

    def _process_question(self, question):
        ...

    def _apply_exclusions(self, df):
        ...

    def _deduplicate(self, df):
        ...

    def _save_preview_files(self, question, variants):
        ...

    def _save_campaign_summary(self):
        ...