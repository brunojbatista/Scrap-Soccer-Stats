# from DriverInterface import DriverInterface
from Library_v1.Driver.DriverInterface import DriverInterface
from Library_v1.Driver.DriverLock import DriverLock

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import undetected_chromedriver as uc

# from selenium_stealth import stealth

import os
import sys
import re

from Library_v1.Utils.file import (
    get_script_path,
    edit_chromedriver,
)

from Library_v1.Directory.Directory import Directory

# def get_script_path():
#     return os.path.dirname(os.path.realpath(sys.argv[0]))


class ChromeDriver(DriverInterface):

    def __init__(self, download_path: str = "Downloads/") -> None:
        super().__init__()
        self.driver = None;
        self.wait = None;
        self.options_browser = {}
        self.options = None
        self.download_path = None
        self.download_relativepath = None
        self.driver_lock = DriverLock()
        self.set_download_path(download_path)
        self.initialize_options()
    
    def initialize_options(self, ):
        self.options_browser = {
            "download.default_directory": self.download_path,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False,
            "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "useAutomationExtension": False,
            "excludeSwitches": ["enable-automation"],
        }

    def set_download_path(self, download_path: str):
        download = Directory(download_path)
        download.create()
        self.download_path = download.get_path()
        self.download_relativepath = download.get_relativepath()
    
    def get_download_path(self, ) -> str:
        return self.download_path
    
    def get_download_relativepath(self, ) -> str:
        return self.download_relativepath
    
    def find_download_file(self, searched_name, path = None):
        download = Directory(self.download_path)
        return download.find_file(searched_name, path)

    def lock(self, timeout : int = 30):
        self.driver_lock.lock(timeout);

    def unlock(self, ):
        self.driver_lock.unlock();
    
    def open(self, ):
        self.close()

        # -------------------------------------------------
        # Buscando do webdriver do chrome
        d = Directory("Library_v1/Driver/browsers/chrome/current")
        filepath = d.find_file(f"\.exe$");

        # -------------------------------------------------
        # Setando as opções
        if filepath:
            self.options = Options()
        else:
            self.options = uc.ChromeOptions()
        self.options.add_experimental_option("prefs", self.options_browser)
        self.options.page_load_strategy = 'normal'
        # self.options.page_load_strategy = 'eager'
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--verbose')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--safebrowsing-disable-download-protection')
        self.options.add_argument('--safebrowsing-disable-extension-blacklist')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument('--disable-web-security')
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument('--always-authorize-plugins=true')
        self.options.add_argument('--disable-dev-shm-usage')

        # -------------------------------------------------
        # Abrindo a instância do webdriver
        # self.driver = Chrome(
        #     service=ChromeService(ChromeDriverManager().install()), 
        #     options=self.options
        # )

        # -------------------------------------------------
        # Escolha do executável
        if filepath:
            self.driver = Chrome(
                service=ChromeService(executable_path=filepath), 
                options=self.options
            )
        else:
            # self.driver = Chrome(
            #     service=ChromeService(ChromeDriverManager().install()), 
            #     options=self.options
            # )
            self.driver = uc.Chrome(options=self.options)

            

        # self.driver.maximize_window()

    def get(self, ):
        return self.driver;

    def is_open(self, ) -> bool:
        return self.driver != None;

    def set_wait(self, timeout = 1, ref = None):
        if ref == None: ref = self.driver
        self.wait = WebDriverWait(
            ref, 
            timeout=timeout
        )
        return self;

    def set_condition(self, ec_function):
        if not(self.wait): raise ValueError("A espera não foi definida")
        return self.wait.until(ec_function)

    def get_url(self, url: str):
        self.driver.get(url)

    def get_session_id(self):
        return self.driver.session_id

    def get_title(self):
        return self.driver.title
    
    def refresh(self):
        return self.driver.refresh();

    def close(self):
        if self.driver: self.driver.close();

    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)

    def get_current_url(self, ):
        return self.driver.current_url

    def get_windows(self, ) -> list:
        return self.driver.window_handles;

    def get_current_window(self, ) -> str:
        return self.driver.current_window_handle

    def switch_window(self, handle: str):
        return self.driver.switch_to.window(handle)

    def new_window(self, ) -> str:
        self.driver.switch_to.new_window();
        return self.get_current_window();

    def close_tab(self, ):
        return self.driver.close();

    def clear_browser_data(self, ):
        self.driver.get('chrome://settings/clearBrowserData')

    def save_screenshot(self, name: str) -> str:
        name_formated = re.sub(r"\.[^\.]*$", '', name)
        name_formated = f"{name_formated}.jpg"
        self.driver.save_screenshot(name_formated)
        return name_formated;