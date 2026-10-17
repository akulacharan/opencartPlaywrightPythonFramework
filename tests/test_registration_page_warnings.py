import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RandomDataUtil
from pages.registration_page_with_empty_fields import RegistrationPageWarnings


@pytest.mark.sanity
@pytest.mark.regression
def test_warning_messages_for_empty_registration_fields(page):
    """
    Verify that appropriate warning messages are displayed when
    mandatory registration fields are left empty.
    Verify that each warning disappears after the corresponding
    field is populated.
    """

    # Page Objects
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)
    empty_registration = RegistrationPageWarnings(page)

    # Generate test data
    random_data = RandomDataUtil()

    first_name = random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    phone = random_data.get_phone_number()
    password = random_data.get_password()

    # Navigate to Registration
    home_page.click_my_account()
    home_page.click_register()

    # Submit empty form
    registration_page.click_continue()

    # Verify warnings for empty mandatory fields
    expect(empty_registration.warning_privacy_policy()).to_be_visible()
    expect(empty_registration.warning_first_name()).to_be_visible()
    expect(empty_registration.warning_last_name()).to_be_visible()
    expect(empty_registration.warning_email()).to_be_visible()
    expect(empty_registration.warning_telephone()).to_be_visible()
    expect(empty_registration.warning_password()).to_be_visible()

    # Confirm Password warning should NOT appear initially
    expect(empty_registration.warning_confirm_password()).not_to_be_visible()

    # Accept Privacy Policy
    registration_page.set_privacy_policy()
    registration_page.click_continue()

    expect(empty_registration.warning_privacy_policy()).not_to_be_visible()

    # Enter First Name
    registration_page.set_first_name(first_name)
    registration_page.click_continue()

    expect(empty_registration.warning_first_name()).not_to_be_visible()

    # Enter Last Name
    registration_page.set_last_name(last_name)
    registration_page.click_continue()

    expect(empty_registration.warning_last_name()).not_to_be_visible()

    # Enter Email
    registration_page.set_email(email)
    registration_page.click_continue()

    expect(empty_registration.warning_email()).not_to_be_visible()

    # Enter Telephone
    registration_page.set_telephone(phone)
    registration_page.click_continue()

    expect(empty_registration.warning_telephone()).not_to_be_visible()

    # Enter Password
    registration_page.set_password(password)
    registration_page.click_continue()

    expect(empty_registration.warning_password()).not_to_be_visible()
    expect(empty_registration.warning_confirm_password()).to_be_visible()

    # Enter Confirm Password
    registration_page.set_confirm_password(password)
    registration_page.click_continue()

    expect(empty_registration.warning_confirm_password()).not_to_be_visible()

    # Verify Account Creation Confirmation ---
    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")