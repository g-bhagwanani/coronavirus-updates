import React from 'react';

function Subscribe() {
    return (
        <form action="http://localhost:5000/subscribe" method="post">
            <label for="name">Name:</label><br></br>
            <input type="text" id="name" name="name"></input><br></br>
            <label for="email">Email:</label><br></br>
            <input type="text" id="email" name="email"></input><br></br>
            <label for="country">Country:</label><br></br>
            <input type="text" id="country" name="country"></input>
            <button type ="submit">Subscribe</button>
        </form>
    );
}

export default Subscribe;