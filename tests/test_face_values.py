# coding=utf-8

from rummy.deck.face_values import FaceValues


class TestFaceValues:

    def test_face_values(self):
        face_values = FaceValues()
        assert ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K') == face_values.get()

    def test_face_values_is_value_in_range(self):
        face_values = FaceValues()
        assert face_values.is_value_in_range('A')
        assert face_values.is_value_in_range('2')
        assert face_values.is_value_in_range('5')
        assert face_values.is_value_in_range('7')
        assert face_values.is_value_in_range('T')
        assert face_values.is_value_in_range('J')
        assert face_values.is_value_in_range('Q')
        assert face_values.is_value_in_range('K')
