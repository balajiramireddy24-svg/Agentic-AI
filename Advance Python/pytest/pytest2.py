#fixtures : using common data for multiple test

import pytest
import pandas as pd

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'age': [20, 21, 22, 23, 24],
        'salary': [5,6,7,8,9],
        'Buy_insurance' : [0,0,1,1,1]
    })

#test 1
def test_data_shape(sample_data):
    assert sample_data.shape == (5,3)

def test_data_target_values(sample_data):
    target = [0,0,1,1,1]
    assert list(sample_data['Buy_insurance']) == target