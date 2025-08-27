from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class BasePage:
    """
    Bazowa klasa Page Object Model (POM) dla wszystkich stron.
    Zawiera metody wspólne do interakcji z elementami i oczekiwań.
    """
    def __init__(self, driver, wait):
        """
        Inicjalizacja BasePage.

        Args:
            driver (WebDriver): instancja przeglądarki.
            wait (WebDriverWait): obiekt do oczekiwania na elementy.
        """
        self.driver = driver
        self.wait = wait

    # -------------------------------
    # Nawigacja
    # -------------------------------
    def open(self, url: str):
        self.driver.get(url)


    # -------------------------------
    # Oczekiwania (waits)
    # -------------------------------
    def wait_for_visibility(self, locator):
        """Czeka aż element będzie widoczny"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickability(self, locator):
        """Czeka aż element będzie klikalny"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        """Czeka aż element pojawi się w DOM"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_present(self, locator):
        """Czeka aż wszystkie elementy pojawią się w DOM"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_invisibility(self, locator):
        """Czeka aż element zniknie"""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_text_in_element(self, locator, text):
        """Czeka aż w elemencie pojawi się tekst"""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_text_in_page_source(self, text):
        """Czeka aż tekst pojawi się w źródle strony"""
        return self.wait.until(lambda driver: text in driver.page_source)

    def wait_for_attribute_to_be(self, locator, attribute, value):
        """Czeka aż atrybut elementu przyjmie daną wartość"""
        return self.wait.until(EC.attribute_to_be(locator, attribute, value))

    # -------------------------------
    # Akcje na elementach
    # -------------------------------

    def click(self, locator):
        """Kliknięcie w element po wcześniejszym sprawdzeniu, że jest klikalny"""
        element = self.wait_for_clickability(locator)
        element.click()

    def type(self, locator, text: str, clear=True):
        """
        Wpisanie tekstu do pola input po wcześniejszym sprawdzeniu, że element jest widoczny.

        Args:
            locator: locator elementu input.
            text (str): tekst do wpisania.
            clear (bool): czy wyczyścić pole przed wpisaniem tekstu.
        """
        element = self.wait_for_visibility(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def is_visible(self, locator) -> bool:
        """
        Sprawdza, czy element jest widoczny.

        Returns:
            bool: True jeśli element jest widoczny, False jeśli TimeoutException.
        """
        try:
            self.wait_for_visibility(locator)
            return True
        except TimeoutException:
            return False
