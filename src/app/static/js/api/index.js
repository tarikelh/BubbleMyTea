import { fetchData } from './fetch.js';

export const get = ({ url, headers = {} }) => fetchData({ endpoint: url, init: { headers, method: 'GET' } });

export const post = ({ url, data, headers = {} }) => fetchData({ endpoint: url, init: { headers, method: 'POST', body: data } });

export const put = ({ url, data, headers = {} }) => fetchData({ endpoint: url, init: { headers, method: 'PUT', body: data } });

export const del = ({ url, headers = {} }) => fetchData({ endpoint: url, init: { headers, method: 'DELETE' } });
