import pytest
import requests

class TestFirstAPI:

    names = ["Vitalii", "Arseniy", ""]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong responce code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no 'answer' fueld in response"

        if name == "":
            expectrd_response_text = "Hello, someone"
        else:
            expectrd_response_text = f"Hello, {name}"
        acttual_response_text = response_dict['answer']
        assert expectrd_response_text == acttual_response_text, "Acttual response text is not correct"