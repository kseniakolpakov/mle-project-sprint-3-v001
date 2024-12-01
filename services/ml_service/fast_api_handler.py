# coding: utf-8
"""Класс FastApiHandler, который обрабатывает запросы API."""

import joblib
import pandas as pd
import os

class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):

        self.param_types = {
            'flat_id': str,
            'model_params': dict
        }


        self.model_path = '/home/mle-user/mle-project-sprint-3-v001/services/models/final_pipeline.pkl'
        self.load_pipeline(model_path=self.model_path)
        
        self.required_model_params = ['building_id', 'floor', 'kitchen_area', 'living_area', 'rooms',
                                      'is_apartment', 'studio', 'total_area', 'build_year',
                                      'building_type_int', 'latitude', 'longitude', 'ceiling_height',
                                      'flats_count', 'floors_total', 'has_elevator', 'new_building']
        
        if self.model is None:  
            raise RuntimeError("Model could not be loaded. Application will not start.")



    def load_pipeline(self, model_path: str):

        try:
            self.model = joblib.load(model_path)
        
        except Exception as e:
            print(f"Failed to load model: {e}")
            self.model = None

    def predict_flat_price(self, model_params: dict) -> float:
        try:
            param_values_list = list(model_params.values())
            df = pd.DataFrame([param_values_list], columns=self.required_model_params)
            prediction = self.model.predict(df)[0]
            return prediction
    
        except KeyError as ke:
            print(f"Missing or incorrect model parameters: {ke}")
            raise ValueError("Invalid input data for prediction.") from ke
    
        except Exception as e:
            print(f"Error during prediction: {e}")
            raise RuntimeError("Prediction failed due to an internal error.") from e
       
        
    def check_required_query_params(self, query_params: dict) -> bool:
       
        if 'flat_id' not in query_params or 'model_params' not in query_params:
            return False
        
        elif not isinstance(query_params['flat_id'], self.param_types['flat_id']):
            return False
        
        elif not isinstance(query_params['model_params'], self.param_types['model_params']):
            return False
        
        else:
            return True
    
    def check_required_model_params(self, model_params: dict) -> bool:

        if set(model_params.keys()) == set(self.required_model_params):
            return True
        
        return False
    
    def validate_params(self, params: dict) -> bool:

        if self.check_required_query_params(params):
            print("All query params exist")
        
        else:
            print("Not all query params exist")
            return False
        
        if self.check_required_model_params(params["model_params"]):
            print("All model params exist")
        
        else:
            print("Not all model params exist")
            return False
        
        return True
		
    def handle(self, params):

        try:
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            
            else:
                model_params = params["model_params"]
                flat_id = params["flat_id"]
                print(f"Predicting for flat_id: {flat_id} and model_params:\n{model_params}")
                price = self.predict_flat_price(model_params)
                response = {
                    "flat_id": flat_id, 
                    "price": price, 
                }
       
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        
        else:
            return response

