import React, { Component } from 'react';
import { Button, Form, FormGroup, Label, Input, Container, Col, Alert } from 'reactstrap';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';
import CountrySuggestor from './CountrySuggestor';
import './Subscribe.css';

class Subscribe extends Component {

    constructor(props) {
        super(props);
        this.action_url = window.location.protocol + '//' + window.location.hostname +":5000/subscribe";
    }

    render() {

        const onSuggestionSelected = (event, { suggestion, suggestionValue, suggestionIndex, sectionIndex, method }) => {
            console.log(suggestion);
            console.log(suggestionValue);
            document.getElementById('country_hidden_field').value = suggestionValue;
        }

        var SuccessAlert = <></>;
        var DangerAlert = <></>;
        if (this.props.message === 'subscribed') {
            SuccessAlert = <Alert color="success">You will now recieve regular coronavirus updates on your email id!</Alert>;
        }
        else if (this.props.message === 'wrongemail') {
            DangerAlert = <Alert color="danger">The email id that you entered is incorrect, please try again</Alert>;
        }
        else if (this.props.message === 'incomplete') {
            DangerAlert = <Alert color="danger">Please fill all the fields to subscribe successfully</Alert>;
        }

        return (
            <Container className="form_container">
                <Col>
                    {SuccessAlert}
                    {DangerAlert}
                    <h6>Subscribe to our service to get regular updates about coronavirus statistics in your country.</h6>
                </Col>
                <Form className="form" action={this.action_url} method="post">
                    <Col>
                        <FormGroup>
                            <Label for="name">Name:</Label>
                            <Input type="text" id="name" name="name" placeholder="Enter your name here"/>
                        </FormGroup>
                    </Col>
                    <Col>
                        <FormGroup>
                            <Label for="email">Email:</Label>
                            <Input type="text" id="email" name="email" placeholder="Enter your email id on which you would like to recieve the updates" />
                        </FormGroup>
                    </Col>
                    <Col>
                        <FormGroup>
                            <Label for="country">Country:</Label>
                            <CountrySuggestor placeholder="Enter the country you reside in" onSuggestionSelected={onSuggestionSelected} />
                            <Input type="text" id="country_hidden_field" name="country" placeholder="Enter the country you reside in" />
                        </FormGroup>
                    </Col>
                    <Col className="text-center">
                        {/* created this button to prevent default on enter form submit shit */}
                        <Button type="submit" className="bali_ka_bakra" disabled aria-hidden="true"></Button>
                        <Button type="submit" color="dark" className="btn">Subscribe</Button>
                    </Col>
                </Form>
                <br></br>
                <Col className="text-center">
                <Link to = "/stats"><Button color="danger" className="btn">Continue without subscribing</Button></Link>
                </Col>
            </Container>
        );
    }
}   

export default Subscribe;