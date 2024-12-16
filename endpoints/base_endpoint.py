from bs4 import BeautifulSoup


class BaseEndpoint:

    status_code = None
    response_json = None
    response = None
    response_data = None

    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.status_code}."

    def check_response_status_code_is_401(self):
        assert self.response.status_code == 401, f"Expected status code 401, but got {self.status_code}."

    def check_response_status_code_is_400(self):
        assert self.response.status_code == 400, f"Expected status code 400, but got {self.status_code}."

    def check_response_status_code_is_404(self):
        assert self.response.status_code == 404, f"Expected status code 404, but got {self.status_code}."
        soup = BeautifulSoup(self.response.text, 'html.parser')
        h1_tag = soup.find('h1')
        assert h1_tag.text == "Not Found", f"Expected <h1> text 'Not Found', but got '{h1_tag.text}'."

    def check_response_status_code_is_410(self):
        assert self.response.status_code == 410, f"Expected status code 410, but got {self.status_code}."
