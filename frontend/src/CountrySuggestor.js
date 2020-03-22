import React, { Component } from 'react';
import Autosuggest from 'react-autosuggest';
import { Col, Row } from 'reactstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const countries = [
    {
        name: 'India'
    },
    {
        name: 'Italy'
    },
    {
        name: 'China'
    },
    {
        name: 'Chile'
    }
];

const getSuggestions = value => {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;

    return inputLength === 0 ? [] : countries.filter(country =>
        country.name.toLowerCase().slice(0, inputLength) === inputValue
    );
};

const getSuggestionValue = suggestion => suggestion.name;

const renderSuggestion = suggestion => (
    <div>
        {suggestion.name}
    </div>
);

const renderInputComponent = inputProps => (
    <Row className = "input_country">
        <Col className="search_icon">
            <FontAwesomeIcon icon={faSearch} />
        </Col>
        <Col>
            <input {...inputProps} />
        </Col>
    </Row>
);

class CountrySuggestor extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            suggestions: []
        }
    }

    onChange = (event, { newValue }) => {
        this.setState({
            value: newValue
        });
    };

    onSuggestionsFetchRequested = ({ value }) => {
        this.setState({
            suggestions: getSuggestions(value)
        });
    };

    onSuggestionsClearRequested = () => {
        this.setState({
            suggestions: []
        });
    };

    render() {
        const inputProps = {
            placeholder: this.props.placeholder,
            value: this.state.value,
            onChange: this.onChange
        };

        return (
            <Autosuggest
                suggestions = {this.state.suggestions}
                onSuggestionsFetchRequested = {this.onSuggestionsFetchRequested}
                onSuggestionsClearRequested = {this.onSuggestionsClearRequested}
                getSuggestionValue = {getSuggestionValue}
                renderSuggestion = {renderSuggestion}
                inputProps = {inputProps}
                renderInputComponent = {renderInputComponent}
                highlightFirstSuggestion={true}
                onSuggestionSelected = {this.props.onSuggestionSelected}
            />
        );

    }
}

export default CountrySuggestor;
