import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_zeroArray():
    assert max_subarray_sum([0,0,0,0,0,0,0,0]) == 0

def test_alternating():
    assert max_subarray_sum([-1,1,-1,1,-1,1]) == 1

def test_random():
    assert max_subarray_sum([-1,4,5,-10,13,-2,0,5]) == 16