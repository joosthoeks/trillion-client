

import requests


class TrillionClient(object):

    def __init__(self, url='https://trillion-eindhoven.xlab.si/api/'):
        self.__url = url

    def set_credential(self, bearer_token):
        self.__bearer_token = bearer_token

    def __get_credential(self):
        headers = {
                'Authorization Bearer ': self.__bearer_token
                }
        return headers

    def __request(self, endpoint, params, method='GET', credential=False):
        full_url = '%s%s' % (self.__url, endpoint)
        if credential:
            headers = self.__get_credential()
            if method is 'GET':
                r = requests.get(full_url, params=params, headers=headers)
            if method is 'POST':
                r = requests.post(full_url, data=params)
            if method is 'PUT':
                r = requests.put(full_url, data=params)
            if method is 'DELETE':
                r = requests.delete(full_url, data=params)
        else:
                r = requests.get(full_url, params=params)
        return r.json()

    def analytics_data_analytics_list(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('analytics/data_analytics/', params)

    def analytics_data_analytics_read(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('analytics/data_analytics/%s/' % id, params)

    def auth_convert_token_create(self):
        return self.__request('auth/convert-token/', {}, 'POST', True)

    def auth_revoke_token_create(self):
        return self.__request('auth/revoke-token/', {}, 'POST', True)

    def auth_token_create(self):
        return self.__request('auth/token/', {}, 'POST', True)

    def biometrics_verify_face_create(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('biometrics/verify_face/', params, 'POST', True)

    def forms_forms_list(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/forms/', params, 'GET', True)

    def forms_forms_read(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/forms/%s/' % id, params, 'GET', True)

    def forms_tos_list(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/tos/', params, 'GET', True)

    def forms_tos_create(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/tos/', params, 'POST', True)

    def forms_tos_read(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/tos/%s/' % id, params, 'GET', True)

    def forms_tos_update(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/tos/%s/' % id, params, 'PUT', True)

    def forms_tos_partial_update(self, id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('forms/tos/%s/' % id, params, 'PATCH', True)

    def forms_tos_delete(self, id):
        return self.__request('forms/tos/%s/' % id, {}, 'DELETE', True)

    def resources_files_read(self, guid, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('resources/files/%s/' % guid, params, 'GET', True)

    def users_confirm_read(self, activation_key):
        return self.__request('users/confirm/%s/' % activation_key, {}, 'GET', True)

    def users_forgot_password_create(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('users/forgot_password/', params, 'POST', True)

    def users_is_username_available_list(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('users/is_username_available/', params, 'GET', True)

    def users_password_reset_read(self, activation_key):
        return self.__request('users/password_reset/%s/' % activation_key, {}, 'GET', True)

    def users_password_reset_create(self, activation_key):
        return self.__request('users/password_reset/%s/' % activation_key, {}, 'POST', True)

    def users_register_create(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('users/register/', params, 'POST', True)

    def users_request_access_list(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('users/request_access/', params, 'GET', True)

    def users_request_access_create(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('users/request_access/', params, 'POST', True)

