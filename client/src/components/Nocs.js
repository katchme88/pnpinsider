import React from 'react';
import { Table, Spinner } from 'react-bootstrap';

class Nocs extends React.Component {
    renderRow(row, index){
        return (
            <tr key={index}>
                {
                    Object.entries(row).map((value, index)=> {
                        if (value[0] === "noc_id") {
                            value[1] = <a href={`https://www120.statcan.gc.ca/stcsr/en/cm1/cls?fq=ds%3A102noc2016&start=0&showSum=show&q=${value[1]}`} target='_blank' rel="noopener noreferrer">{value[1]}</a>
                        }
                        return <td key={index}>{value[1]}</td> 
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
        if (this.props.data.length > 0) {
            let headers = Object.keys(this.props.data[0])
            return <Table striped bordered hover>
                <thead>
                    <tr>
                        {headers.map(this.renderHead)}
                    </tr>
                </thead>
                <tbody>
                    {this.props.data.map(this.renderRow)}
                </tbody>
            </Table>
        } else {
            return <div className="d-flex justify-content-center">
                     <Spinner style={{marginTop:'15%', width:'150px', height:'150px'}} animation="border" />
                   </div>
            
        }
    }
}

export default Nocs;
