import React from 'react';
import { Spinner } from 'react-bootstrap';
import TableView from './TableView'

class Overview extends React.Component {
    render() {
        if (this.props.data.length > 0) {
            return (
                <TableView data = {this.props.data}/>
            )
        }  else {
            return (
                <div className="d-flex justify-content-center">
                    <Spinner style={{marginTop:'15%', width:'150px', height:'150px'}} animation="border" />
                </div>
            )
        }
    }
}

export default Overview;
