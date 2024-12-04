from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element(locator='div.login_logo')
    assert swag_labs_page.exist_icon()
    swag_labs_page.find_element(locator="username")
    assert swag_labs_page.exist_icon()
    swag_labs_page.find_element(locator="password")
    assert swag_labs_page.exist_icon()

