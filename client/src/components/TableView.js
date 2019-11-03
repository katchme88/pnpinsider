import React from 'react';
import {Table} from 'react-bootstrap'

class TableView extends React.Component {
    render() {
        if (typeof this.props.data != 'undefined'){
            return (
                <Table striped bordered hover size="sm">
                    <thead>
                        <tr>
                            { Object.keys(this.props.data[0]).map((colName, index) => { return <th key={index}>{colName}</th>})}
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.data.map((row, index)=> {
                            return (
                                <tr key={index}>
                                    { Object.entries(row).map((vals, idx) => {
                                            if (vals[0] === 'noc_id') {
                                                vals[1] = <a href = {`https://www120.statcan.gc.ca/stcsr/en/cm1/cls?fq=ds%3a102noc2016&start=0&showsum=show&q=${vals[1]}`} target={'_blank'}>{vals[1]}</a> 
                                            } 
                                            return (
                                                <td key={idx}>{vals[1]}</td>
                                            )
                                        })
                                    }
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