from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_IMG_HEADER = (By.CSS_SELECTOR, "#header_site_icon")
    LOGO_URL_HEADER = (By.CSS_SELECTOR, "#header_site_icon_url")
    MARKETPLACE_BTN_HEADER = (By.XPATH, "#marketplace-btn-header")
    BLOG_BTN_HEADER = (By.CSS_SELECTOR, "#blog-btn-header")
    BLOG_DROPDOWN_BTN_HEADER = (By.CSS_SELECTOR, "#dropdownNavbarLink")
    BLOG_DROPDOWN_DRIFT_BTN_HEADER = (By.CSS_SELECTOR, "#drift-category-header")
    BLOG_DROPDOWN_DRAG_BTN_HEADER = (By.CSS_SELECTOR, "#drag-category-header")
    BLOG_DROPDOWN_TA_BTN_HEADER = (By.CSS_SELECTOR, "#ta-category-header")
    CALENDAR_BTN_HEADER = (By.CSS_SELECTOR, "#calendar-header")
    ABOUT_US_BTN_HEADER = (By.CSS_SELECTOR, "#about-header")
    LOGIN_BTN_HEADER = (By.CSS_SELECTOR, "#login_btn_header")
    REGISTER_BTN_HEADER = (By.CSS_SELECTOR, "#signup_btn_header")
    AUTH_MESSAGES_BTN_HEADER = (By.CSS_SELECTOR, "#messages_btn_header")
    AUTH_LIKE_BTN_HEADER = (By.CSS_SELECTOR, "#")
    AUTH_USER_IMG_HEADER = (By.CSS_SELECTOR, "#username-img-header")
    AUTH_USERNAME_BTN_HEADER = (By.CSS_SELECTOR, "#username-header")
    AUTH_USERNAME_DROPDOWN_HEADER = (By.CSS_SELECTOR, "#dropdownAvatarNameButton")
    AUTH_MY_ITEMS_BTN_HEADER = (By.CSS_SELECTOR, "#")
    AUTH_MY_FAVORITES_BTN_HEADER = (By.CSS_SELECTOR, "#")
    AUTH_SETTINGS_BTN_HEADER = (By.CSS_SELECTOR, "#")
    AUTH_LOGOUT_BTN_HEADER = (By.CSS_SELECTOR, "#logout")
    MARKETPLACE_H2_FOOTER = (By.CSS_SELECTOR, "#marketplace-h2-footer")
    BLOG_H2_FOOTER = (By.CSS_SELECTOR, "#blog-h2-footer")
    PARTNERS_H2_FOOTER = (By.CSS_SELECTOR, "#partners-h2-footer")
    INFO_H2_FOOTER = (By.CSS_SELECTOR, "#info-heading-footer")
    CARS_CAT_BTN_FOOTER = (By.CSS_SELECTOR, "#cars-cat-footer")
    PARTS_CAT_BTN_FOOTER = (By.CSS_SELECTOR, "#parts-cat-footer")
    SERVICES_CAT_BTN_FOOTER = (By.CSS_SELECTOR, "#services-cat-footer")
    DRAG_BLOG_CAT_BTN_FOOTER = (By.CSS_SELECTOR, "#drag-cat-footer")
    DRIFT_BLOG_CAT_BTN_FOOTER = (By.CSS_SELECTOR, "#drift-cat-footer")
    TA_BLOG_CAT_BTN_FOOTER = (By.CSS_SELECTOR, "#ta-cat-footer")
    PARTNER_22RT_BTN_FOOTER = (By.CSS_SELECTOR, "#22rt-link-footer")
    PARTNER_ERAFAR_BTN_FOOTER = (By.CSS_SELECTOR, "#erafar-link-footer")
    PARTNER_RACELANE_BTN_FOOTER = (By.CSS_SELECTOR, "#racelane-link-footer")
    FAQ_BTN_FOOTER = (By.CSS_SELECTOR, "#faq-link-footer")
    ABOUT_BTN_FOOTER = (By.CSS_SELECTOR, "#about-link-footer")
    CONTACTS_BTN_FOOTER = (By.CSS_SELECTOR, "#")
    LOGO_FOOTER = (By.CSS_SELECTOR, "#")
    BRAND_NAME_FOOTER = (By.CSS_SELECTOR, "#sitename-footer")
    BRAND_DESCR_FOOTER = (By.CSS_SELECTOR, "#site-description-footer")
    COPYRIGHT_TEXT_FOOTER = (By.CSS_SELECTOR, "#copyright-text-footer")
    INTSTAGRAM_BTN_FOOTER = (By.CSS_SELECTOR, "#inst-link-footer")
    LINKEDIN_BTN_FOOTER = (By.CSS_SELECTOR, "#linkedin-link-footer")


class MainPageLocators:
    HERO_H1 = (By.CSS_SELECTOR, "h1")
    HERO_DESCR_TEXT = (By.CSS_SELECTOR, "#hero-descr-text")
    HERO_IMG = (By.CSS_SELECTOR, "#hero-img")
    HERO_MARKETPLACE_BTN = (By.CSS_SELECTOR, "#hero-marketplace-btn")
    HERO_ABOUT_US_BTN = (By.CSS_SELECTOR, "#hero-about-btn")
    ITEM_CARDS = (By.XPATH, "//*[contains(@id,'item-url')]")
    GO_TO_MARKETPLACE_BTN = (By.CSS_SELECTOR, "#go-to-marketplace-btn")
    BLOG_TITLE = (By.CSS_SELECTOR, "#blog-heading")
    BLOG_DESCR_TEXT = (By.CSS_SELECTOR, "#blog-description")
    EVENTS_COUNT = (By.CSS_SELECTOR, "#events-count")
    REPORTS_COUNT = (By.CSS_SELECTOR, "#reports-count")
    NEW_ITEMS_COUNT = (By.CSS_SELECTOR, "#new-items-count")
    POST_IMGS = (By.XPATH, "//*[contains(@id,'post-img')]")
    POST_READ_MORE_BTNS = (By.XPATH, "//*[contains(@id,'post-url')]")
    GO_TO_BLOG_BTN = (By.CSS_SELECTOR, "#go-to-blog-btn")
    OUR_PARTNERS_TITLE = (By.CSS_SELECTOR, "#our-partners-h2")
    PARTNER_22RT_LINK = (By.CSS_SELECTOR, "#rt22")
    PARTNER_22RT_IMG = (By.CSS_SELECTOR, "#rt22 img")
    PARTNER_R1_LINK = (By.CSS_SELECTOR, "#r1")
    PARTNER_R1_IMG = (By.CSS_SELECTOR, "#r1 img")
    PARTNER_TUMANOV_LINK = (By.CSS_SELECTOR, "#tumanov")
    PARTNER_TUMANOV_IMG = (By.CSS_SELECTOR, "#tumanov img")
    PARTNER_ERAFAR_LINK = (By.CSS_SELECTOR, "#erafar")
    PARTNER_ERAFAR_IMG = (By.CSS_SELECTOR, "#erafar img")
    PARTNER_RACELANE_LINK = (By.CSS_SELECTOR, "#racelane")
    PARTNER_RACELANE_IMG = (By.CSS_SELECTOR, "#racelane img")
    SUCCESS_MESSAGE_TEXT = (By.CSS_SELECTOR, "#")


class LoginPageLocators:
    LOGO_IMG = (By.CSS_SELECTOR, "#")
    LOGIN_FORM = (By.CSS_SELECTOR, "#")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SUBMIT_BTN = (By.CSS_SELECTOR, "body > div > div > div > div.mt-2.sm\:mx-auto.sm\:w-full.sm\:max-w-sm > form > div:nth-child(4) > button")
    REGISTER_LINK_BTN = (By.CSS_SELECTOR, "#")
    ERROR_MSG_TEXT = (By.CSS_SELECTOR, ".errorlist.nonfield > li")


class RegisterPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#registration_form")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD1_FIELD = (By.CSS_SELECTOR, "#password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#password2")
    USER_AGREEMENT_BTN = (By.CSS_SELECTOR, "#")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#")
    ERROR_MSG_TEXT = (By.CSS_SELECTOR, "#")


class MarketplacePageLocators:
    ALL_ITEMS_BTN = (By.CSS_SELECTOR, "#")
    CARS_CAT_BTN = (By.CSS_SELECTOR, "#")
    CARS_CAT_DROPDOWN_BTN = (By.CSS_SELECTOR, "#")
    PARTS_CAT_BTN = (By.CSS_SELECTOR, "#")
    PARTS_CAT_DROPDOWN_BTN = (By.CSS_SELECTOR, "#")
    SERVICES_CAT_BTN = (By.CSS_SELECTOR, "#")
    SERVICES_CAT_DROPDOWN_BTN = (By.CSS_SELECTOR, "#")
    WHEELS_CAT_BTN = (By.CSS_SELECTOR, "#")
    WHEELS_CAT_DROPDOWN_BTN = (By.CSS_SELECTOR, "#")
    SIMRACING_CAT_BTN = (By.CSS_SELECTOR, "#")
    SIMRACING_CAT_DROPDOWN_BTN = (By.CSS_SELECTOR, "#")
    KARTING_CAT_BTN = (By.CSS_SELECTOR, "#")
    KARTING_CAT_DROPDOWN_BTN = (By.CSS_SELECTOR, "#")
    NEW_ITEM_BTN = (By.CSS_SELECTOR, "#")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#")
    SEARCH_BTN_SUBMIT = (By.CSS_SELECTOR, "#")
    CATEGORIES_DROPDOWN = (By.CSS_SELECTOR, "#")
    NEW_ITEMS_SORTING_BTN = (By.CSS_SELECTOR, "#")
    OLD_ITEMS_SORTING_BTN = (By.CSS_SELECTOR, "#")
    ITEM_CARD = (By.CSS_SELECTOR, "#")
    ITEM_IMG = (By.CSS_SELECTOR, "#")
    ITEM_LIKE_BTN = (By.CSS_SELECTOR, "#")
    ITEM_CATEGORY_NAME = (By.CSS_SELECTOR, "#")
    ITEM_TITLE = (By.CSS_SELECTOR, "#")
    ITEM_PRICE = (By.CSS_SELECTOR, "#")
    ITEM_CITY = (By.CSS_SELECTOR, "#")
    ITEM_PUBLISH_DATE = (By.CSS_SELECTOR, "#")
    ITEMS_PER_PAGE = (By.CSS_SELECTOR, "#")
    ITEMS_QUANTITY_OVERALL = (By.CSS_SELECTOR, "#")
    PAGE_NUMBER = (By.CSS_SELECTOR, "#")
    LEFT_PAGINATION_BTN = (By.CSS_SELECTOR, "#")
    RIGHT_PAGINATION_BTN = (By.CSS_SELECTOR, "#")


class ItemPageLocators:
    BREADCRUMB_HOME_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_MARKETPLACE_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_CATEGORY_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_SUBCATEGORY_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_ITEM_NAME = (By.CSS_SELECTOR, "#")
    ITEM_MAIN_IMG = (By.CSS_SELECTOR, "#")
    ITEM_ADDITIONAL_IMG_1 = (By.CSS_SELECTOR, "#")
    ITEM_ADDITIONAL_IMG_2 = (By.CSS_SELECTOR, "#")
    ITEM_ADDITIONAL_IMG_3 = (By.CSS_SELECTOR, "#")
    ITEM_ADDITIONAL_IMG_4 = (By.CSS_SELECTOR, "#")
    ITEM_IMG_SLIDER_LEFT_BTN = (By.CSS_SELECTOR, "#")
    ITEM_IMG_SLIDER_RIGHT_BTN = (By.CSS_SELECTOR, "#")
    ITEM_DATE_PUBLISHED = (By.CSS_SELECTOR, "#")
    ITEM_DATE_UPDATED = (By.CSS_SELECTOR, "#")
    ITEM_CATEGORY_NAME = (By.CSS_SELECTOR, "#")
    ITEM_NAME = (By.CSS_SELECTOR, "#")
    ITEM_CITY = (By.CSS_SELECTOR, "#")
    ITEM_REGION = (By.CSS_SELECTOR, "#")
    ITEM_CURRENCY = (By.CSS_SELECTOR, "#")
    ITEM_PRICE = (By.CSS_SELECTOR, "#")
    ITEM_CURR_CONVERTED_PRICE = (By.CSS_SELECTOR, "#")
    AUTHOR_LINK = (By.CSS_SELECTOR, "#")
    YOU_ARE_THE_AUTHOR_TEXT = (By.CSS_SELECTOR, "#")
    EDIT_ITEM_BTN = (By.CSS_SELECTOR, "#")
    MESSAGE_ITEM_BTN = (By.CSS_SELECTOR, "#")
    PHONE_NUM_BTN = (By.CSS_SELECTOR, "#")
    PHONE_NUM_DROPDOWN_TEXT = (By.CSS_SELECTOR, "#")
    LIKES_COUNT = (By.CSS_SELECTOR, "#")
    LIKE_BTN = (By.CSS_SELECTOR, "#")
    SIMILAR_ITEM_CARD = (By.CSS_SELECTOR, "#")


class BlogPageLocators:
    BLOG_H2 = (By.CSS_SELECTOR, "#")
    BLOG_H1 = (By.CSS_SELECTOR, "#")
    BLOG_DESCRIPTION_TEXT = (By.CSS_SELECTOR, "#")
    ALL_CATEGORIES_BTN = (By.CSS_SELECTOR, "#")
    DRIFT_CATEGORY_BTN = (By.CSS_SELECTOR, "#")
    TIME_ATTACK_CATEGORY_BTN = (By.CSS_SELECTOR, "#")
    INSTAGRAM_BTN = (By.CSS_SELECTOR, "#")
    POST_TITLE = (By.CSS_SELECTOR, "#")
    POST_IMG = (By.CSS_SELECTOR, "#")
    POST_LIKE_BTN = (By.CSS_SELECTOR, "#")
    POST_LIKES_COUNT = (By.CSS_SELECTOR, "#")
    POST_COMMENTS_BTN = (By.CSS_SELECTOR, "#")
    POST_COMMENTS_COUNT = (By.CSS_SELECTOR, "#")
    POST_CATEGORY_BTN = (By.CSS_SELECTOR, "#")
    POST_DATE_PUBLISHED = (By.CSS_SELECTOR, "#")
    POST_AUTHOR_NAME = (By.CSS_SELECTOR, "#")
    POST_AUTHOR_IMG = (By.CSS_SELECTOR, "#")


class BlogCategoryPageLocators:
    POST_TITLE = (By.CSS_SELECTOR, "#")
    POST_IMG = (By.CSS_SELECTOR, "#")
    POST_LIKE_BTN = (By.CSS_SELECTOR, "#")
    POST_LIKES_COUNT = (By.CSS_SELECTOR, "#")
    POST_COMMENTS_BTN = (By.CSS_SELECTOR, "#")
    POST_COMMENTS_COUNT = (By.CSS_SELECTOR, "#")
    POST_CATEGORY_BTN = (By.CSS_SELECTOR, "#")
    POST_DATE_PUBLISHED = (By.CSS_SELECTOR, "#")
    POST_AUTHOR_NAME = (By.CSS_SELECTOR, "#")
    POST_AUTHOR_IMG = (By.CSS_SELECTOR, "#")


class BlogPostPageLocators:
    BREADCRUMB_HOME_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_BLOG_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_CATEGORY_BTN = (By.CSS_SELECTOR, "#")
    BREADCRUMB_POST_NAME = (By.CSS_SELECTOR, "#")
    POST_TITLE = (By.CSS_SELECTOR, "#")
    POST_IMG_MAIN = (By.CSS_SELECTOR, "#")
    POST_TEXT_BODY = (By.CSS_SELECTOR, "#")
    POST_AUTHOR_NAME = (By.CSS_SELECTOR, "#")
    POST_AUTHOR_IMG = (By.CSS_SELECTOR, "#")
    POST_LIKE_BTN = (By.CSS_SELECTOR, "#")
    POST_LIKES_COUNT = (By.CSS_SELECTOR, "#")
    COMMENTS_COUNT = (By.CSS_SELECTOR, "#")
    SEPARATE_COMMENT_SECTION = (By.CSS_SELECTOR, "#")
    COMMENT_AUTHOR_NAME = (By.CSS_SELECTOR, "#")
    COMMENT_DATE_PUBLISHED = (By.CSS_SELECTOR, "#")
    COMMENT_LIKE_BTN = (By.CSS_SELECTOR, "#")
    COMMENT_LIKES_COUNT = (By.CSS_SELECTOR, "#")
    COMMENT_SUCCESS_MSG_TEXT = (By.CSS_SELECTOR, "#")
    SIMILAR_POSTS_CATEGORY_NAME = (By.CSS_SELECTOR, "#")
    SIMILAR_POSTS_CARD = (By.CSS_SELECTOR, "#")


class CalendarPageLocators:
    CURRENT_MM_YY_TEXT = (By.CSS_SELECTOR, "#")
    TODAY_BTN = (By.CSS_SELECTOR, "#")
    PREV_MONTH_BTN = (By.CSS_SELECTOR, "#")
    NEXT_MONTH_BTN = (By.CSS_SELECTOR, "#")
    CURRENT_DAY_CARD = (By.CSS_SELECTOR, "#")
    DRIFT_BTN = (By.CSS_SELECTOR, "#")
    TIME_ATTACK_BTN = (By.CSS_SELECTOR, "#")
    DRAG_BTN = (By.CSS_SELECTOR, "#")
    RT_BTN = (By.CSS_SELECTOR, "#")
    DRIFT_TRAINING_BTN = (By.CSS_SELECTOR, "#")
    CONTACT_FORM_LINK = (By.CSS_SELECTOR, "#")
    AUTH_CONTACT_FORM = (By.CSS_SELECTOR, "#")


class AboutPageLocators():
    H2_TEXT = (By.CSS_SELECTOR, "#")


class ContactPageLocators():
    MAIN_IMAGE = (By.CSS_SELECTOR, "#")
    DESCRIPTION_TEXT = (By.CSS_SELECTOR, "#")
    INSTAGRAM_BTN = (By.CSS_SELECTOR, "#")
    EMAIL_BTN = (By.CSS_SELECTOR, "#")
    TG_BTN = (By.CSS_SELECTOR, "#")
    CONTACT_FORM = (By.CSS_SELECTOR, "#")
    NAME_FIELD = (By.CSS_SELECTOR, "#")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#")
    MESSAGE_FIELD = (By.CSS_SELECTOR, "#")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#")
    USER_AGREEMENT_TEXT = (By.CSS_SELECTOR, "#")
    USER_AGREEMENT_LINK = (By.CSS_SELECTOR, "#")


class ModerationPageLocators():
    ITEM_CARD = (By.CSS_SELECTOR, "#")
    MODERATE_ITEM_BTN = (By.CSS_SELECTOR, "#")
    EDIT_ITEM_BTN = (By.CSS_SELECTOR, "#")
    GO_TO_MARKEPLACE_BTN = (By.CSS_SELECTOR, "#")
    COMMENT_CARD = (By.CSS_SELECTOR, "#")


class NewItemPageLocators():
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "#")
    SUBCATEGORY_DROPDOWN = (By.CSS_SELECTOR, "#")
    ITEM_NAME_FIELD = (By.CSS_SELECTOR, "#")
    ITEM_DESCR_FIELD = (By.CSS_SELECTOR, "#")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#")
    PRICE_FIELD = (By.CSS_SELECTOR, "#")
    REGION_FIELD = (By.CSS_SELECTOR, "#")
    CITY_FIELD = (By.CSS_SELECTOR, "#")
    SHOW_NUMBER_CHECKBOX = (By.CSS_SELECTOR, "#")
    MAIN_IMG_FIELD = (By.CSS_SELECTOR, "#")
    IMAGES_ACCORDION_BTN = (By.CSS_SELECTOR, "#")
    ADDITIONAL_PHOTO_1_FIELD = (By.CSS_SELECTOR, "#")
    ADDITIONAL_PHOTO_2_FIELD = (By.CSS_SELECTOR, "#")
    ADDITIONAL_PHOTO_3_FIELD = (By.CSS_SELECTOR, "#")
    ADDITIONAL_PHOTO_4_FIELD = (By.CSS_SELECTOR, "#")
    CANCEL_BTN = (By.CSS_SELECTOR, "#")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#")


class MyItemsPageLocators():
    ITEMS_COUNT = (By.CSS_SELECTOR, "#")
    HIDE_BTN = (By.CSS_SELECTOR, "#")
    EDIT_BTN = (By.CSS_SELECTOR, "#")
    DELETE_BTN = (By.CSS_SELECTOR, "#")
    DELETED_POPOVER = (By.CSS_SELECTOR, "#")
    ON_MODERATION_POPOVER = (By.CSS_SELECTOR, "#")
    ITEM_CARD = (By.CSS_SELECTOR, "#")
    NEW_ITEM_SIDEBAR_BTN = (By.CSS_SELECTOR, "#")
    MY_ITEMS_SIDEBAR_BTN = (By.CSS_SELECTOR, "#")
    MY_ITEMS_COUNT_SIDEBAR_TEXT = (By.CSS_SELECTOR, "#")
    CHATS_SIDEBAR_BTN = (By.CSS_SELECTOR, "#")
    CHATS_COUNT_SIDEBAR_TEXT = (By.CSS_SELECTOR, "#")
    FAVORITES_SIDEBAR_BTN = (By.CSS_SELECTOR, "#")
    PUBLIC_PROFILE_SIDEBAR_BTN = (By.CSS_SELECTOR, "#")
    ACC_SETTINGS_SIDEBAR_BTN = (By.CSS_SELECTOR, "#")


class ChatPageLocators():
    ITEM_CHAT_BTN = (By.CSS_SELECTOR, "#")


class FavoritesPageLocators():
    ITEMS_COUNT = (By.CSS_SELECTOR, "#")
    ITEM_CARD = (By.CSS_SELECTOR, "#")
    POSTS_COUNT = (By.CSS_SELECTOR, "#")
    POST_CARD = (By.CSS_SELECTOR, "#")


class PublicProfilePageLocators():
    USER_NAME_TEXT = (By.CSS_SELECTOR, "#")
    USER_CREATION_DATE = (By.CSS_SELECTOR, "#")
    ITEM_CARD = (By.CSS_SELECTOR, "#")


class EditProfilePageLocators():
    PHONE_CODE_FIELD = (By.CSS_SELECTOR, "#")
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, "#")
    NAME_FIELD = (By.CSS_SELECTOR, "#")
    IMAGE_FIELD = (By.CSS_SELECTOR, "#")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "#")
    NEWS_CHECKBOX = (By.CSS_SELECTOR, "#")