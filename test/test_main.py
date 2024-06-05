from src import main
from classes.Activity import Activity


class TestActivity:

    def test_class_instance(self):
        a = Activity()
        assert isinstance(a, Activity)

