from fastapi import FastAPI
from pydantic import BaseModel, Field
app=FastAPI(title='SupplySphere planning')
class Material(BaseModel):
    demand:int=Field(ge=0)
    per_unit:int=Field(gt=0)
    available:int=Field(ge=0)
    daily_demand:float=Field(ge=0,default=0)
    lead_days:int=Field(ge=0,default=0)
    safety_stock:int=Field(ge=0,default=0)
@app.post('/mrp')
def mrp(m:Material):
    required=m.demand*m.per_unit
    return {'required':required,'shortage':max(0,required-m.available),'reorder_point':m.daily_demand*m.lead_days+m.safety_stock}
class Metrics(BaseModel):
    produced:int=Field(gt=0)
    accepted:int=Field(ge=0)
@app.post('/yield')
def production_yield(m:Metrics):
    from fastapi import HTTPException
    if m.accepted>m.produced: raise HTTPException(400,'Accepted exceeds produced')
    return {'yield_percent':100*m.accepted/m.produced}
