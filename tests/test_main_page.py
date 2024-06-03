import time
from pages.main_page import MainPage


link = "https://race-marketplace.by"


def test_guest_get_status_code_200_tc_id1(browser):
    """Checking the status code of the page, it should be 200."""
    page = MainPage(browser, link)
    page.assert_status_code_200()


def test_check_page_title_tc_id2(browser):
    """Checking the page title"""
    page = MainPage(browser, link)
    page.open()
    page.assert_page_title("Главная страница | Race-Marketplace.by")


def test_guest_should_see_hero_h1_tc_id3(browser):
    """Checking the h1 title."""
    page = MainPage(browser, link)
    page.open()
    page.should_be_hero_h1_with_text()


def test_guest_should_see_hero_h1_tc_id4(browser):
    """Checking the text under the h1 title."""
    page = MainPage(browser, link)
    page.open()
    page.should_be_hero_descr_text()


def test_guest_should_see_hero_img_tc_id5(browser):
    """Checking the hero image, it should be 'bmw_m4-removebg-preview.png'."""
    page = MainPage(browser, link)
    page.open()
    page.should_be_hero_img()


def test_guest_can_click_hero_marketplace_btn_tc_id6(browser):
    """Clicking the 'go to marketplace' button at the hero section."""
    page = MainPage(browser, link)
    page.open()
    page.click_hero_marketplace_btn()


def test_guest_can_click_hero_about_us_btn_tc_id7(browser):
    """Clicking the 'About us' button at the hero section."""
    page = MainPage(browser, link)
    page.open()
    page.click_hero_about_us_btn()


def test_guest_can_see_10_items_tc_id8(browser):
    """Finding 10 item cards and counting it."""
    page = MainPage(browser, link)
    page.open()
    page.count_item_cards_qty()


def test_guest_can_click_go_to_marketplace_btn_tc_id9(browser):
    """Clicking the 'Go to marketplace' under the items."""
    page = MainPage(browser, link)
    page.open()
    page.click_go_to_marketplace_btn()


def test_guest_should_see_blog_h2_tc_id10(browser):
    """Checking the h2 blog title."""
    page = MainPage(browser, link)
    page.open()
    page.should_be_blog_h2()


def test_guest_should_see_blog_description_tc_id11(browser):
    """Checking the h2 blog description text."""
    page = MainPage(browser, link)
    page.open()
    page.should_be_blog_description()


def test_guest_should_see_blog_counters_tc_id12(browser):
    """Checking the blog counter numbers."""
    page = MainPage(browser, link)
    page.open()
    page.check_counters()


def test_guest_can_click_go_to_blog_btn_tc_id15(browser):
    """Clicking go to blog button."""
    page = MainPage(browser, link)
    page.open()
    page.click_go_to_blog_btn()


def test_guest_can_partners_images_and_links_tc_id17(browser):
    """Checking the presence of partners images and asserting the links."""
    page = MainPage(browser, link)
    page.open()
    page.check_our_partners_images()
    page.check_our_partners_links()


def test_guest_tc_id16(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_tc_id17(browser):
    page = MainPage(browser, link)
    page.open()



def test_guest_tc_id18(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_tc_id19(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_tc_id20(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_tc_id21(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_tc_id22(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_tc_id23(browser):
    page = MainPage(browser, link)
    page.open()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_tc_id25(browser):
    page = MainPage(browser, link)
    page.open()
    page.click_login_btn_header()
