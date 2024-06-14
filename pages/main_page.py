from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_displayed(*BasePageLocators.LOGIN_BTN_HEADER), "There is no login link"

    def should_be_hero_h1_with_text(self):
        assert self.result_text(*MainPageLocators.HERO_H1) == "Продажа тюнинг-запчастей и авто в РБ",\
            "The text of hero h1 is different."

    def should_be_hero_descr_text(self):
        assert self.result_text(*MainPageLocators.HERO_DESCR_TEXT) == "Покупай, продавай и обменивай " \
                                                                      "тюнинг-запчасти онлайн. " \
                                                                      "Все в одном месте с Race.",\
            "The text of hero description is different."

    def should_be_hero_img(self):
        hero_img = self.browser.find_element(*MainPageLocators.HERO_IMG)
        img_path = hero_img.get_attribute("src")
        assert img_path[-27:] == "bmw_m4-removebg-preview.png", "The image name is other"

    def click_hero_marketplace_btn(self):
        self.click_button(*MainPageLocators.HERO_MARKETPLACE_BTN)
        assert self.browser.current_url == "https://race-marketplace.by/items/"

    def click_hero_about_us_btn(self):
        self.click_button(*MainPageLocators.HERO_ABOUT_US_BTN)
        assert self.browser.current_url == "https://race-marketplace.by/about/"

    def count_item_cards_qty(self):
        cards = self.browser.find_elements(*MainPageLocators.ITEM_CARDS)
        assert len(cards) == 10,  "The qty of cards at main page is not 10."

    def click_go_to_marketplace_btn(self):
        self.click_button(*MainPageLocators.GO_TO_MARKETPLACE_BTN)
        assert self.browser.current_url == "https://race-marketplace.by/items/"

    def should_be_blog_h2(self):
        assert self.is_displayed(*MainPageLocators.BLOG_TITLE), "There is no blog H2."

    def should_be_blog_description(self):
        assert self.is_displayed(*MainPageLocators.BLOG_DESCR_TEXT), "There is no blog description text."
        assert self.result_text(*MainPageLocators.BLOG_DESCR_TEXT) == "Фотоотчеты, новости и результаты " \
                                                                      "соревнований, Drift, Time-Attack и Drag. " \
                                        "А также календарь автоспортивных мероприятий в Беларуси на 2024 год.", \
            "The description text is different"

    def check_counters(self):
        assert self.is_displayed(*MainPageLocators.EVENTS_COUNT), "El is not presented"
        assert self.result_text(*MainPageLocators.EVENTS_COUNT) == '100+', 'The events count text is different'
        assert self.is_displayed(*MainPageLocators.REPORTS_COUNT), "El is not presented"
        assert self.result_text(*MainPageLocators.REPORTS_COUNT) == '30+', 'The reports count text is different'
        assert self.is_displayed(*MainPageLocators.NEW_ITEMS_COUNT), "El is not presented"
        assert self.result_text(*MainPageLocators.NEW_ITEMS_COUNT) == '10+', 'The new items count text is different'

    def click_go_to_blog_btn(self):
        self.click_button(*MainPageLocators.GO_TO_BLOG_BTN)
        assert self.browser.current_url == "https://race-marketplace.by/blog/"

    def check_our_partners_h2_text(self):
        assert self.is_displayed(*MainPageLocators.OUR_PARTNERS_TITLE), "El is not presented"
        assert self.result_text(*MainPageLocators.OUR_PARTNERS_TITLE) == "Наши партнеры",\
            "The text of blog h2 is different."

    def check_our_partners_images(self):
        assert self.is_displayed(*MainPageLocators.PARTNER_22RT_IMG), "22rt img is not presented"
        assert self.is_displayed(*MainPageLocators.PARTNER_R1_IMG), "Racing.by link is not presented"
        assert self.is_displayed(*MainPageLocators.PARTNER_TUMANOV_IMG), "Tumanov img is not presented"
        assert self.is_displayed(*MainPageLocators.PARTNER_ERAFAR_IMG), "ERAFAR img is not presented"
        assert self.is_displayed(*MainPageLocators.PARTNER_RACELANE_IMG), "Racelane img is not presented"

    def check_our_partners_links(self):
        assert self.result_href(*MainPageLocators.PARTNER_22RT_LINK) == "https://www.instagram.com/22rt_trackday/", \
            "The 22rt href is different."
        assert self.result_href(*MainPageLocators.PARTNER_R1_LINK) == "https://racing.by/", \
            "The Racing.by href is different."
        assert self.result_href(*MainPageLocators.PARTNER_TUMANOV_LINK) == "https://www.instagram.com/tumanov_photo/", \
            "The Tumanov href is different."
        assert self.result_href(*MainPageLocators.PARTNER_ERAFAR_LINK) == "https://www.instagram.com/erafar.by", \
            "The ERAFAR href is different."
        assert self.result_href(*MainPageLocators.PARTNER_RACELANE_LINK) == "https://www.instagram.com/racelaneapp/", \
            "The Racelane href is different."

