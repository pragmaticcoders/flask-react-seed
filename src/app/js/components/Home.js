import React, {Component} from 'react';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import * as HomeActions from '../actions/HomeActions';
import * as ApiActions from '../actions/ApiActions';
import styles from '../../css/app.css';

class Home extends Component {
  componentDidMount() {
    const actions = this.getActions(ApiActions);
    actions.fetchAbout();
  }
  getActions(actions) {
    const {dispatch} = this.props;
    return bindActionCreators(actions, dispatch);
  }
  render() {
    const {title, version, dispatch} = this.props;
    const actions = this.getActions(HomeActions);
    return (
      <main>
        <h1 className={styles.text}>Welcome {title}!</h1>
        <p>Version: {version}</p>
        <button onClick={e => actions.changeTitle(prompt())}>
          Update Title
        </button>
      </main>
    );
  }
}

export default connect(state => {
  let props = {title: state.getIn(['Sample', 'title']),
               version: state.getIn(['About', 'message', 'version'], '...')};
  return props;
})(Home);
