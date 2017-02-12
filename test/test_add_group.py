# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.session.login_admin_django(username= "test", password= "test12345")
    app.create_group(Group(name= "test1"))
    app.session.logout_admin_django()
