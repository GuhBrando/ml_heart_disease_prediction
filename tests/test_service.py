import pytest
from fastapi import HTTPException
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
from src.heart_prediction.service import ModelPrediction

@pytest.fixture
def mock_model(mocker):
    mock_rf_model = MagicMock()
    mock_rf_model.predict_proba.return_value = np.array([[0.2, 0.8]])  # Simula a previsão
    mock_scaler = MagicMock()
    mock_scaler.transform.return_value = np.ones((1, 23))  # Simula transformação de dados
    mocker.patch('joblib.load', side_effect=[mock_rf_model, mock_scaler])

@pytest.fixture
def payload():
    return {
        "name": "John",
        "surname": "Doe",
        "email": "john.doe@example.com",
        "health": "1",
        "have_private_doctor": "1",
        "last_checkup": "1",
        "last_exercise": "1",
        "high_blood_pressure": "0",
        "use_cholesterol_medicine": "0",
        "had_a_stroke": "0",
        "had_depression": "0",
        "kidney_disease": "0",
        "diabetes": "0",
        "urban_rural_status": "1",
        "mental_health": "1",
        "physical_activity": "1",
        "aerobic_recommendation": "1",
        "high_cholesterol": "1",
        "asthma": "0",
        "ethnicity": "1",
        "sex": "1",
        "age": "35",
        "height": "180",
        "weight": "75",
        "smoker_status": "0",
        "is_heavy_drinker": "0"
    }

def test_define_and_validate_payload_success(mock_model, payload):
    prediction = ModelPrediction()
    prediction._define_and_validate_payload(**payload)

    assert prediction.name == "John"
    assert prediction.surname == "Doe"
    assert prediction.age == 35
    assert prediction.health == 1

@patch('src.heart_prediction.service.insert_values_into_table')
def test_predict(mock_insert_values, mock_model, payload):
    prediction = ModelPrediction()

    result = prediction.predict(payload)
    assert "Você possui um risco significativo" in result

    mock_insert_values.assert_called_once()

    assert mock_insert_values.call_args[1]['model_prediction_result'] == 1  # classe prevista
    assert mock_insert_values.call_args[1]['model_confidence_result'] == 80.0  # confiança simulada

def test_predict_invalid_payload(mock_model, payload):
    prediction = ModelPrediction()

    invalid_payload = payload.copy()
    invalid_payload['health'] = "invalid"
    
    with pytest.raises(HTTPException):
        prediction.predict(invalid_payload)
