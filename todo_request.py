from pydantic import BaseModel , Field
from typing import Optional

class Todo_Request(BaseModel):
    id : Optional[int] = Field(ge=1 , description="During Todo creation ID is not required.." , default=None)
    title : str = Field(min_length=2 ,max_length=50)
    description : str = Field(min_length=2, max_length=50)
    is_completed : Optional[bool] =  Field(default=False)
    priority : int =Field(le=5 , ge=1)

    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title" : "Todo Title" , 
                "description" : "Todo description" ,
                "is_complete" : False,
                "priority" : "Todo priority..."
            }
            
        }
    }
