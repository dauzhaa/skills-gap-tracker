import json

def parse_vacancies(filename):
    with open(filename, encoding='utf-8') as f:
        vc_lst = json.load(f)
        
    return vc_lst
    
def extraction(vacancies):
    res = []
    for vacancy in vacancies:
        res.append({
            "id": vacancy["id"],
            # "url": vacancy["url"],
            # "title": vacancy["jobTitle"],
            # "description": vacancy["jobDescription"],
        })
        
    return res
 

if __name__ == '__main__':
    p = parse_vacancies('jobicy_like.json')
    f = extraction(p)
    print(f)
    