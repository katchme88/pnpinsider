import React from 'react';
import {Accordion, Card, Button} from 'react-bootstrap'
import TableView from './TableView'

class Details extends React.Component {
    
    constructor(props) {
        super(props); 
        this.state = {
        }
    }

    handleClick = (date, draw_type) => {
        fetch(`http://localhost:5000/api/draws?date=${date}&draw_type=${draw_type}`)
        .then((response) => response.json())
        .then((data) => this.setState({...this.state, [data[0]['draw_id']]: data}))
    }

    render () {
        return (
        <Accordion>
            {this.props.data.map((item, index) => {
            return (
            <Card key={index}>
            <Card.Header>
                <Accordion.Toggle onClick={() => this.handleClick(item.date, item.draw_type, index)} as={Button} variant="link" eventKey={index}>
                {item.date} - {item.draw_type.toUpperCase()}
                </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey={index}>
                <Card.Body>
                    Draw Type: {item.draw_type}<br/>Invitations: {item.invitations}<br/>Score: {item.score}<br/>
                    <TableView data={this.state[item.draw_id]}/>
                </Card.Body>
            </Accordion.Collapse>
            </Card>)
            })}
        </Accordion>
       );
   }
}

export default Details;
