"""Bag distance measure"""

from __future__ import division
import collections

from py_stringmatching import utils
from py_stringmatching.similarity_measure.sequence_similarity_measure import \
    SequenceSimilarityMeasure

class BagDistance(SequenceSimilarityMeasure):
    def __init__(self):
        super(BagDistance, self).__init__()

    def get_raw_score(self, string1, string2):
        # input validations
        utils.sim_check_for_none(string1, string2)
        utils.sim_check_for_string_inputs(string1, string2)
        if utils.sim_check_for_exact_match(string1, string2):
            return 0

        len_str1 = len(string1)
        len_str2 = len(string2)

        if len_str1 == 0:
            return len_str2

        if len_str2 == 0:
            return len_str1

        bag1 = collections.Counter(string1)
        bag2 = collections.Counter(string2)

        size1 = sum((bag1 - bag2).values())
        size2 = sum((bag2 - bag1).values())

        # returning the max of difference of sets
        return max(size1, size2)

    def get_sim_score(self, string1, string2):
        raw_score = self.get_raw_score(string1, string2)
        string1_len = len(string1)
        string2_len = len(string2)
        if string1_len == 0 and string2_len == 0:
            return 1.0
        return 1 - (raw_score / max(string1_len, string2_len))




def distance (word1, word2):
  bd = BagDistance()
  return bd.get_raw_score(word1, word2)


