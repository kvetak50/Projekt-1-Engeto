import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        yield page
        browser.close()

# Ověření cookie okna a jeho reakce po kliknutí na "Pouze nezbytné"
def test_cookie_consent(browser):
    browser.goto("https://www.lhkjestrabi.cz")
    print("Otevřena stránka lhkjestrabi.cz")

    consent_button = browser.locator("text=Pouze nezbytné")
    expect(consent_button).to_be_visible()
    print("Zobrazen banner s cookies")

    consent_button.click()
    print("Kliknuto na 'Pouze nezbytné'")

    expect(consent_button).not_to_be_visible()
    print("Banner zmizel")

# Test pro navštívení dalšího vebu na daných stránkách pomocí obrázku na horní liště
def test_hokejcz_link(browser):
    browser.goto("https://www.lhkjestrabi.cz")
    print("Otevřena stránka lhkjestrabi.cz")

# Přes třídu top_bar_icons_logo--no_grayscale

    link = browser.locator('a.top_bar_icons_logo--no_grayscale[href="http://www.hokej.cz/maxa-liga"]')
    expect(link).to_be_visible()
    print("Nalezen odkaz na hokej.cz")

    with browser.expect_popup() as popup_info:
        link.click()
    print("Kliknuto na odkaz")

    new_page = popup_info.value
    print(f"Přesměrováno na: {new_page.url}")

    assert "hokej.cz/maxa-liga" in new_page.url
    print("Ověřeno, že URL obsahuje hokej.cz/maxa-liga")

def test_historie_link(browser):
    browser.goto("https://www.lhkjestrabi.cz")
    print("Načtena hlavní stránka.")

#klub.hover, něco jako simulátor """najetí na dané tlačítko"""
    klub = browser.get_by_role("button", name="Klub")
    klub.hover()
    print("Najel jsem na Klub.")

    historie = browser.locator('a[href="/historie"]')
    assert historie.is_visible()
    print("Vidím Historii.")

    historie.click()
    print("Kliknul jsem na Historii.")

    assert "historie" in browser.url
    print("Jsme na stránce Historie.")