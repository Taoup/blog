from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blogpost

# Create your tests here.
def create_blog(id, public):
    return Blogpost.objects.create(title= id, body=id, public = public)

class TestLogin(TestCase):

    def setUp(self):
        user = User.objects.create_user('test', "", 'test')

    def testNonlogin(self):
        self.client.logout()
        create_blog('ttt', False)
        response = self.client.get('/')
        self.assertNotContains(response, 'ttt')
        create_blog('xxx', True)
        response = self.client.get('/')
        self.assertContains(response, 'xxx')

    
    def testLogin(self):
        t = self.client.login(username='test', password='test')
        self.assertTrue(t)
        create_blog('testLogin', False)
        response = self.client.get('/')
        self.assertContains(response, 'testLogin')

    def test_postDetail_while_logout(self):
        self.client.logout()
        t = create_blog('test_postDetail_while_logout', False)

        res = self.client.get(f'post/{t.id}')

        # 不存在 or 无权限访问？
        self.assertEqual(res.status_code, 404)

    def test_postDetail_logout_then_login(self):
        self.client.logout()
        t = create_blog('test_postDetail_while_logout', False)
        res = self.client.get(f'/post/{t.id}')
        # 不存在 or 无权限访问？
        self.assertEqual(res.status_code, 404)
        self.assertTrue(self.client.login(username='test', password='test'))
        res = self.client.get(f'/post/{t.id}')
        # 不存在 or 无权限访问？
        self.assertContains(res, 'test_postDetail_while_logout')
        
    def test_non_existing_tags(self):
        res = self.client.get('/list/tag/1000000')
        self.assertEqual(res.status_code, 404)

    def test_non_existing_post(self):
        res = self.client.get('/post/1000000')
        self.assertEqual(res.status_code, 404)

    def test_exstreme_numbers_of_posts(self):
        res = self.client.get('/post/100000000000000000000000')
        self.assertEqual(res.status_code, 404)

    def test_exstreme_numbers_of_tags(self):
        res = self.client.get('/list/tag/100000000000000000000000')
        self.assertEqual(res.status_code, 404)