from mock import patch

@patch("application.get_random_person")
def test_new_person(mock_get_rand_person):
    # arrange
    user = {'people_seen': []}
    expected_person = 'Katie'
    mock_get_rand_person.return_value = 'Katie'
    
    # action
    actual_person = get_next_person(user)
    
    assert_equals(actual_person, expected_person)
