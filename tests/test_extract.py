import extract

vacancies = extract.parse_vacancies("jobicy_like.json")

def test_all_vacancies():
    result = extract.extraction(vacancies)
    assert [ids["id"] for ids in result] == [155316, 155317, 155318, 155319, 155320, 155321, 155322, 155323, 155324, 155325]
    
def test_empty():
    result = extract.extraction([])
    assert result == []