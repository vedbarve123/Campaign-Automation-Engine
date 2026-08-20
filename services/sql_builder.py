from config.campaign_config import Question

class SQLBuilder:
    def build(self,question:Question)->str:
        select_clause=self._build_select()
        from_clause=self._build_from()
        where_clause=self._build_where(question)
        query = f"""
        {select_clause}
        {from_clause}
        {where_clause}
    """
        return query.strip()
    
    def _build_select(self)->str:
        return """
        SELECT mobile
    """
    
    def _build_from(self)->str:
        return """
        FROM dbo.customer_single_view
    """
    
    def _build_where(self,question:Question)->str:
        conditions=[]
        
        if question.customer_types:
            customer_types = [
                f"'{customer_type}'"
                for customer_type in question.customer_types
                            ]
            sql_customer_types=",".join(customer_types)
            
            conditions.append(
                f"customer_type IN ({sql_customer_types})"
            )

        if question.recency:
            recency_value = [
                f"'{value}'"
                for value in question.recency
                            ]
            sql_recency=",".join(recency_value)
            
            conditions.append(
                f"recency_segment IN ({sql_recency})"
            )

        if question.fav_stores:
            fav_stores = [
                f"'{fav_store}'"
                for fav_store in question.fav_stores
                            ]
            sql_fav_stores=",".join(fav_stores)
            
            conditions.append(
                f"favorite_store IN ({sql_fav_stores})"
            )

        if question.min_frequency is not None:
            conditions.append(
                f"frequency >= {question.min_frequency}"
            )
        
        if question.min_quantity is not None:
            conditions.append(
                f"total_quantity >= {question.min_quantity}"
            )

        if question.min_revenue is not None:
            conditions.append(
                f"total_revenue >= {question.min_revenue}"
            )


        if  conditions:
            return "WHERE " + " AND ".join(conditions)
        else:
            return ""
