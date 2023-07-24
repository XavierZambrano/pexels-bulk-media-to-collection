import os
from unittest import TestCase
from dotenv import load_dotenv

from api import API


class TestApi(TestCase):
    def setUp(self):
        load_dotenv()
        self.pexels_session = os.getenv('PEXELS_SESSION')

    def test_api(self):
        collection_id = 'wpfmesw'
        media_url = 'https://www.pexels.com/photo/america-architecture-bay-boat-208745/'

        api = API(self.pexels_session)
        api.add_media_to_collection(media_url, collection_id)

