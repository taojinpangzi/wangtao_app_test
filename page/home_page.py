from common.operation import Operation


class HomePage(Operation):
    def tap_mine_button(self):
        super().tap_coordinate(x_coordinate=965, y_coordinate=2265)

    def click_login(self):
        super().click_xpath("//*[@text='登录/注册途虎会员']")

    def click_login_button(self):
        super().click_xpath("//*[@text='验证并登录']")
