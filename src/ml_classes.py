from __future__ import annotations
import dataclasses
import random
from typing import Iterable


@dataclasses.dataclass
class LinearModel:

    slope: float = 0.0
    intercept: float = 0.0
    _score: Optional[float] = None

    def score(self, y: Iterable[float], predictions: list[float]) -> float:
        """Calculates the score from y-coordinates and predictions"""
        differences = sum(
            [abs(y_ - prediction) for y_, prediction in zip(y, predictions)]
        )
        return 1 - differences

    def fit(
        self,
        x: Iterable[float],
        y: list[float],
        generations: int = 5,
    ) -> None:
        """Searches for best model across generations"""
        for _ in range(generations):
            new_model = self._do_step()
            predictions = new_model.predict(x)
            generation_score = new_model.score(y, predictions)
            # update self with attributes from the better model
            if self._score is None or generation_score > self._score:
                self.slope = new_model.slope
                self.intercept = new_model.intercept
                self._score = generation_score

    def predict(self, x: Iterable[float, int]) -> Iterable[float]:
        """Predict y value for each x value using model's attributes"""
        predictions = [self.slope * x_ + self.intercept for x_ in x]
        return predictions

    def _do_step(self) -> LinearModel:
        """Randomly changes instance attributes, returning a new model"""
        slope = self.slope + random.random() - 0.5
        intercept = self.intercept + random.random() - 0.5
        new_model = dataclasses.replace(self, slope=slope, intercept=intercept)
        return new_model
