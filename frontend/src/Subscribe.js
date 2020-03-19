import React, { Component } from 'react';
import './Subscribe.css';
import { Button, Form, FormGroup, Label, Input, Container, Col } from 'reactstrap';

class Subscribe extends Component {
    render() {
        return (
            <Container className="form_container">
                <Col>
                    <p>Subscribe to our service to get regular updates about coronavirus statistics in your country:</p>
                </Col>
                <Form className="form" action="http://localhost:5000/subscribe" method="post">
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
                            <Input type="text" id="country" name="country" placeholder="Enter the country you reside in" /> 
                        </FormGroup>
                    </Col>
                    <Col className="text-center">
                        <Button type="submit" color="dark" className="btn">Subscribe</Button>
                    </Col>
                </Form>
            </Container>
        );
    }
}   

export default Subscribe;