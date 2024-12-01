import pytest
from fast_api_handler import FastApiHandler

def test_model_loading():
    handler = FastApiHandler()
    assert handler.model is not None, "Model should be loaded successfully"

def test_predict_flat_price_valid():
    handler = FastApiHandler()
    valid_params = {
        'building_id': 12345,
        'floor': 3,
        'kitchen_area': 10,
        'living_area': 20,
        'rooms': 2,
        'is_apartment': 0,
        'studio': 0,
        'total_area': 50,
        'build_year': 2005,
        'building_type_int': 1,
        'latitude': 55.7558,
        'longitude': 37.6173,
        'ceiling_height': 2.7,
        'flats_count': 100,
        'floors_total': 15,
        'has_elevator': 1,
        'new_building': 0
    }
    result = handler.predict_flat_price(valid_params)
    print(result)
    assert isinstance(result, (float, int)), "Prediction should return a numerical value"


def test_validate_params_valid():
    handler = FastApiHandler()
    valid_request = {
        'flat_id': '12345',
        'model_params': {
            'building_id': 12345,
            'floor': 3,
            'kitchen_area': 10,
            'living_area': 20,
            'rooms': 2,
            'is_apartment': 0,
            'studio': 0,
            'total_area': 50,
            'build_year': 2005,
            'building_type_int': 1,
            'latitude': 55.7558,
            'longitude': 37.6173,
            'ceiling_height': 2.7,
            'flats_count': 100,
            'floors_total': 15,
            'has_elevator': 1,
            'new_building': 0
        }
    }
    assert handler.validate_params(valid_request), "Validation should pass for complete parameters"
