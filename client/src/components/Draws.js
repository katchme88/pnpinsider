import React from 'react';
import { Table } from 'react-bootstrap';

class Draws extends React.Component {
    constructor(props) {
        super(props); 
        this.state = {
            data: [{
                "date": "2019-09-25", 
                "draw_id": 1, 
                "draw_type": "express", 
                "invitations": 404, 
                "score": 70
              }, 
              {
                "date": "2019-09-25", 
                "draw_id": 2, 
                "draw_type": "oid", 
                "invitations": 365, 
                "score": 79
              }, 
              {
                "date": "2019-10-02", 
                "draw_id": 3, 
                "draw_type": "express", 
                "invitations": 396, 
                "score": 68
              }, 
              {
                "date": "2019-10-02", 
                "draw_id": 4, 
                "draw_type": "oid", 
                "invitations": 214, 
                "score": 68
              }, 
              {
                "date": "2019-10-08", 
                "draw_id": 5, 
                "draw_type": "express", 
                "invitations": 231, 
                "score": 69
              }, 
              {
                "date": "2019-10-08", 
                "draw_id": 6, 
                "draw_type": "oid", 
                "invitations": 328, 
                "score": 69
              }, 
              {
                "date": "2019-10-17", 
                "draw_id": 7, 
                "draw_type": "express", 
                "invitations": 986, 
                "score": 67
              }]
        }
    }

    componentDidMount() {
        fetch("http://localhost:5000/api/draws")
        .then(response => response.json())
        .then(data => this.setState({data: data}))
    }
    
    renderRow(row, index){
        return (
            <tr key={index}>
                {
                    Object.values(row).map((value, index)=> {
                        return <td key={index}>{value}</td> 
                    })
                }
            </tr>
        )       
    }

    renderHead(title, index) {
        return (
            <th key={index}>
                {title}
            </th>
        )
    }

    render() {
        let headers = Object.keys(this.state.data[0])
        return (
            <Table striped bordered hover>
                <thead>
                    <tr>
                        {headers.map(this.renderHead)}
                    </tr>
                </thead>
                <tbody>
                    {this.state.data.map(this.renderRow)}
                </tbody>
            </Table>
        );
    }
}

export default Draws;
