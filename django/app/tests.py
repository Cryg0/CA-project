
from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Post,Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        test_category = Category.objects.create(name='django')
        testUser1 = User.objects.create(username='test',password='test123')

        post1= Post.objects.create(category_id=1,title='Django',content='Django is great',\
            slug='post-title',author_id=1,status='published')


    def test_app_content(self):
        post= Post.postObjects.get(id=1)
        cat= Category.objects.get(id=1)
        author=post.author
        title=post.title
        content=post.content
        status=post.status

        self.assertEqual(author.username,'test')
        self.assertEqual(title,'Django')
        self.assertEqual(content,'Django is great')
        self.assertEqual(status,'published')
        self.assertEqual(str(post),'Django')
        self.assertEqual(str(cat),'django')
        

 
