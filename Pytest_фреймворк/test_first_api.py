import requests

class TestFirstAPI:

    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Vitalii"
        data = {'name': name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong responce code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no 'answer' fueld in response"

        expectrd_response_text = f"Hello, {name}"
        acttual_response_text = response_dict['answer']
        assert expectrd_response_text == acttual_response_text, "Acttual response text is not correct"