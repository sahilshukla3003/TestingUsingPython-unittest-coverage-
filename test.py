import unittest
from W import tell_weather

class TestWeatherApp(unittest.TestCase):

    def test_tell_weather(self):
        # Test with valid city name
        city_name = "Seattle"
        result = tell_weather(city_name)
        self.assertTrue(isinstance(result, dict))
        self.assertIn("temperature", result)
        self.assertIn("pressure", result)
        self.assertIn("humidity", result)
        self.assertIn("description", result)

        # Test with invalid city name
        city_name = "InvalidCityName"
        result = tell_weather(city_name)
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()