from django.test import TestCase
from news.models import Articles
from django.utils import timezone


class mytest(TestCase):
	title = "13 iphone fake news"
	posttext="Инновационный тандем сверхширокоугольной и широкоугольной камер позволяет превратить практически любой кадр в прекрасное фото студийного качества. Не ограничивайте свой творческий потенциал, снимайте при недостаточной освещенности и под разными ракурсами, помещайте в кадр в 4 раза больше видов и впечатлений, запечатлевайте масштабные сцены, портреты и безграничные пейзажи. "

	def create_Articles(self):
		return Articles.objects.create(title=mytest.title, post=mytest.posttext, date=timezone.now())

	def test_Articles(self):
		news = self.create_Articles()
		self.assertTrue(isinstance(news, Articles))
		self.assertEqual(mytest.title, news.title)
		self.assertEqual(mytest.posttext, news.post)