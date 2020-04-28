#import pytest
from data_structures_and_algorithms import __version__
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverseArray
from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray
from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch

#@pytest.mark.parametrize("test_input1","test_input2","expected",[([1,2,3,4],4,3),([1,2,3,4],3,2)])

# def test_array_binary_search_test(test_input1,test_input2,expected):
#     assert BinarySearch(test_input1,test_input2) == expected


def test_version():
    assert __version__ == '0.1.0'

def test_array_shift_one():
    assert insertShiftArray([2,4,6,8],5) == [2,4,5,6,8]

def test_array_shift_two():
    assert insertShiftArray([2,4,6,8,10],99) == [2,4,6,99,8,10]

def test_array_shift_three():
    assert insertShiftArray([2,4,6,8,10,14],99) == [2,4,6,99,8,10,14]

def test_array_shift_four():
    assert insertShiftArray([2,4,6,8,10,14,16],99) == [2,4,6,8,99,10,14,16]

def test_array_reverse_one():
    assert reverseArray([1,2,3,4]) == [4,3,2,1]

def test_array_reverse_two():
    assert reverseArray([5,6,7,8]) == [8,7,6,5]

def test_array_reverse_three():
    assert reverseArray([100,135,80,200]) == [200,80,135,100]

def test_array_reverse_four():
    assert reverseArray([-987,9877,-843343,400]) == [400,-843343,9877,-987]

def test_array_binary_search_one():
    assert BinarySearch([1,2,3,4],4) == 3

def test_array_binary_search_two():
    assert BinarySearch([1,2,3,4],3) == 2

def test_array_binary_search_three():
    assert BinarySearch([1,2,3,4],2) == 1

def test_array_binary_search_four():
    assert BinarySearch([1,2,3,4],1) == 0

def test_array_binary_search_five():
    assert BinarySearch([1,2,3,4],99) == -1

def test_array_binary_search_six():
    assert BinarySearch([1,2,3,4],-33) == -1

def test_array_binary_search_seven():
    assert BinarySearch([1,2,3,4,5],4) == 3

def test_array_binary_search_eight():
    assert BinarySearch([1,2,3,4,5],5) == 4

def test_array_binary_search_nine():
    assert BinarySearch([1,2,3,4,5],3) == 2

def test_array_binary_search_ten():
    assert BinarySearch([1,2,3,4,5],2) == 1

def test_array_binary_search_11():
    assert BinarySearch([1,2,3,4,5],1) == 0

def test_array_binary_search_12():
    assert BinarySearch([1,2,3,4,5],99) == -1

def test_array_binary_search_13():
    assert BinarySearch([1,2,3,4,5],-12) == -1