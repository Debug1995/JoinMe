import unittest

# The class we want to test
from Model.EventModel import EventModel as EventModel
from Model.UserModel import UserModel as UserModel
import Controller.EventController as EventController
import Controller.UserController as UserController


class Test(unittest.TestCase):
    date = '2018-12-01'
    event_1 = EventModel(1, 'event_title_1', 'tags_1', 'description_1', 'image_1', [], [], date, 'location_1', '5')
    user_1 = UserModel(1, 'real_name_1', 'nickname_1', 'gender_1', 'email_1', 'location_1', 'tags_1', 'description_1',
                       [], [], 'image_1', 'googleid_1')
    user_2 = UserModel(2, 'real_name_2', 'nickname_2', 'gender_2', 'email_2', 'location_2', 'tags_2', 'description_2',
                       [], [], 'image_2', 'googleid_2')

    # test event model
    def test_add_event(self):
        invalid_date = '2018.12.31'
        invalid_event_1 = EventModel(1, 'event_title_1', 'tags_1', 'description_1', 'image_1', [], [], invalid_date,
                                     'location_1', '5')
        event_id_1 = EventController.add_event(self.user_1, self.event_1)

        self.assertIsNotNone(event_id_1)
        self.assertIsNotNone(EventController.add_event(invalid_event_1))
    
    # def test_retrieve_event(self):
    # #     # UserController.delete_user('nickname_1', 'email_1')
    # #     # UserController.add_user(self.user_1)
    # #     # user_2 = UserController.retrieve_user('email', 'email_1')

    # #     # event_id = EventController.add_event(self.user_2, self.event_1)
    # #     # self.event_1.eventid = event_id
    # #     # EventController.host_event(user_2, self.event_1)

    #     event_2 = EventController.retrieve_event('1')
    #     self.assertIsInstance(event_2, EventModel)
    #     self.assertEqual(EventController.retrieve_event('-1'), 'MISSING')

    #     # UserController.delete_user('nickname_1', 'email_1')

    # def test_edit_event(self):
    #     event_id = EventController.add_event(self.event_1)
    #     event_2 = EventModel(1, 'event_title_2', 'tags_2', 'description_2', 'image_2', [], [], self.date, 'location_2', 'address_2', '5')
    #     event_2.image = 'image_3'
    #     self.assertEqual(EventController.edit_event(event_2), 'SUCCESS')
    #     event_2.image = 'image_2'
    #     self.assertEqual(EventController.edit_event(event_2), 'SUCCESS')        
    #     self.assertEqual(EventController.edit_event(event_2), 'MISSING')

    
#     def test_expire:
        
#     def test_remove_user:
        
#     def test_join_event:
    
    # def test_host_event(self):
    #     UserController.add_user(self.user_1)
    #     user_2 = UserController.retrieve_user('email', 'email_1')

    #     event_id = EventController.add_event(self.user_1, self.event_1)
    #     self.event_1.eventid = event_id

    #     self.assertIsNotNone(EventController.host_event(user_2, self.event_1))

    #     UserController.delete_user('nickname_1', 'email_1')
    
#     def test_hosted_event:
        
#     def test_get_hosted_event:
        
    # test user model
    def test_add_user(self):
        UserController.delete_user('nickname_2', 'email_2')
        self.assertEqual(UserController.add_user(self.user_2), 'SUCCESS')
        self.assertEqual(UserController.add_user(self.user_2), 'DUPLICATE')
        UserController.delete_user('nickname_2', 'email_2')
        
    def test_delete_user(self):
        UserController.add_user(self.user_2)
        self.assertEqual(UserController.delete_user('nickname_2', 'email_2'), 'SUCCESS')
        self.assertEqual(UserController.delete_user('fake_nickname_1', 'fake_email_1'), 'SUCCESS')
        
    def test_edit_user_1(self):
        UserController.delete_user('nickname_3', 'email_2')
        UserController.delete_user('nickname_2', 'email_2')
        UserController.add_user(self.user_2)
        user_3 = UserController.retrieve_user('email', 'email_2')
        user_3.nickname = 'nickname_3'
        self.assertIsNot(UserController.edit_user(user_3), 'MISSING' or 'DUPLICATE' or 'FAILURE')
        self.assertEqual(UserController.edit_user(user_3), 'MISSING')
        self.assertEqual(UserController.retrieve_user('email', 'email_2').nickname, 'nickname_3')
        UserController.delete_user('nickname_3', 'email_2')

    def test_edit_user_2(self):
        UserController.delete_user('nickname_3', 'email_2')
        UserController.delete_user('nickname_2', 'email_2')
        UserController.add_user(self.user_2)
        user_3 = UserController.retrieve_user('email', 'email_2')
        user_3.location = 'location_3'
        self.assertIsNot(UserController.edit_user(user_3), 'MISSING' or 'DUPLICATE' or 'FAILURE')
        self.assertEqual(UserController.edit_user(user_3), 'MISSING')
        self.assertEqual(UserController.retrieve_user('email', 'email_2').location, 'location_3')
        UserController.delete_user('nickname_3', 'email_2')
        
    def test_retrieve_user(self):
        UserController.delete_user('nickname_1', 'email_1')
        UserController.delete_user('nickname_2', 'email_2')
        UserController.add_user(self.user_1)
        self.assertIsInstance(UserController.retrieve_user('email', 'email_1'), UserModel)
        self.assertEqual(UserController.retrieve_user('email', 'email_2'), 'MISSING')
        UserController.delete_user('nickname_1', 'email_1')


if __name__ == '__main__':
    print(1)
    log_file = 'report/unittest_log.txt'
    f = open(log_file, 'a')
    suite = unittest.TestSuite()
    tests = [Test("test_add_event"), 
             Test("test_add_user"), Test("test_delete_user"), 
             Test("test_edit_user_1"), Test("test_edit_user_2"), 
             Test("test_retrieve_user")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(f)
    runner.run(suite)
    f.close()
    print(2)
    # unittest.main(testRunner=runner)

    # unittest.main()

