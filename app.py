from flask import (
  Flask,
  render_template,
  request,
  redirect,
  flash,
)
app = Flask(__name__)


@app.route('/')
def index():
  # get posts from database
  return render_template('index.html', posts=posts)

@app.route('/blogpost', methods=['POST'])
@app.route('/blogpost/<id>', methods=['GET'])
def blogpost(id=None):
  if request.method == 'GET' and id is not None:
    # get post with id from database
    return render_template('blogpost.html', post=posts[int(id)])
  elif request.method == 'POST':
    # write form data to database
    print(request.form)
    return redirect('/')

@app.route('/newpost')
def newpost():
  return render_template('newpost.html')


posts = [
  {
    'id': 0,
    'title': 'What\'s poppin\'?',
    'body': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
    'date': 'March 4, 2018',
  },
  {
    'id': 1,
    'title': 'Top 10 Taylor Swift Albums',
    'body': '1. Fearless\n2. 1989\n3. Red\n4. Speak Now\n5. Taylor Swift',
    'date': 'March 8, 2018',
  },
  {
    'id': 2,
    'title': 'Dogs vs Cats',
    'body': 'Dog dog dog cat cat cat',
    'date': 'March 11, 2018',
  },
]