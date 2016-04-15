import * as ActionTypes from '../constants/ActionTypes';
import { createReducer } from 'redux-immutablejs';
import {Map} from 'immutable';

let defaultState = Map({
  title: 'Home'
});


export default createReducer(defaultState, {
  [ActionTypes.TITLE_CHANGED]: (state, action) => state.merge({
    title: action.text
  })
});
