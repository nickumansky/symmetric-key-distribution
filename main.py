from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Set, Dict
from key_distribution import assign_keys


app = FastAPI(
    title="Symmetric Key Distribution API",
    description="Assigns keys for provided networks."
)


class NetworkPlan(BaseModel):
    networks: List[Set[str]]


class Assignment(BaseModel):
    network: int
    key: int
    members: Dict[str, int]


class AssignmentResponse(BaseModel):
    assignments: List[Assignment]


@app.post("/assign_keys", response_model=AssignmentResponse)
def assign_keys_endpoint(plan: NetworkPlan):
    """
    API endpoint that takes a network plan (list of sets of names)
    and returns the key distribution assignments.
    """
    try:
        assignments = assign_keys(plan.networks)
        return {"assignments": assignments}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
