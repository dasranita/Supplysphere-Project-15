from main import Material,mrp,Metrics,production_yield

def test_shortage():
    assert mrp(Material(demand=10,per_unit=3,available=20))['shortage']==10

def test_yield():
    assert production_yield(Metrics(produced=10,accepted=8))['yield_percent']==80
