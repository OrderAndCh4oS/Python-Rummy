# coding=utf-8

from rummy.deck.face_values import FaceValues


class TestFaceValues:

    def test_face_values(self):
        assert ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K') == FaceValues.get()

    def test_face_values_is_value_in_range(self):
        assert FaceValues.is_value_in_range('A')
        assert FaceValues.is_value_in_range('2')
        assert FaceValues.is_value_in_range('5')
        assert FaceValues.is_value_in_range('7')
        assert FaceValues.is_value_in_range('T')
        assert FaceValues.is_value_in_range('J')
        assert FaceValues.is_value_in_range('Q')
        assert FaceValues.is_value_in_range('K')
