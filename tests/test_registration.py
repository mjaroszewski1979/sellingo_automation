import pytest
from data.user_data import get_test_user



@pytest.mark.usefixtures("driver")
class TestRegistrationPage:
    """
    Testy strony rejestracji.
    Sprawdzają poprawność procesu rejestracji nowego użytkownika.
    """

    def test_successful_registration(self, home_page, registration_page):
        """
        Weryfikacja pomyślnej rejestracji nowego użytkownika.
        
        Kroki testowe:
        1. Pobranie danych testowego użytkownika.
        2. Wypełnienie formularza rejestracyjnego.
        3. Zatwierdzenie rejestracji.
        4. Sprawdzenie, czy komunikat o sukcesie jest widoczny na stronie głównej.

        Używa fixture 'registration_page' do interakcji z formularzem rejestracyjnym
        i fixture 'home_page' do weryfikacji komunikatu sukcesu.
        """
        user = get_test_user()

        # Wypełnienie formularza rejestracyjnego danymi testowego użytkownika
        registration_page.fill_registration_form(user)
        registration_page.submit()

        # Weryfikacja, że rejestracja zakończyła się sukcesem
        assert home_page.is_registration_successful(), "Rejestracja nie powiodła się"

        # Wylogowanie użytkownika
        home_page.logout_if_logged_in()




    

