import React, { Component } from 'react';
import './Card_stats.css';
import { Card, Row, Col, CardTitle, CardText } from 'reactstrap';

class Card_stats extends Component {

    constructor(props) {
        super(props);
        this.state = {
            deets : [],
            flask_url : window.location.protocol + '//' + window.location.hostname +":5000/"
        };
    }

    componentDidMount() {

        var countryy = this.props.country;

        document.getElementsByClassName('react-autosuggest__input')[0].value = countryy[0].toUpperCase() + countryy.slice(1);

        fetch(this.state.flask_url + '/getinfo?country=' + countryy)
            .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            deets: result
                        });
                    },
                    (error) => {
                        console.log(error);
                    }
                )
    }

    componentWillReceiveProps(newProps) {

        var countryy = newProps.country;

        document.getElementsByClassName('react-autosuggest__input')[0].value = countryy[0].toUpperCase() + countryy.slice(1);

        fetch(this.state.flask_url + '/getinfo?country=' + countryy)
            .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            deets: result
                        });
                    },
                    (error) => {
                        console.log(error);
                    }
                )
    }

    render() {

        // const cards = <></>;

        const cards = this.state.deets.map((deet) => {
            return (
                <Col xs="6" sm="3" className="deet_card">
                    <Card body>
                        <CardTitle>{deet.title}</CardTitle>
                        <CardText>
                            <div className="card-value">{deet.value}</div>
                            {deet.extra_val} {deet.extra_text}
                        </CardText>
                    </Card>
                </Col>
            );
        });

        return (
            <Row className="cards_row">
                {cards}
            </Row>
        );
    }

}

export default Card_stats;