import requests


class API:
    def __init__(self, pexels_session: str):
        self.pexels_session = pexels_session  # _pexels_session cookie
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.pexels.com',
            # 'Referer': media_url,  # set in add_media_to_collection
            'Secret-Key': 'H2jk9uKnhRmL6WPwh89zBezWvr',
        }

        self.session = requests.Session()
        self.session.headers.update(headers)
        self.session.cookies.set('_pexels_session', pexels_session, domain='www.pexels.com')

    def add_media_to_collection(self, media_url: str, collection_id: str):
        media_id = self.__get_media_id(media_url)

        self.session.headers['Referer'] = media_url
        r = self.session.post(f'https://www.pexels.com/en-us/api/v2/collections/{collection_id}/photos?photo_id={media_id}')

        if r.status_code == 201:
            print(f'Media added to collection successfully, url: {media_url}')
        elif r.status_code == 422\
                and r.json()['error_messages'] == ['Validation failed: Medium has already been taken']:
            raise ValueError(f'Media already in collection, url: {media_url}')
        else:
            print(r.status_code)
            print(r.text)
            raise Exception(f'Error adding media to collection, url: {media_url}')

    def __get_media_id(self, media_url: str):
        return media_url[:-1].split('-')[-1]
