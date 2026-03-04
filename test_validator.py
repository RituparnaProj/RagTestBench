from validator.similarity_validator import validate_similarity


def test_similarity_validator():

    expected = "Paris is the capital of France."
    actual = "France's capital city is Paris."

    score = validate_similarity(expected, actual)

    print(score)

    assert score > 0.7
