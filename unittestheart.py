import unittest
from Heart_Disease_Prediction_WebApp import heartdisease_prediction

class TestDiseasePredictionSystem(unittest.TestCase):

    def test_heart_disease_prediction(self):
        # Test case for Heart Disease Prediction
        # You need to update the input values based on your model's requirements
        input_data = {
            'age': 63,
            'sex': 1,
            'cp': 3,
            'trestbps': 145,
            'chol': 233,
            'fbs': 1,
            'restecg': 0,
            'thalach': 150,
            'exang': 0,
            'oldpeak': 2.3,
            'slope': 0,
            'ca': 0,
            'thal': 1
        }

        # Assuming that your model predicts 1 for heart disease and 0 for no heart disease
        expected_target = 'The person is having heart disease'

        # Now, simulate the Streamlit app interaction
        with self.subTest(msg="Heart Disease Prediction Test"):
            target = heartdisease_prediction(input_data)
            print("Actual Target:", target)
            print("Expected Target:", expected_target)
            self.assertEqual(target, expected_target)

if __name__ == '__main__':
    unittest.main()