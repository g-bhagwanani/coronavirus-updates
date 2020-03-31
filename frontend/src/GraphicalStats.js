import React, { Component } from 'react';
import PieChart from './PieChart';
import { Row, Col } from 'reactstrap';
import StackedColChart from './StackedColChart';
import './GraphicalStats.css';

class GraphicalStats extends Component {

    constructor(props) {
        super(props);
    }

    render () {
        return (
            <>
            <Row className="graph_row">
                <Col>
                    <PieChart country={this.props.country} />
                </Col>
            </Row>
            <Row className="graph_row">
                <Col>
                    <StackedColChart country={this.props.country} />
                </Col>
                {/* <Col xs="12" sm="6">
                    xxx
                </Col> */}
            </Row>
            </>
        );
    }
}

export default GraphicalStats;