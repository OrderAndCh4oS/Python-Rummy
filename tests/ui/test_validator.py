# coding=utf-8

from rummy.ui.validator import Validator
from rummy.ui.view import View


class TestValidator:

    def test_valid_number_check(self, mocker):
        assert Validator.valid_number_check(8) == 8
        assert Validator.valid_number_check("5") == 5
        assert Validator.valid_number_check(4.5) == 4
        mocker.patch.object(View, "render")
        Validator.valid_number_check("!A!?K@210578")
        assert View.render.call_count == 1
