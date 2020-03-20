import React, { Fragment } from 'react';
import { Switch, Route, Redirect } from 'react-router-dom';
import Subscribe from './Subscribe';
import './RoutingComponent.css';
import Stats from './Stats';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';

function Home() {
    return (
        <Fragment>
            <h1 className = "title">Coronavirus Updates</h1>
            <Subscribe></Subscribe>
            <h5><Link to='/stats' className = "go_to_stats">Click here if you want to view the current statistics of Coronavirus in your country</Link></h5>
        </Fragment>
    );
}

function RoutingComponent() {
    return (
        <Switch>
            <Route exact path = '/home' component={Home} />
            <Redirect exact from = '/' to = '/home' />
            <Route exact path ='/stats' component={Stats} />
        </Switch>
    );
}

export default RoutingComponent;