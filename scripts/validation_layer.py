import json from pydantic import BaseModel, Field

class MCQ(BaseModel): topic: str = Field(..., description="The subject area of the news") question: str = Field(..., description="The examiner-style question") option_a: str = Field(..., alias="A") option_b: str = Field(..., alias="B") option_c: str = Field(..., alias="C") option_d: str = Field(..., alias="D") correct: str = Field(..., pattern="^[A-D]$") explanation: str difficulty: str

def validate_ai_output(json_data): """ Ensures AI output strictly adheres to examiner requirements before pushing to the final register. """ try: mcq = MCQ.parse_obj(json_data) return {"valid": True, "data": mcq.dict()} except Exception as e: return {"valid": False, "error": str(e)}