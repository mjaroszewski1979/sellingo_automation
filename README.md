# sellingo_automation

## Wymagania

- Python 3.10+
- Przeglądarka: Chrome/Edge/Firefox
- Selenium 4.22+

## Instalacja

python -m venv .venv

# (aktywuj venv)

pip install -r requirements.txt

## Konfiguracja WebDriver

Aby uruchomić testy, należy pobrać odpowiedni WebDriver dla wybranej przeglądarki:

- ChromeDriver
- Edge WebDriver
- GeckoDriver (Firefox)

Po pobraniu ustaw ścieżki w pliku conftest.py zgodnie z lokalizacją na Twoim komputerze:

CHROME_DRIVER_PATH = r"C:\WebDrivers\chromedriver.exe"
EDGE_DRIVER_PATH = r"C:\WebDrivers\msedgedriver.exe"
FIREFOX_DRIVER_PATH = r"C:\WebDrivers\geckodriver.exe"

## Uruchomienie testów

pytest -v --browser=chrome # lub edge / firefox
pytest -v --browser=chrome --headed
