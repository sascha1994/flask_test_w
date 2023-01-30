from flask import Flask, request, render_template
import utils

app = Flask(__name__)


@app.route("/")
def page_index():
    items = utils.load_candidates_from_json()
    return render_template('list.html', items=items)


@app.route("/candidate/<int:x>")
def page_candidate(x):
    candidate = utils.get_candidate(x)
    return render_template('card.html', candidate=candidate)

@app.route("/search/<candidate_name>")
def search_candidate(candidate_name):
    candidate_names = utils.get_candidates_by_name(candidate_name)
    coat = len(candidate_names)
    return render_template('search.html', items=candidate_names, coat = coat)

@app.route("/skill/<skill_name>")
def search_skill(skill_name):
    candidate_skills = utils.get_candidates_by_skill(skill_name)
    coat = len(candidate_skills)
    return render_template('skill.html', items=candidate_skills, coat = coat)




app.run(debug=True)
