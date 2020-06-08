# coding:utf-8
import pytest
import allure
import inspect
import logging
from Base.assert_method import Assert_method


@allure.feature("Login_activity_case")
class Test_login_page_case:

    @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_DLZC1(self, login_page_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_page_class_load.login_by_config_url()
        username_input_attribute_value = login_page_class_load.get_username_attribute_value()
        Assert_method.assert_equal_screen_shot(function_driver, (username_input_attribute_value, "手机号码"))

    # @allure.story("Login")
    # @allure.severity("normal")
    # @allure.title("test")
    # def test_DLZC2(self, login_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_reset_btn()
    #     reset_title = login_page_class_load.get_reset_page_title()
    #     Assert_method.assert_equal_screen_shot(function_driver, (reset_title, "找回密码"))

    # @allure.story("Login")
    # @allure.severity("normal")
    # @allure.title("test")
    # def test_DLZC3(self, login_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_register_btn()
    #     register_title = login_page_class_load.get_register_page_title()
    #     Assert_method.assert_equal_screen_shot(function_driver, (register_title, "注册"))
    #
    # @allure.story("Login")
    # @allure.severity("normal")
    # @allure.title("test")
    # def test_DLZC4(self, login_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.click_login_btn()
    #     error_text = login_page_class_load.get_error_text()
    #     Assert_method.assert_equal_screen_shot(function_driver, (error_text, "注册"))
    #
    # @allure.story("Login")
    # @allure.severity("normal")
    # @allure.title("test")
    # def test_DLZC5(self, login_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.username_send_keys(1)
    #     login_page_class_load.click_login_btn()
    #     error_text = login_page_class_load.get_error_text()
    #     Assert_method.assert_equal_screen_shot(function_driver, (error_text, "密码不能为空"))
    #
    # @allure.story("Login")
    # @allure.severity("normal")
    # @allure.title("test")
    # def test_DLZC6(self, login_page_class_load, function_driver):
    #     login_page_class_load.login_by_config_url()
    #     login_page_class_load.username_send_keys("1")
    #     login_page_class_load.password_send_keys("1")
    #     login_page_class_load.click_login_btn()
    #     error_text = login_page_class_load.get_error_text()
    #     Assert_method.assert_equal_screen_shot(function_driver, (error_text, "账号不存在"))


if __name__ == "__main__":
    pytest.main(["test_login_activity_case.py"])
