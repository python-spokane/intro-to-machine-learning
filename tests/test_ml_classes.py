from src.ml_classes import LinearModel


def test__linear_model__uses_init_args__slope():
    assert LinearModel(slope=1).slope == 1


def test__linear_model__uses_init_args__intercept():
    assert LinearModel(intercept=1).intercept == 1


def test__linear_model__uses_init_args__uses_defaults():
    model = LinearModel()
    assert model.slope == 0
    assert model.intercept == 0
