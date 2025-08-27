from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.home_page_locators import HomePageLocators as HPL

# ------------------------------------
# Page Object: HomePage
# Reprezentuje stronę główną aplikacji.
# Zawiera metody do interakcji z elementami UI takimi jak:
# - komunikaty o sukcesie
# - przycisk "Konto"
# - link "Wyloguj się"
# ------------------------------------
class HomePage(BasePage):

    def __init__(self, driver, timeout=10):
        """
        Inicjalizuje HomePage z obiektem WebDriver oraz WebDriverWait.

        Args:
            driver (WebDriver): Instancja Selenium WebDriver.
            timeout (int): Maksymalny czas oczekiwania (domyślnie 10 sekund).
        """
        wait = WebDriverWait(driver, timeout)
        super().__init__(driver, wait)

    def get_success_message_text(self):
        """
        Pobiera tekst komunikatu o sukcesie wyświetlanego po rejestracji.

        Returns:
            str: Treść komunikatu o sukcesie.
        """
        element = self.wait_for_visibility(HPL.SUCCESS_MESSAGE_DIV)
        return element.text

    def close_success_message(self):
        """
        Zamyka popup z komunikatem o sukcesie klikając w ikonę zamykania.
        """
        element = self.wait_for_clickability(HPL.SUCCESS_MESSAGE_DIV_CLOSE)
        element.click()

    def click_account_button(self):
        """
        Kliknięcie w przycisk 'Konto' znajdujący się w nagłówku strony.
        """
        element = self.wait_for_clickability(HPL.ACCOUNT_BUTTON)
        element.click()

    def click_logout_link(self):
        """
        Kliknięcie w link 'Wyloguj się' umożliwiający wylogowanie użytkownika.
        """
        element = self.wait_for_clickability(HPL.LOGOUT_LINK)
        element.click()

    def is_registration_successful(self) -> bool:
        """
        Sprawdza, czy komunikat o sukcesie rejestracji jest widoczny na stronie.

        Returns:
            bool: True jeśli komunikat jest widoczny, False w przeciwnym razie.
        """
        return self.is_visible(HPL.SUCCESS_MESSAGE_DIV)
    
    def logout_if_logged_in(self):
        """
        Wylogowuje użytkownika, jeśli jest zalogowany.
        """
        if self.is_visible(HPL.SUCCESS_MESSAGE_DIV):
            self.close_success_message()
            self.click_account_button()
            self.click_logout_link()