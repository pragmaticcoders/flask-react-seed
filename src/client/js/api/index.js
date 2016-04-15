import 'whatwg-fetch';
import restful, { fetchBackend } from 'restful.js';
import Immutable from 'immutable';


export const api = restful('/api', fetchBackend(fetch));
export const about = api.custom('about');


export function get_data(response) {
  return Immutable.fromJS(response.body().data());
}


export default api;
