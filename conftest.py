import os
import json
from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop_app(get_playwright, request):
    base_url = request.config.getoption('--base_url')
    app = App(get_playwright, base_url=base_url)
    app.goto("/main_unauthorised")
    yield app
    app.close()


@fixture
def desktop_app_auth(desktop_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(secure)
    app = desktop_app
    app.login(**config['user'])
    yield app


def pytest_addoption(parser):
    parser.addoption('--base_url', help='store', default='https://test-ib.mybank.by')
    parser.addoption('--secure', help='store', default='secure.json')


def load_config(file):
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())
