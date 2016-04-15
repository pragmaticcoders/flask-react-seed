import * as ActionTypes from '../constants/ActionTypes';
import { createReducer } from 'redux-immutablejs';
import {Map} from 'immutable';

let defaultState = Map({
  fetching: false
});


export default createReducer(defaultState, {
  [ActionTypes.ABOUT_RECIVED]: (state, action) => state.merge(action.data),
  [ActionTypes.ABOUT_REQUESTED]: (state, action) => state.merge({
    fetching: true
  })
});
