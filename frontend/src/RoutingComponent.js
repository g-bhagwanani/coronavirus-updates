import React, { Fragment } from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import Subscribe from './Subscribe';
import './RoutingComponent.css';
import Stats from './Stats';

function Home({ match }) {

    var send = '';
    if(match.params.message) {
        send = match.params.message;
    }

    return (
        <Fragment>
            <h1 className = "title">Coronavirus Updates</h1>
            <Subscribe message={send}></Subscribe>
        </Fragment>
    );
}

function RoutingComponent() {
    return (
        <Switch>
            <Route path = '/home/:message' component={Home} />
            <Route path = '/home' component={Home} />
            <Redirect exact from = '/' to = '/home' />
            <Route exact path ='/stats/:country' component={Stats} />
            <Redirect exact from = '/stats' to = '/stats/world' />
            <Redirect from ='*' to = '/' />
        </Switch>
    );
}

export default RoutingComponent;