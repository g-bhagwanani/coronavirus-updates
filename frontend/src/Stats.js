import React, { Component } from 'react';
import CountrySuggestor from './CountrySuggestor';
import { Container } from 'reactstrap';
import './Stats.css';
import Card_stats from './Card_stats';
import Graphical_stats from './Graphical_stats';

class Stats extends Component {

    // constructor(props) {
    //     super(props);
    // }

    render() {

        const onSuggestionSelected = (event, { suggestion, suggestionValue, suggestionIndex, sectionIndex, method }) => {
            console.log(suggestion);
            console.log(suggestionValue);
            this.props.history.push('/stats/' + suggestionValue.toLowerCase());
        }

        const country = this.props.match.params.country;

        return (
            <>
                <h1 className = "title">Coronavirus Updates</h1>
                <Container className="stats_page_container">
                    <div className="country_ka_search_box">
                        <CountrySuggestor className="country_ip" placeholder="Type a country to get the stats" onSuggestionSelected={onSuggestionSelected} />
                    </div>
                    <Card_stats country={country} />
                </Container>
            </>
        )
    }
}

export default Stats;