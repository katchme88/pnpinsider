import React from 'react';
import {Table} from 'react-bootstrap'

class TableView extends React.Component {
    render() {
        if (typeof this.props.data != 'undefined'){
            return (
                <Table striped bordered hover size="sm">
                    <thead>
                        <tr>
                            {Object.keys(this.props.data[0]).map((colName, index) => { return <th key={index}>{colName}</th>})}
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.data.map((row, index)=> {
                            return (
                                <tr key={index}>
                                    {Object.values(row).map((colValue, index)=>{return <td key={index}>{colValue}</td>})}
                                </tr>
                            )
                        })}
                    </tbody>
                </Table>       
            )
        }

        return(
            <p/>
        )
    }
}

export default TableView;