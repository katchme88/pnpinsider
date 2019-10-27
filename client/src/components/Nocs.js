import React from 'react';
import { Table } from 'react-bootstrap';

class Nocs extends React.Component {
    constructor(props) {
        super(props); 
        this.state = {
            data: [
                {
                    "2019_est_employments": 450, 
                    "2019_wage_est": "$52,500.00", 
                    "job_openings": 140, 
                    "job_outlook": "Fair ", 
                    "noc_id": "0011", 
                    "skill_level": "Mgt ", 
                    "soft_skills": "n.a. ", 
                    "statscan_link": "https://www120.statcan.gc.ca/stcsr/en/cm1/cls?fq=ds%3A102noc2016&start=0&showSum=show&q=0011", 
                    "title": "Legislators "
                }
            ]
        }
    }

    componentDidMount() {
        fetch("http://localhost:5000/api/nocs/all")
        .then(response => response.json())
        .then(data => this.setState({data: data}))
    }
    
    renderRow(row, index){
        return (
            <tr key={index}>
                {
                    Object.entries(row).map((value, index)=> {
                        if (value[0] === "statscan_link") {
                            value[1] = <a href={value[1]} target='_blank' rel="noopener noreferrer">{value[1]}</a>
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

// const is_url = (str) => {
//     const regexp =  /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
//     if (regexp.test(str)) {
//       return true;
//     }
//     else {
//       return false;
//     }
// }
export default Nocs;
