from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
 {
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Chinmai, Thailand',
  'salary': 'Kyats. 700,000'
 },
 {
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Beijein, China',
  'salary': 'Kyats. 500,000'
 },
 {
  'id': 1,
  'title': 'Frontend Engineer',
  'location': 'Ohio, Frence',
  'salary': 'Kyats. 700,000'
 },
 {
  'id': 1,
  'title': 'Backend Engineer',
  'location': 'Hong Kong, China',
  'salary': 'Kyats. 700,000'
 },
]


@app.route("/")
def hello_world():
	return render_template('home.html', jobs=JOBS,)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
