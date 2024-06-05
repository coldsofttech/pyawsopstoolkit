import unittest
from datetime import datetime

from pyawsopstoolkit.models.ec2.network_interface import Attachment


class TestAttachment(unittest.TestCase):
    """Unit test cases for Attachment."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'id': 'eni-attach-0123456789abcdef0',
            'device_index': 1,
            'status': 'attached',
            'delete_on_termination': True,
            'attach_time': datetime(2023, 5, 19),
            'network_card_index': 0,
            'instance_id': 'i-0123456789abcdef0',
            'instance_owner_id': '123456789012'
        }
        self.attachment = self.create_attachment()
        self.attachment_with_termination = self.create_attachment(
            delete_on_termination=self.params['delete_on_termination']
        )
        self.attachment_with_time = self.create_attachment(attach_time=self.params['attach_time'])
        self.attachment_with_network_index = self.create_attachment(
            network_card_index=self.params['network_card_index']
        )
        self.attachment_with_instance_id = self.create_attachment(instance_id=self.params['instance_id'])
        self.attachment_with_instance_owner = self.create_attachment(instance_owner_id=self.params['instance_owner_id'])
        self.attachment_full = self.create_attachment(
            delete_on_termination=self.params['delete_on_termination'],
            attach_time=self.params['attach_time'],
            network_card_index=self.params['network_card_index'],
            instance_id=self.params['instance_id'],
            instance_owner_id=self.params['instance_owner_id']
        )

    def create_attachment(self, **kwargs):
        return Attachment(
            id=self.params['id'],
            device_index=self.params['device_index'],
            status=self.params['status'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.attachment.id, self.params['id'])
        self.assertEqual(self.attachment.device_index, self.params['device_index'])
        self.assertEqual(self.attachment.status, self.params['status'])
        self.assertFalse(self.attachment.delete_on_termination)
        self.assertIsNone(self.attachment.attach_time)
        self.assertIsNone(self.attachment.network_card_index)
        self.assertIsNone(self.attachment.instance_id)
        self.assertIsNone(self.attachment.instance_owner_id)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.attachment_with_termination, self.params['delete_on_termination'], None, None, None, None),
            (self.attachment_with_time, False, self.params['attach_time'], None, None, None),
            (self.attachment_with_network_index, False, None, self.params['network_card_index'], None, None),
            (self.attachment_with_instance_id, False, None, None, self.params['instance_id'], None),
            (self.attachment_with_instance_owner, False, None, None, None, self.params['instance_owner_id']),
            (
                self.attachment_full,
                self.params['delete_on_termination'],
                self.params['attach_time'],
                self.params['network_card_index'],
                self.params['instance_id'],
                self.params['instance_owner_id']
            ),
        ]
        for attachment, del_termination, attach_time, network_card_index, instance_id, instance_owner_id in test_cases:
            with self.subTest(attachment=attachment):
                self.assertEqual(attachment.id, self.params['id'])
                self.assertEqual(attachment.device_index, self.params['device_index'])
                self.assertEqual(attachment.status, self.params['status'])
                self.assertEqual(attachment.delete_on_termination, del_termination)
                self.assertEqual(attachment.attach_time, attach_time)
                self.assertEqual(attachment.network_card_index, network_card_index)
                self.assertEqual(attachment.instance_id, instance_id)
                self.assertEqual(attachment.instance_owner_id, instance_owner_id)

    def test_setters(self):
        new_params = {
            'id': 'eni-attach-0123456789abcdef1',
            'device_index': 2,
            'status': 'detached',
            'delete_on_termination': False,
            'attach_time': datetime.today(),
            'network_card_index': 1,
            'instance_id': 'i-0123456789abcdef1',
            'instance_owner_id': '987654321012'
        }

        self.attachment_full.id = new_params['id']
        self.attachment_full.device_index = new_params['device_index']
        self.attachment_full.status = new_params['status']
        self.attachment_full.delete_on_termination = new_params['delete_on_termination']
        self.attachment_full.attach_time = new_params['attach_time']
        self.attachment_full.network_card_index = new_params['network_card_index']
        self.attachment_full.instance_id = new_params['instance_id']
        self.attachment_full.instance_owner_id = new_params['instance_owner_id']

        self.assertEqual(self.attachment_full.id, new_params['id'])
        self.assertEqual(self.attachment_full.device_index, new_params['device_index'])
        self.assertEqual(self.attachment_full.status, new_params['status'])
        self.assertEqual(self.attachment_full.delete_on_termination, new_params['delete_on_termination'])
        self.assertEqual(self.attachment_full.attach_time, new_params['attach_time'])
        self.assertEqual(self.attachment_full.network_card_index, new_params['network_card_index'])
        self.assertEqual(self.attachment_full.instance_id, new_params['instance_id'])
        self.assertEqual(self.attachment_full.instance_owner_id, new_params['instance_owner_id'])

    def test_invalid_types(self):
        invalid_params = {
            'id': 123,
            'device_index': 'dev-0',
            'status': 123,
            'delete_on_termination': 'False',
            'attach_time': '2024-02-06',
            'network_card_index': 'ncard-0',
            'instance_id': 123,
            'instance_owner_id': 123
        }

        with self.assertRaises(TypeError):
            Attachment(
                id=invalid_params['id'],
                device_index=self.params['device_index'],
                status=self.params['status'],
            )
        with self.assertRaises(TypeError):
            Attachment(
                id=self.params['id'],
                device_index=invalid_params['device_index'],
                status=self.params['status'],
            )
        with self.assertRaises(TypeError):
            Attachment(
                id=self.params['id'],
                device_index=self.params['device_index'],
                status=invalid_params['status'],
            )
        with self.assertRaises(TypeError):
            self.create_attachment(delete_on_termination=invalid_params['delete_on_termination'])
        with self.assertRaises(TypeError):
            self.create_attachment(attach_time=invalid_params['attach_time'])
        with self.assertRaises(TypeError):
            self.create_attachment(network_card_index=invalid_params['network_card_index'])
        with self.assertRaises(TypeError):
            self.create_attachment(instance_id=invalid_params['instance_id'])
        with self.assertRaises(TypeError):
            self.create_attachment(instance_owner_id=invalid_params['instance_owner_id'])

        with self.assertRaises(TypeError):
            self.attachment_full.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.attachment_full.device_index = invalid_params['device_index']
        with self.assertRaises(TypeError):
            self.attachment_full.status = invalid_params['status']
        with self.assertRaises(TypeError):
            self.attachment_full.delete_on_termination = invalid_params['delete_on_termination']
        with self.assertRaises(TypeError):
            self.attachment_full.attach_time = invalid_params['attach_time']
        with self.assertRaises(TypeError):
            self.attachment_full.network_card_index = invalid_params['network_card_index']
        with self.assertRaises(TypeError):
            self.attachment_full.instance_id = invalid_params['instance_id']
        with self.assertRaises(TypeError):
            self.attachment_full.instance_owner_id = invalid_params['instance_owner_id']

    def test_to_dict(self):
        expected_dict = {
            "id": self.params['id'],
            "device_index": self.params['device_index'],
            "status": self.params['status'],
            "delete_on_termination": self.params['delete_on_termination'],
            "attach_time": self.params['attach_time'].isoformat(),
            "network_card_index": self.params['network_card_index'],
            "instance_id": self.params['instance_id'],
            "instance_owner_id": self.params['instance_owner_id']
        }
        self.assertDictEqual(self.attachment_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "id": self.params['id'],
            "device_index": self.params['device_index'],
            "status": self.params['status'],
            "delete_on_termination": False,
            "attach_time": None,
            "network_card_index": None,
            "instance_id": None,
            "instance_owner_id": None
        }
        self.assertDictEqual(self.attachment.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
