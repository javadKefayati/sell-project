from django.test import TestCase
from account.models import User , Account
from transaction.models import Order , Increase_balance



class OrderTestCase(TestCase):
      
      def setUp(self):
            User.objects.regiter_user(email="u1@gmail.com",username="u1", password="u1" ,balance = 30000)
            
            User.objects.regiter_user(email="u2@gmail.com",username="u2", password="u2",balance = 100000 )
            
            User.objects.regiter_user(email="u3@gmail.com",username="u3", password="u3",balance = 53658.487  )

      
      def test_increase_balance_account_user(self):
           
            status , message , balance = Increase_balance.objects.register_increase("u1",500)
            self.assertEqual(balance, 30500)
            status , message , balance = Increase_balance.objects.register_increase("u1",15000)
            self.assertEqual(balance, 45500)
            status , message , balance = Increase_balance.objects.register_increase("u1",10.5)
            self.assertEqual(balance, 45510.5)
            status , message , balance = Increase_balance.objects.register_increase("u1",20.398)
            self.assertEqual(balance, 45530.898)

            status , message , balance = Increase_balance.objects.register_increase("u2",19000)
            self.assertEqual(balance, 119000)
            status , message , balance = Increase_balance.objects.register_increase("u2",500)
            self.assertEqual(balance, 119500)

            status , message , balance = Increase_balance.objects.register_increase("u3",1000)
            self.assertEqual(balance, 54658.487)
            status , message , balance = Increase_balance.objects.register_increase("u3",36.98857)
            self.assertEqual(balance, 54695.47557)

            