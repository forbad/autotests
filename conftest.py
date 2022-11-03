import os
import json
import pytest
from settings import *
from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App


@fixture(scope='session')
def get_playwright():
    """
    returns single instance of playwright itself
    :return:
    """
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session', params=['chromium'])
def get_browser(get_playwright, request):
    browser = request.param
    # save browser type to env variable so fixtures and tests can get current browser
    # Needed to skip unused browser-test combinations
    os.environ['PWBROWSER'] = browser
    headless = request.config.getini('headless')
    if headless == 'True':
        headless = True
    else:
        headless = False

    if browser == 'chromium':
        bro = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        bro = get_playwright.firefox.launch(headless=headless)
    elif browser == 'webkit':
        bro = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'

    yield bro
    bro.close()
    del os.environ['PWBROWSER']


@fixture(scope='session')
def desktop_app(get_browser, request):
    """
    Fixture of playwright for non autorised tests
    """
    base_url = request.config.getini('base_url')
    app = App(get_browser, base_url=base_url, **BROWSER_OPTIONS)
    app.goto("/main_unauthorised")
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = desktop_app
    app.login(**config['user'])
    yield app


@fixture(scope='session', params=['iPhone 11', 'Pixel 2'])
def mobile_app(get_playwright, get_browser, request):
    if os.environ.get('PWBROWSER') == 'firefox':
        pytest.skip()
    base_url = request.config.getini('base_url')
    device = request.param
    device_config = get_playwright.devices.get(device)
    if device_config is not None:
        device_config.update(BROWSER_OPTIONS)
    else:
        device_config = BROWSER_OPTIONS
    app = App(get_browser, base_url=base_url, **device_config)
    app.goto('/')
    app.goto("/main_unauthorised")
    yield app
    app.close()


@fixture(scope='session')
def mobile_app_auth(mobile_app, request):
    secure = request.config.getoption('--secure')
    config = load_config(request.session.fspath.strpath, secure)
    app = mobile_app
    app.login(**config['user'])
    yield app


def pytest_addoption(parser):
    parser.addoption('--secure', action='store', default='secure.json')
    parser.addini('base_url', help='base url of site under test', default='https://test-ib.mybank.by')
    parser.addini('headless', help='run browser in headless mode', default='True')
    parser.addini('tcm_report', help='report test results to tcm', default='False')


# request.session.fspath.strpath - path to project root
def load_config(project_path: str, file: str) -> dict:
    config_file = os.path.join(project_path, file)
    with open(config_file) as cfg:
        return json.loads(cfg.read())
