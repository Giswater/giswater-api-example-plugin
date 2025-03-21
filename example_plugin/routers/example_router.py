from fastapi import APIRouter, Query
from ..models.example_model import ExampleModel

router = APIRouter(prefix="/exampleplugin", tags=["Example Plguin"])

@router.get("/custom")
def custom_endpoint():
    return {"message": "Custom endpoint from a plugin"}

@router.post("/data")
def receive_data(data: ExampleModel):
    return {"received": data.dict()}

@router.put("/data")
def modify_data(data: ExampleModel):
    return {"modified": data.dict()}

@router.delete("/data")
def delete_data(name: str = Query(..., title="Name", description="Name of the data to delete")):
    return {"deleted": name}
