from config.campaign_config import Campaign
from config.campaign_config import Question
from services.sql_builder import SQLBuilder
from database.repository import Repository
import os
import pandas as pd

class PreviewEngine:
    def __init__(self, repository:Repository, sql_builder:SQLBuilder):
        self.repository = repository
        self.sql_builder = sql_builder

    def run(self, campaign):
        exclusion_sms = self.repository.get_exclusion_sms()
        exclusion_wa = self.repository.get_exclusion_wa()
        control_group = self.repository.get_control_group()
        assigned_mobiles = set()
        summary=[]
        for question_no,question in enumerate(campaign.questions,start=1):
            if not question.enabled:
                continue
            
            sql = self.sql_builder.build(question)            
            df = self.repository.fetch_dataframe(sql)
            df = self._deduplicate(df, assigned_mobiles)
            result=self._process_question(campaign,question_no,question,df,control_group,exclusion_wa,exclusion_sms)
            assigned_mobiles.update(df["mobile"])
            summary.append(result)
        self._save_campaign_summary(campaign, summary)
    
    
    def _deduplicate(self, df, assigned_mobiles):
        return df[~df["mobile"].isin(assigned_mobiles)]
    
    def _process_question(self, campaign,question_no,question,df,control_group,exclusion_wa,exclusion_sms):
        base_df = df[~df["mobile"].isin(control_group["mobile"])]
        delwa_df = base_df[~base_df["mobile"].isin(exclusion_wa["mobile"])]
        delsms_df = base_df[~base_df["mobile"].isin(exclusion_sms["mobile"])]
        
        variants = {"all": base_df,"delwa": delwa_df,"delsms": delsms_df}
        self._save_preview_files(campaign,question_no, variants)
        return {
            "Question No": question_no,
            "segment": question.segment_name,
            "all": len(base_df),
            "delwa": len(delwa_df),
            "delsms": len(delsms_df)
        }
                
    
    def _save_preview_files(self, campaign, question_no, variants):
        output_dir = f"output/{campaign.campaign_id}/Question_{question_no}"
        os.makedirs(output_dir, exist_ok=True)
        for variant_name, df in variants.items():
            filename = f"{output_dir}/preview_{variant_name}.csv"
            df.to_csv(filename, index=False)

    def _save_campaign_summary(self, campaign, summary):
        summary_df = pd.DataFrame(summary)
        output_dir = f"output/{campaign.campaign_id}"
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{output_dir}/campaign_summary.csv"
        summary_df.to_csv(filename, index=False)