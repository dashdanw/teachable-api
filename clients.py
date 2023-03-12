import logging
import requests

from serializers import BaseResponseModel
from serializers import CoursesResponse
from serializers import EnrollmentsResponse
from serializers import UsersResponse

logger = logging.getLogger()


class TeachableAPIClient(object):
    DEFAULT_API_KEY = '7JbSA3ep6XOMV3t8t7QXuXq9HS79Dwnr'
    BASE_URL = 'https://developers.teachable.com/v1/'

    COURSES_PATH = 'courses'
    USERS_PATH = 'users'

    def __init__(self, api_key=None):
        self.api_key = api_key or self.DEFAULT_API_KEY

    def list_users(self, params:dict=None, *args, **kwargs):
        users_generator = self.list_by_page(path='users', response_serializer=UsersResponse, params=params, *args, **kwargs)
        for users_page in users_generator:
            for user in users_page.users:
                yield user

    def list_enrollments(self, course_id:int, params:dict=None, *args, **kwargs):
        enrollments_page_generator = self.list_by_page(path=f'courses/{course_id}/enrollments', response_serializer=EnrollmentsResponse, params=params, *args, **kwargs)
        for enrollments_page in enrollments_page_generator:
            for enrollment in enrollments_page.enrollments:
                yield enrollment

    def list_published_courses(self, params:dict=None, *args, **kwargs):
        params = params or {}
        params['is_published'] = 1
        for course in self.list_courses(params=params, *args, **kwargs):
            yield course

    def list_courses(self, params:dict=None, *args, **kwargs):
        courses_page_generator = self.list_by_page(path='courses', response_serializer=CoursesResponse, params=params, *args, **kwargs)
        for courses_page in courses_page_generator:
            for course in courses_page.courses:
                yield course

    def list_by_page(self, path:str, response_serializer:BaseResponseModel, params:dict=None, *args, **kwargs):
        params = params or {}
        # get page index from the defined parameters or set it to the first page index
        page_index = params.get('page_index', 1)

        while True:
            params['page_index'] = page_index
            current_page_response = self.get(path=path, params=params, *args, **kwargs)
            current_page = response_serializer.parse_obj(current_page_response.json())

            # this function will yield a generator, so that we can loop the function via a for..in..
            yield current_page

            # break at the end to simulate a do->while, since we need data from the response for control flow
            logging.debug(f'current page: {page_index}\nnumber of pages: {current_page.meta.number_of_pages}')
            if page_index >= current_page.meta.number_of_pages:
                break
            else:
                page_index += 1

    def get(self, path, *args, **kwargs):
        return self.request(method='GET', path=path, *args, **kwargs)

    def request(self, path, *args, **kwargs):
        url = f'{self.BASE_URL}/{path}'
        headers = kwargs.get('headers', {})
        headers['apiKey'] = self.api_key
        kwargs['headers'] = headers
        return requests.request(url=url, *args, **kwargs)