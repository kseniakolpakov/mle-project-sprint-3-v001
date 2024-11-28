from fastapi import FastAPI, Body
from fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter
from prometheus_client import Histogram

app = FastAPI()

app.handler = FastApiHandler()

instrumentator = Instrumentator()
Instrumentator().instrument(app).expose(app) 

main_app_predictions = Histogram(

    "main_app_predictions",
    "Histogram of predictions",
    buckets=(1, 2, 4, 5, 10)
) 

c_1 = Counter('main_app_flats_less_20M_counter', 'Counts all flats that cost less than 20M')
c_2 = Counter('main_app_flats_more_50M_counter', 'Counts all flats that cost more than 50M')

@app.post("/api/flat/") 
def get_prediction_for_item(flat_id: str, model_params: dict):

    all_params = {
        'flat_id': flat_id,
        'model_params': model_params
    }
    response = app.handler.handle(all_params) 

    main_app_predictions.observe(response['price'])
    
    if response['price'] < 20_000_000:
        c_1.inc()
    
    if response['price'] > 50_000_000:
        c_2.inc()

    return response
