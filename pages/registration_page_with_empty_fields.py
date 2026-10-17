# registration_page.py
from playwright.sync_api import Page


class RegistrationPageWarnings:
    """
    Page Object Model class for the Registration Page if we enter blank inputs.
    This class contains web element locators and methods (actions)
    to interact with the registration form.
    """

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        # Warning for Input fields
        self.txt_blank_firstname = page.locator("//div[contains(text(),'First Name must be between 1 and 32 characters!')]")
        self.txt_blank_lastname = page.locator("//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")
        self.txt_blank_email = page.locator("//div[contains(text(),'E-Mail Address does not appear to be valid!')]")
        self.txt_blank_telephone = page.locator("//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")
        self.txt_blank_password = page.locator("//div[contains(text(),'Password must be between 4 and 20 characters!')]")
        self.txt_blank_confirm_password = page.locator("//div[contains(text(),'Password confirmation does not match password!')]")
        self.txt_blank_privacy_policy = page.locator("div.alert.alert-danger.alert-dismissible i")

        # Already existing warnings
        self.email_exists = page.locator("//div[contains(text(),'Warning: E-Mail Address is already registered!')]")






    # ===== Action Methods =====

    def warning_first_name(self):
        return self.txt_blank_firstname

    def warning_last_name(self):
        return self.txt_blank_lastname

    def warning_email(self):
        return self.txt_blank_email
    def warning_telephone(self):
        return self.txt_blank_telephone

    def warning_password(self):
        return self.txt_blank_password

    def warning_confirm_password(self):
        return self.txt_blank_confirm_password

    def warning_privacy_policy(self):
        return self.txt_blank_privacy_policy

    def email_exists_warning(self):
        return self.email_exists
