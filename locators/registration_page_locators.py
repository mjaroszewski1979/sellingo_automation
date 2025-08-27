from selenium.webdriver.common.by import By

class RegistrationLocators:
    """
    Lokatory elementów na stronie rejestracji.
    Definiują selektory używane przez Page Object `RegistrationPage`
    do interakcji z formularzem rejestracyjnym.
    """

    # Przycisk do akceptacji plików cookies (popup pojawiający się przed rejestracją)
    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[@data-role="all"]')

    # Pole input do wprowadzenia adresu e-mail
    EMAIL_INPUT = (By.NAME, "email")

    # Pole input do wprowadzenia hasła
    PASSWORD_INPUT = (By.NAME, "password")

    # Pole input do powtórzenia hasła
    PASSWORD_REPEAT_INPUT = (By.NAME, "password_confirm")

    # Checkbox do akceptacji regulaminu
    TERMS_CHECKBOX = (By.CLASS_NAME, "c-checkbox-field__checkmark")

    # Przycisk zatwierdzający formularz rejestracji ("Zarejestruj się")
    REGISTER_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Zarejestruj się']")

