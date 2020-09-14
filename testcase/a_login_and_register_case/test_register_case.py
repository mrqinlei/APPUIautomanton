from base.base_driver import BaseDriver


class TestRegisterCase:


    def setup(self):
        self.register_page = BaseDriver.andriod_driver().to_login_page()