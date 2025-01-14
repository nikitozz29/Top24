from MainPage import *
from KostromaPage import *


def test_chrome_main_page_nav_bar(chrome):
    top_news_page = MainPage(chrome)
    top_news_page.go_to_main_page()
    if top_news_page.check_on_close_button():
        top_news_page.check_on_close_button().click()
    if top_news_page.check_on_tg_close():
        top_news_page.check_on_tg_close().click()
    elements = top_news_page.check_nav_bar()
    assert "МОСКВА\nРОССИЯ\nЭКОНОМИКА\nМЕГАМИКС 90-Х\nПРОИСШЕСТВИЯ" in elements


def test_chrome_check_cityes(chrome):
    top_news_page = MainPage(chrome)
    # top_news_page.go_to_main_page()
    # if top_news_page.check_on_close_button():
    #     top_news_page.check_on_close_button().click()
    # if top_news_page.check_on_tg_close():
    #     top_news_page.check_on_tg_close().click()
    top_news_page.click_on_city_select()
    cityes = top_news_page.check_cityes()
    assert "Москва\nКиров\nКострома\nКрым\nНижневартовск\nОмск\nРязань\nСочи\nУльяновск\nШарья" in cityes


def test_chrome_check_kostroma(chrome):
    top_news_page = MainPage(chrome)
    top_news_page.click_on_city_select()
    top_news_page.check_kostroma_page().click()
    kostroma_page = KostromaPage(chrome)
    if kostroma_page.check_on_close_button():
        kostroma_page.check_on_close_button().click()
    if kostroma_page.check_on_tg_close():
        kostroma_page.check_on_tg_close().click()
    elements = kostroma_page.check_nav_bar()
    assert "КРУПНЫМ ПЛАНОМ\nШЕФ ШАРОВ\nЗОНА СВО\nЭТО У НАС СЕМЕЙНОЕ" in elements


def test_firefox_main_page_nav_bar(firefox):
    top_news_page = MainPage(firefox)
    top_news_page.go_to_main_page()
    if top_news_page.check_on_close_button():
        top_news_page.check_on_close_button().click()
    if top_news_page.check_on_tg_close():
        top_news_page.check_on_tg_close().click()
    elements = top_news_page.check_nav_bar()
    assert "МОСКВА\nРОССИЯ\nЭКОНОМИКА\nМЕГАМИКС 90-Х\nПРОИСШЕСТВИЯ" in elements


def test_firefox_check_cityes(firefox):
    top_news_page = MainPage(firefox)
    # top_news_page.go_to_main_page()
    # if top_news_page.check_on_close_button():
    #     top_news_page.check_on_close_button().click()
    # if top_news_page.check_on_tg_close():
    #     top_news_page.check_on_tg_close().click()
    top_news_page.click_on_city_select()
    cityes = top_news_page.check_cityes()
    assert "Москва\nКиров\nКострома\nКрым\nНижневартовск\nОмск\nРязань\nСочи\nУльяновск\nШарья" in cityes


def test_firefox_check_kostroma(firefox):
    top_news_page = MainPage(firefox)
    top_news_page.click_on_city_select()
    top_news_page.check_kostroma_page().click()
    kostroma_page = KostromaPage(firefox)
    if kostroma_page.check_on_close_button():
        kostroma_page.check_on_close_button().click()
    if kostroma_page.check_on_tg_close():
        kostroma_page.check_on_tg_close().click()
    elements = kostroma_page.check_nav_bar()
    assert "КРУПНЫМ ПЛАНОМ\nШЕФ ШАРОВ\nЗОНА СВО\nЭТО У НАС СЕМЕЙНОЕ" in elements
