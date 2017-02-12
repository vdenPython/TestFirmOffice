# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.login_admin_django(username= "test", password= "test12345")
    app.create_group(Group(name= "test1"))
    app.logout_admin_django()
