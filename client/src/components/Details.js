import React from 'react';
import {Accordion, Card, Button, Table} from 'react-bootstrap'

class Details extends React.Component {
    
    constructor(props) {
        super(props); 
        this.state = {
        }
    }

    handleClick = (date, draw_type) => {
        fetch(`http://localhost:5000/api/draws?date=${date}&draw_type=${draw_type}`)
        .then((response) => response.json())
        .then((data) => this.setState({...this.state, [data.draw_id]: data}))
    }

    renderHead = (title, index) =>  {
        return (
            <th key={index}>
                {title}
            </th>
        )
    }

    renderRow = (row, index) => {
        return (
            <tr key={index}>
                {
                    Object.entries(row).map((value, index)=> {
                        if (value[0]==='noc_list'){
                            return <td key={index}>{value[1].join(',')}</td>
                        }
                        return <td key={index}>{value[1]}</td>
                    })
                }
            </tr>
        )       
    }

    renderTable = (data) => {
    }

    render () {
        return (
        <Accordion>
            {this.props.data.map((item, index) => {
            return (
            <Card key={index}>
            <Card.Header>
                <Accordion.Toggle onClick={() => this.handleClick(item.date, item.draw_type, index)} as={Button} variant="link" eventKey={index}>
                {item.date}
                </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey={index}>
                <Card.Body>
                    Draw Type: {item.draw_type}<br/>Invitations: {item.invitations}<br/>Score: {item.score}<br/>
                    <Table>
                        {}
                    </Table>
                </Card.Body>

            </Accordion.Collapse>
            </Card>)
            })}
        </Accordion>
       );
   }
}

export default Details;
