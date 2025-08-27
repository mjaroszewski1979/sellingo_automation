from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.registration_page_locators import RegistrationLocators as RPL

class RegistrationPage(BasePage):
    """
    Page Object Model (POM) dla strony rejestracji.
    Dziedziczy po BasePage wszystkie metody interakcji z przeglądarką
    i inicjalizuje locatory specyficzne dla formularza rejestracji.
    """

    def __init__(self, driver, timeout=10):
        """
        Inicjalizacja strony rejestracji.
        Tworzy WebDriverWait dla elementów strony, aby zapewnić synchronizację.
        
        Args:
            driver (WebDriver): instancja przeglądarki.
            timeout (int): maksymalny czas oczekiwania na elementy.
        """
        wait = WebDriverWait(driver, timeout)
        super().__init__(driver, wait)

    # -------------------------------
    # Metody interakcji z elementami strony
    # -------------------------------

    def click_accept_cookies(self):
        """Kliknięcie przycisku akceptacji cookies"""
        self.click(RPL.ACCEPT_COOKIES_BUTTON)

    def fill_registration_form(self, user):
        """
        Wypełnienie formularza rejestracji danymi użytkownika.
        Wpisuje email, hasło, powtórzenie hasła oraz zaznacza checkbox regulaminu.

        Args:
            user (UserData): obiekt z danymi użytkownika (email, password).
        """
        self.type(RPL.EMAIL_INPUT, user.email)
        self.type(RPL.PASSWORD_INPUT, user.password)
        self.type(RPL.PASSWORD_REPEAT_INPUT, user.password)
        self.click(RPL.TERMS_CHECKBOX)

    def submit(self):
        """Kliknięcie przycisku 'Zarejestruj się', aby wysłać formularz"""
        self.click(RPL.REGISTER_BUTTON)
