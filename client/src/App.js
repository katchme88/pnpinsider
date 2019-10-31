import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Draws from './components/Draws'
import Home from './components/Home'
import Nocs from './components/Nocs'
import { Nav, Navbar, Form, FormControl, Button } from 'react-bootstrap';

class App extends React.Component {
  constructor(props) {
    super(props); 
    this.state = {
        draws: [],
        nocs: []
    }
  }

  componentDidMount() {
    fetch("http://localhost:5000/api/draws")
    .then(response => response.json())
    .then(data => this.setState({draws: data, nocs: this.state.nocs}))

    fetch("http://localhost:5000/api/nocs/all")
    .then(response => response.json())
    .then(data => this.setState({draws: this.state.draws, nocs: data}))
  }

  render(){
    return (
      <Router>
        <div>
          <Navbar sticky="top" bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/home">PNP Trend</Navbar.Brand>
            <Nav className="mr-auto">
              <Nav.Link as={Link} to="/">Home</Nav.Link>
              <Nav.Link as={Link} to="/draws">Draws</Nav.Link>
              <Nav.Link as={Link} to="/nocs">Noc List</Nav.Link>
            </Nav>
            <Form inline>
              <FormControl type="text" placeholder="Search" className="mr-sm-2" />
              <Button variant="outline-info">Search</Button>
            </Form>
          </Navbar> 
          <Switch>
            <Route path="/draws"><Draws data={this.state.draws}/></Route>
            <Route path="/nocs">< Nocs data={this.state.nocs}/></Route>
            <Route path="/"><Home /></Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;