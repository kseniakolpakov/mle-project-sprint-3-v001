import joblib
from fast_api_handler import FastApiHandler

def load_pipeline(model_path: str):
    try:
        model = joblib.load(model_path)
        
    except Exception as e:
        print(f"Failed to load model: {e}")
        model = None
    return model 

if __name__ == "__main__":
    
    model = load_pipeline(model_path='/home/mle-user/mle-project-sprint-3-v001/services/models/final_pipeline.pkl')

    if model is None:  
        raise RuntimeError("Model could not be loaded. Application will not start.")
    
    
    print(f'Model parameter names: {model["model"].feature_names_}')
    test_params = {
        "flat_id": "123",
      "model_params": {
            "building_id": 12909,
            "floor": 25,
            "kitchen_area": 20,
            "living_area": 120,
            "rooms": 4,
            "is_apartment": False,
            "studio": False,
            "total_area": 140,
            "build_year": 2023,
            "building_type_int": 1,
            "latitude": 55.05,
            "longitude": 37.05,
            "ceiling_height": 3.5,
            "flats_count": 100,
            "floors_total": 25,
            "has_elevator": True,
            "new_building": True
    
      }
    }
    handler = FastApiHandler()
    response = handler.handle(test_params)
    print(f"Response: {response}") 