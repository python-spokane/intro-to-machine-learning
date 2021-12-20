from .ml_classes import LinearModel


if __name__ == "__main__":
    model = LinearModel()
    model.fit([1, 2, 3], [10, 11, 12], generations=200)
    prediction = model.predict([1, 2, 3])
    print(prediction)
