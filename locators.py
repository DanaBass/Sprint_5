from selenium.webdriver.common.by import By


class TestLocators:
    ACCOUNT_LOGIN_LOCATOR = By.XPATH, "//button[text()='Войти в аккаунт']" # Кнопка "Войти в аккаунт"

    ACCOUNT_REGISTRATION_LOCATOR = By.XPATH, "//a[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"

    NAME_REGISTRATION = By.XPATH, "(//input[@name='name'])[1]" # Ввод имени для регистрации

    EMAIL_REGISTRATION = By.XPATH, "(//input[@name='name'])[2]" # Ввод email для регистрации

    PASSWORD_REGISTRATION = By.NAME, 'Пароль' # Ввод пароля для регистрации

    ACCOUNT_REGISTER = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка для подтверждения регистрации.

    LOCATOR_INCORRECT_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']" # Статический текст "Неправильный пароль".

    LOCATOR_AUTHORIZATION_EMAIL = By.NAME, 'name' # Ввод email для входа.

    LOCATOR_AUTHORIZATION_PASSWORD = By.NAME, 'Пароль' # Ввод пароля для входа.

    LOCATOR_LOGIN_BUTTON = By.XPATH, './/button[text()="Войти"]' # Кнопка "Войти" после авторизации.

    LOCATOR_PLACE_AN_ORDER = By.XPATH, './/button[text()="Оформить заказ"]' # Кнока "Оформить заказ", видна только зарегистрированным пользователям.

    LOCATOR_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']" # Вход в личный кабинет.

    LOCATOR_LOGIN = By.XPATH, "//a[text()='Войти']" # Вход в аккаунт через окно регистрации.

    LOCATOR_RESTORE_PASSWORD = By.CSS_SELECTOR, '.Auth_link__1fOlj' # Кнопка "Восстановить пароль".

    LOCATOR_LOGIN_RESTORE = By.LINK_TEXT, "Войти" # Кнопка "Войти".

    LOCATOR_CONSTRUCTOR = By.LINK_TEXT, "Конструктор" # Кнопка перехода в "Конструктор".

    LOCATOR_BUTTON_BURGER = By.XPATH, "//h1[text()='Соберите бургер']" # Текст "Соберите бургер".

    LOCATOR_LOGO = By.CSS_SELECTOR, 'svg[width="290"][height="50"]' # Логотип Stellar Burgers.

    LOCATOR_BUTTON_EXIT = By.XPATH, '//button[text()="Выход"]' # Кнопка для выхода из аккаунта.

    BUN_LOCATOR = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]" # Элемент с текстом 'Булки'.

    SAUCE_LOCATOR = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]" # Элемент с текстом 'Соусы'.

    FILLING_LOCATOR = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]"  # Элемент с текстом 'Начинки'.
