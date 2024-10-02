from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports.db'
db = SQLAlchemy(app)
# База данных
class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/')
def index():
    sections = Section.query.all()
    return render_template('index.html', sections=sections)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    sections = Section.query.filter(Section.name.contains(query)).all()
    if sections:
        message = f"{len(sections)} section(s) found."
    else:
        message = "No sections found."
    return render_template('index.html', sections=sections, message=message)

# Добавить данные в БД
def add_sample_data():
    sections_data = [
        {'name': 'Football', 'description': 'Players kick a ball to score points.'},
        {'name': 'Basketball', 'description': 'Players shoot a ball through a hoop to score points.'},
        {'name': 'Swimming', 'description': 'Competitors race in a pool to finish first.'},
        # Add more sections as needed
    ]

    for section_data in sections_data:
        existing_section = Section.query.filter_by(name=section_data['name']).first()
        if not existing_section:
            section = Section(name=section_data['name'], description=section_data['description'])
            db.session.add(section)

    db.session.commit()

# удалить данные из БД
def delete_sections_by_name(names):
    for name in names:
        section = Section.query.filter_by(name=name).first()
        if section:
            db.session.delete(section)

    db.session.commit()

# Пользователь может читать описание кажого вида секции

@app.route('/section/<int:section_id>')
def section_page(section_id):
    section = Section.query.get_or_404(section_id)
    return render_template('section.html', section=section)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_sample_data()
        # delete_sections_by_name(['Football', 'Basketball', "Swimming"])
    app.run(debug=True)
