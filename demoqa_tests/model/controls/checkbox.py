from selene import have
from selene.support.shared import browser


def hobby(selector, value):
    browser.all(selector).element_by(have.text(value)).click()
