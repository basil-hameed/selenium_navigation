"""
test_homepage.py - Python selenium scripts for executing tests
"""
from homepage import HRMLogin
import pytest

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
orange_hrm = HRMLogin(url)

def test_valid_login():
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    assert orange_hrm.login() == expected_url

