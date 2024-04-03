"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from requests_toolbelt.utils import dump

logger = get_logger('cloudflare-waf')


class CloudFlareWAF(object):

    def __init__(self, config):
        self.server_url = config.get('server_url').strip()
        self.api_key = config.get('api_key')
        self.headers = {'Authorization':'Bearer {}'.format(self.api_key)}
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url

    def make_api_call(self, endpoint=None, method='GET', params=None, headers=None, data=None):
        service_endpoint = f'{self.server_url}{endpoint}'
        logger.debug('REST API Service URL: {0}'.format(service_endpoint))
        if headers:
            self.headers.update(headers)
        try:
            response = requests.request(method, service_endpoint, headers=self.headers, params=params, json=data)
            logger.debug('\n{}\n'.format(dump.dump_all(response).decode('utf-8')))
            logger.error('REST API Response Status Code: {0}'.format(response.status_code))
            logger.error('REST API Response: {0}'.format(response.text))
            if response.ok:
                return response.json()
            else:
                raise ConnectorError(response.text)
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError(
                'The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def remove_empty_value(params):
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    return params


def build_rule_payload(params):
    filter_dict = {}
    params['action'] = params.pop('action', '').lower().replace(' ', '_')
    params = remove_empty_value(params)
    filter_id = params.pop('filter_id', '')
    filter_expression = params.pop('filter_id', '')
    if filter_id:
        filter_dict.update({'id': filter_id})
    if filter_expression:
        filter_dict.update({'expression': filter_expression})
    if filter_dict:
        params.update({'filter': filter_dict})
    return params


def create_firewall_rule(config, params):
    waf = CloudFlareWAF(config)
    params = build_rule_payload(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/firewall/rules'
    return waf.make_api_call(endpoint, 'POST', data=[params])


def update_firewall_rule(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    params = build_rule_payload(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/firewall/rules'
    return waf.make_api_call(endpoint, 'PUT', data=[params])


def list_firewall_rules(config, params):
    waf = CloudFlareWAF(config)
    params['action'] = params.pop('action', '').lower().replace(' ', '_')
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/firewall/rules'
    return waf.make_api_call(endpoint, 'GET', params=params)


def delete_firewall_rule(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/firewall/rules'
    return waf.make_api_call(endpoint, 'DELETE', params=params)


def list_filters(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/firewall/filters'
    return waf.make_api_call(endpoint, 'GET', params=params)


def create_filter(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/filters'
    return waf.make_api_call(endpoint, 'POST', data=[params])


def update_filter(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/filters'
    return waf.make_api_call(endpoint, 'PUT', data=[params])


def delete_filter(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    zone_id = config.get('zone_id')
    endpoint = f'/client/v4/zones/{zone_id}/filters'
    return waf.make_api_call(endpoint, 'DELETE', params=params)


def list_zones(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    endpoint = f'/client/v4/zones'
    return waf.make_api_call(endpoint, 'GET', params=params)


def get_ip_lists(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    account_id = config.get('account_id', '')
    endpoint = f'/client/v4/accounts/{account_id}/rules/lists'
    return waf.make_api_call(endpoint, 'GET', params=params)


def create_ip_list(config, params):
    waf = CloudFlareWAF(config)
    params['kind'] = 'ip'
    params = remove_empty_value(params)
    account_id = config.get('account_id', '')
    endpoint = f'/client/v4/accounts/{account_id}/rules/lists'
    return waf.make_api_call(endpoint, 'POST', data=params)


def delete_ip_list(config, params):
    waf = CloudFlareWAF(config)
    params = remove_empty_value(params)
    account_id = config.get('account_id', '')
    list_id = params.pop('list_id', '')
    endpoint = f'/client/v4/accounts/{account_id}/rules/lists/{list_id}'
    return waf.make_api_call(endpoint, 'DELETE', data=params)

def _check_health(config):
    return list_zones(config, params={})

operations = {
    'create_firewall_rule': create_firewall_rule,
    'update_firewall_rule': update_firewall_rule,
    'list_firewall_rules': list_firewall_rules,
    'delete_firewall_rule': delete_firewall_rule,
    'list_filters': list_filters,
    'create_filter': create_filter,
    'update_filter': update_filter,
    'delete_filter': delete_filter,
    'list_zones': list_zones,
    'get_ip_lists': get_ip_lists,
    'create_ip_list': create_ip_list,
    'delete_ip_list': delete_ip_list
}
