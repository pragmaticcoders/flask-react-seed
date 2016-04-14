import {about, get_data} from '../api';

import {
  ABOUT_RECIVED,
  ABOUT_REQUESTED
} from '../constants/ActionTypes';



export function reciveAbout(response) {
  return {
    type: ABOUT_RECIVED,
    data: get_data(response)
  };
}

export function requestAbout() {
  return {
    type: ABOUT_REQUESTED
  };
}



export function fetchAbout() {
  return dispatch => {
    dispatch(requestAbout());
    return about.get().then(response => {
      dispatch(reciveAbout(response));
    });
  };
}
