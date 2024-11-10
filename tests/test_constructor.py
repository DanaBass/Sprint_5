import pytest
from locators import TestLocators


class TestConstructor:
    @pytest.mark.parametrize(
        'tab_locators',
        [
            [TestLocators.FILLING_LOCATOR, TestLocators.BUN_LOCATOR, TestLocators.SAUCE_LOCATOR],
            [TestLocators.SAUCE_LOCATOR, TestLocators.BUN_LOCATOR, TestLocators.FILLING_LOCATOR]
        ]
    )
    def test_transitions_constructor(self, driver, tab_locators):
        for locator in tab_locators:
            element = driver.find_element(*locator)

            class_name_before_clicked = element.get_attribute('class')
            element.click()
            class_name_after_clicked = element.get_attribute('class')

            assert class_name_before_clicked != class_name_after_clicked
