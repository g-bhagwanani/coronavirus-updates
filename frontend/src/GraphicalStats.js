import React, { Component } from 'react';
import PieChart from './PieChart';

class GraphicalStats extends Component {

    constructor(props) {
        super(props);
    }

    render () {
        return (
            <PieChart country={this.props.country} />
        );
    }
}

export default GraphicalStats;