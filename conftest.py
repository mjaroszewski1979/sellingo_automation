import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from config.config import BASE_URL, REGISTRATION_URL

# ------------------------------------
# Ścieżki do lokalnych sterowników przeglądarek
# ------------------------------------
CHROME_DRIVER_PATH = r"C:\Users\mjaro\Desktop\selling_zadanie\chromedriver.exe"
EDGE_DRIVER_PATH = r"C:\WebDrivers\msedgedriver.exe"
FIREFOX_DRIVER_PATH = r"C:\WebDrivers\geckodriver.exe"



def _make_driver(browser: str, headed: bool):
    """
    Fabryka driverów Selenium obsługująca różne przeglądarki (Chrome, Edge, Firefox).
    Tworzy i konfiguruje instancję przeglądarki na podstawie przekazanych parametrów.

    Args:
        browser (str): Nazwa przeglądarki ('chrome', 'edge', 'firefox').
        headed (bool): 
            - True → tryb z UI (okno przeglądarki widoczne).
            - False → tryb headless (przeglądarka działa w tle).

    Returns:
        webdriver: Skonfigurowana instancja wybranej przeglądarki.
    """
    browser = browser.lower()
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        return webdriver.Chrome(service=ChromeService(CHROME_DRIVER_PATH), options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        return webdriver.Edge(service=EdgeService(EDGE_DRIVER_PATH), options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if not headed:
            options.add_argument("-headless")
        driver = webdriver.Firefox(service=FirefoxService(FIREFOX_DRIVER_PATH), options=options)
        driver.maximize_window()
        return driver

    else:
        raise ValueError(f"Nieznana przeglądarka: {browser}")


def pytest_addoption(parser):
    """
    Rejestruje dodatkowe opcje linii poleceń pytest:
    - --browser → wybór przeglądarki (chrome, edge, firefox).
    - --headed → uruchomienie w trybie z UI (bez headless).
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Wybierz przeglądarkę: chrome, edge, firefox",
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Uruchom testy z UI (bez headless)",
    )


@pytest.fixture
def driver(request):
    """
    Fixture tworząca i udostępniająca instancję Selenium WebDriver
    na podstawie opcji podanych w wierszu poleceń pytest.
    Po zakończeniu testów driver jest automatycznie zamykany.
    """
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    driver_instance = _make_driver(browser, headed)
    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def home_page(driver):
    """
    Fixture zwracająca instancję HomePage i otwierająca stronę główną.
    
    Returns:
        HomePage: Strona główna aplikacji.
    """
    home = HomePage(driver)
    home.open(BASE_URL)
    return home

@pytest.fixture
def registration_page(driver):
    """
    Fixture zwracająca instancję RegistrationPage i otwierająca stronę rejestracji.
    
    Returns:
        RegistrationPage: Strona formularza rejestracji użytkownika.
    """
    registration = RegistrationPage(driver)
    registration.open(REGISTRATION_URL)
    return registration


