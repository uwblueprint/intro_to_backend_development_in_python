```py
# import and create db
from app import db
db.create_all()

from models import BlogPost

# Create BlogPost object
post1 = BlogPost(title="great new post", body="great new content")

# Add and commit created BlogPost to session
db.session.add(post1)
db.session.commit()

# Query BlogPost in db
allPosts = BlogPost.query.all()
allPosts[0]

# Add more posts
post2 = BlogPost(title="another post", body="back at it")
db.session.add(post2)
db.session.commit()

BlogPost.query.all()
```