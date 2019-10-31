import React from 'react';
import { Table, Spinner } from 'react-bootstrap';

class Draws extends React.Component {

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

    render() {
        if (this.props.data.length > 0) {
        let headers = Object.keys(this.props.data[0])
        return (
            <Table striped bordered hover size="sm">
                <thead>
                    <tr>
                        {headers.map(this.renderHead)}
                    </tr>
                </thead>
                <tbody>
                    {this.props.data.map(this.renderRow)}
                </tbody>
            </Table>
        )} else {
            return <Spinner animation="border" />
        }
    }
}

export default Draws;
