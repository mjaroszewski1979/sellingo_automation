import pytest
from config.config import BASE_URL

# -------------------------------------------------------
# Test Suite: Home Page
# -------------------------------------------------------
# Zawiera testy weryfikujące kluczowe elementy i stabilność
# strony głównej aplikacji Sellingo (w wersji demo).
# Każdy test opiera się na wykorzystaniu obiektu Page Object
# `HomePage`, który reprezentuje stronę główną.
@pytest.mark.usefixtures("driver")
class TestHomePage:
    """
    Zestaw testów funkcjonalnych dla strony głównej aplikacji Sellingo.
    Testy obejmują poprawność adresu URL, tytułu strony oraz brak
    błędów krytycznych (500, 404).
    """

    def test_home_page_url(self, home_page, driver):
        """
        Test: Weryfikacja poprawności adresu URL strony głównej.
        Kroki:
            1. Otwórz stronę główną.
            2. Sprawdź, czy adres URL odpowiada wartości BASE_URL.
        Walidacja:
            - Aktualny adres URL == BASE_URL + "/".
        """
        assert driver.current_url == BASE_URL + "/", \
            f"Oczekiwany URL: {BASE_URL}/, ale był: {driver.current_url}"

    def test_home_page_title(self, home_page, driver):
        """
        Test: Weryfikacja poprawności tytułu strony głównej.
        Kroki:
            1. Otwórz stronę główną.
            2. Sprawdź, czy tytuł strony odpowiada oczekiwanemu.
        Walidacja:
            - Tytuł strony == "Demo.sellingo.pl".
        """
        assert driver.title == "Demo.sellingo.pl", \
            f"Oczekiwany tytuł: 'Demo.sellingo.pl', ale był: {driver.title}"

    def test_no_internal_server_error(self, home_page, driver):
        """
        Test: Weryfikacja, że strona główna nie zawiera błędu 500.
        Kroki:
            1. Otwórz stronę główną.
            2. Przeskanuj źródło strony pod kątem frazy "500 Internal Server Error".
        Walidacja:
            - Strona NIE zawiera komunikatu "500 Internal Server Error".
        """
        assert "500 Internal Server Error" not in driver.page_source, \
            "Na stronie wystąpił błąd 500!"

    def test_no_not_found_error(self, home_page, driver):
        """
        Test: Weryfikacja, że strona główna nie zawiera błędu 404.
        Kroki:
            1. Otwórz stronę główną.
            2. Przeskanuj źródło strony pod kątem frazy "Strona nie została znaleziona".
        Walidacja:
            - Strona NIE zawiera komunikatu 404.
        """
        assert "Strona nie została znaleziona" not in driver.page_source, \
            "Na stronie pojawił się komunikat 404!"

