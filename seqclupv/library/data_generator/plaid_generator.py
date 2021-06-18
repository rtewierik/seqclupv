"""
    This module contains a class that is responsible for generating PLAID data that are passed to the
    'SeqClu' algorithm.

    Link to the 'PLAID' data set
    http://www.timeseriesclassification.com/description.php?Dataset=PLAID
"""

import os
from typing import List, Union

from numpy import ndarray

from seqclupv.library.data_generator.time_series_classification_base import TimeSeriesClassificationBase


class PLAIDGenerator(TimeSeriesClassificationBase):

    # CONSTRUCTOR #

    def __init__(self, numPrototypes: int, computeDistances: bool) -> None:
        """
            This method initializes the data generator given the number of prototypes and a boolean value indicating
            whether or not the pair-wise distances between all items in the data set need to be computed. This
            data generator is applicable to the 'GesturePebbleZ1' data set.

            :param numPrototypes: The number of prototypes that will be used in the 'SeqClu' algorithm.
            :param computeDistances: A boolean value indicating whether or not the pair-wise distances between all
            items in the data set.
        """
        super().__init__(numPrototypes, computeDistances)

    # PUBLIC METHODS #

    def generateData(self) -> List[Union[ndarray, list]]:
        """
            This method generates a data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.

            :return: A data set that is used in the 'SeqClu' algorithm or one of its extensions as
            a list of sequences.
        """
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data/PLAID")
        data, labels = PLAIDGenerator.loadData(path, ["PLAID_TRAIN.ts"])
        resultData, resultLabels = self._generateData(data, labels, ['1', '7', '8', '9', '10'])
        return resultData
