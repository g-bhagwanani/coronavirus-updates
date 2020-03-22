import React, { Component } from 'react';
import CountrySuggestor from './CountrySuggestor';
import { Container, Input, Form } from 'reactstrap';
import './Stats.css';
import Button from 'reactstrap/lib/Button';

class Stats extends Component {

    constructor(props) {
        super(props);
        this.action_url = window.location.protocol + '//' + window.location.hostname +":5000/countrystats";
    }

    render() {

        const onSuggestionSelected = (event, { suggestion, suggestionValue, suggestionIndex, sectionIndex, method }) => {
            console.log(suggestion);
            console.log(suggestionValue);
            document.getElementById('country_hidden_field').value = suggestionValue;
            // form submit here
            document.getElementById('country_stats_search_form').submit();
        }

        const country = this.props.match.params.country;

        return (
            <>
                <h1 className = "title">Coronavirus Updates</h1>
                <Container className="stats_page_container">
                    <Form action={this.action_url} method="post" id="country_stats_search_form">
                        <CountrySuggestor className="country_ip" placeholder="Type a country to get the stats" onSuggestionSelected={onSuggestionSelected} />
                        <Input type="text" id="country_hidden_field" name="country" placeholder="Enter the country you reside in" />
                        <Button type="submit" className="hidden_btn" aria-hidden="true">Submit</Button>
                    </Form>
                    {country} stats will appear here!
                </Container>
            </>
        )
    }
}

export default Stats;