from dataclasses import dataclass,field
from datetime import date
from typing import List,Optional

@dataclass
class Question:
    segment_id: int
    segment_name: str
    customer_types:List[str]=field(default_factory=list)
    recency:List[str] = field(default_factory=list)
    min_total_orders:Optional[int]=None
    max_total_orders:Optional[int]=None
    min_frequency:Optional[int]=None
    max_frequency:Optional[int]=None
    min_orders_last_1yr:Optional[int]=None
    max_orders_last_1yr:Optional[int]=None
    min_quantity:Optional[int]=None
    max_quantity:Optional[int]=None
    min_revenue:Optional[float]=None
    max_revenue:Optional[float]=None
    min_avg_order_value:Optional[float]=None
    fav_stores:List[str] = field(default_factory=list)
    stores: List[str] = field(default_factory=list)
    products:List[str] = field(default_factory=list)
    enabled:bool=True

@dataclass
class Campaign:
    name:str
    campaign_id:int
    campaign_date:date
    questions:List[Question]=field(default_factory=list)
    
    






