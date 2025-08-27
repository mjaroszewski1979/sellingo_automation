from selenium.webdriver.common.by import By

# ------------------------------------
# Locatory dla strony głównej (HomePage)
# Zawierają wszystkie elementy, z którymi interakcję wykonuje klasa HomePage.
# Każdy locator opisany jest w kontekście jego funkcjonalności.
# ------------------------------------
class HomePageLocators:
    # Komunikat o sukcesie wyświetlany po rejestracji
    SUCCESS_MESSAGE_DIV = (By.CLASS_NAME, "l-popup__message-content")

    # Przycisk zamknięcia popupu z komunikatem o sukcesie
    SUCCESS_MESSAGE_DIV_CLOSE = (By.CLASS_NAME, "l-popup__message-close")

    # Przycisk 'Konto' w nagłówku strony
    ACCOUNT_BUTTON = (By.ID, "header-account")

    # Link umożliwiający wylogowanie użytkownika
    LOGOUT_LINK = (By.LINK_TEXT, "Wyloguj się")
