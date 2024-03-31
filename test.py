import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):

    def test_website_loading(self):
        url = "https://atg.world"
        print("Connecting to", url)
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for non-200 status codes
            print("Status code:", response.status_code)
            self.assertEqual(response.status_code, 200, "Website did not load properly")
            print("Website loaded successfully!")
        except requests.RequestException as e:
            print("Error connecting to the website:", e)
            self.fail("Failed to load the website")

if __name__ == '__main__':
    unittest.main()
