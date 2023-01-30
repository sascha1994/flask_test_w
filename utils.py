import json


def load_candidates_from_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        profile = json.load(file)
        candidates = {}
        for i in profile:
            candidates[i['id']] = i
        return profile


def get_candidate(candidate_id):
    for i in load_candidates_from_json():
        if candidate_id == i['id']:
            return i


def get_candidates_by_name(candidate_name):
    names = []
    for name in load_candidates_from_json():
        candidate_names = name['name'].split()
        candidate_names = [x.lower() for x in candidate_names]
        if candidate_name in candidate_names:
            names.append(name)
    return names


def get_candidates_by_skill(skill_name):
    skills = []
    for candidate in load_candidates_from_json():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill_name in candidate_skills:
            skills.append(candidate)
    return skills

print(get_candidates_by_name('adela'))