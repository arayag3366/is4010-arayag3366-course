# test_lab04.py
import pytest
from lab04 import find_common_elements, find_user_by_name, get_list_of_even_numbers


# Tests for find_common_elements
def test_find_common_elements_with_common_items():
    """Test finding common elements when they exist."""
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    # The order does not matter, so we compare sets
    assert set(find_common_elements(l1, l2)) == {4, 5}


def test_find_common_elements_with_no_common_items():
    """Test finding common elements when none exist."""
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    assert find_common_elements(l1, l2) == []


def test_find_common_elements_with_empty_lists():
    """Test finding common elements with empty lists."""
    assert find_common_elements([], []) == []
    assert find_common_elements([1, 2, 3], []) == []


def test_find_common_elements_with_duplicates():
    """Test finding common elements with duplicates in lists."""
    l1 = [1, 1, 2, 3, 3]
    l2 = [1, 2, 2, 4, 5]
    result = find_common_elements(l1, l2)
    # Should contain 1 and 2, order doesn't matter
    assert set(result) == {1, 2}


# Tests for find_user_by_name
@pytest.fixture
def sample_users():
    """Fixture providing sample user data for testing."""
    return [
        {"name": "alice", "age": 30, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "email": "bob@example.com"},
        {"name": "charlie", "age": 35, "email": "charlie@example.com"},
    ]


def test_find_user_by_name_existing(sample_users):
    """Test finding a user that exists."""
    assert find_user_by_name(sample_users, "alice") == {
        "name": "alice",
        "age": 30,
        "email": "alice@example.com",
    }


def test_find_user_by_name_not_existing(sample_users):
    """Test searching for a user that doesn't exist."""
    assert find_user_by_name(sample_users, "david") is None


def test_find_user_by_name_empty_list():
    """Test searching in an empty user list."""
    assert find_user_by_name([], "alice") is None


def test_find_user_by_name_case_sensitivity(sample_users):
    """Test that user search is case-sensitive."""
    assert find_user_by_name(sample_users, "Alice") is None  # Capital A
    assert find_user_by_name(sample_users, "alice") is not None  # lowercase a


# Tests for get_list_of_even_numbers
def test_get_list_of_even_numbers_mixed():
    """Test filtering even numbers from a mixed list."""
    assert get_list_of_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_get_list_of_even_numbers_all_odd():
    """Test filtering even numbers from a list of all odd numbers."""
    assert get_list_of_even_numbers([1, 3, 5, 7]) == []


def test_get_list_of_even_numbers_all_even():
    """Test filtering even numbers from a list of all even numbers."""
    assert get_list_of_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_get_list_of_even_numbers_empty():
    """Test filtering even numbers from an empty list."""
    assert get_list_of_even_numbers([]) == []


def test_get_list_of_even_numbers_with_zero():
    """Test that zero is correctly identified as even."""
    assert get_list_of_even_numbers([0, 1, 2, 3]) == [0, 2]


def test_get_list_of_even_numbers_preserves_order():
    """Test that the order of even numbers is preserved."""
    assert get_list_of_even_numbers([10, 1, 8, 3, 6, 5, 4]) == [10, 8, 6, 4]


def test_get_list_of_even_numbers_negative():
    """Test filtering even numbers including negative numbers."""
    assert get_list_of_even_numbers([-4, -3, -2, -1, 0, 1, 2]) == [-4, -2, 0, 2]