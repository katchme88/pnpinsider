import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Draws from './components/Draws'
import Home from './components/Home'
import Nocs from './components/Nocs'
import Details from './components/Details'
import Overview from './components/Overview'
import { Nav, Navbar } from 'react-bootstrap';
import './App.css'
import logo from './canada.png'

class App extends React.Component {
  constructor(props) {
    super(props); 
    this.state = {
        draws: [],
        nocs: [],
        overview: []
    }
  }

  componentDidMount() {
    fetch("/api/draws?summary=1")
    .then(response => response.json())
    .then(data => this.setState({...this.state, draws: data}))

    fetch("/api/nocs/all")
    .then(response => response.json())
    .then(data => this.setState({...this.state, nocs: data}))

    fetch("/api/draws/overview")
    .then(response => response.json())
    .then(data => this.setState({...this.state, overview: data}))
  }

  render(){
    return (
      <Router>
        <div style={{backgroundColor: `#f2f2f2`, minHeight:'100vh'}}>
          <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" sticky="top">
            <Navbar.Brand as={Link} to="/home"><img
              alt=""
              src={logo}
              width="40"
              height="30"
              className="d-inline-block align-top"
            />{' '}PNP Insights</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Item><Nav.Link eventKey="1" as={Link} to="/">Home</Nav.Link></Nav.Item>
              <Nav.Item><Nav.Link eventKey="2" as={Link} to="/draws">Draws</Nav.Link></Nav.Item>
              <Nav.Item><Nav.Link eventKey="3" as={Link} to="/nocs">NocList</Nav.Link></Nav.Item>
              <Nav.Item><Nav.Link eventKey="4" as={Link} to="/details">Details</Nav.Link></Nav.Item>
              <Nav.Item><Nav.Link eventKey="5" as={Link} to="/overview">Overview</Nav.Link></Nav.Item>
            </Nav>
            {/* <Form inline>
              <FormControl type="text" placeholder="Search" className="mr-sm-2" />
              <Button variant="outline-info">Search</Button>
            </Form> */}
            </Navbar.Collapse>
          </Navbar> 
          <Switch>
            <Route path="/draws"><Draws data={this.state.draws}/></Route>
            <Route path="/nocs">< Nocs data={this.state.nocs}/></Route>
            <Route path="/details"><Details data={this.state.draws}/></Route>
            <Route path="/overview"><Overview data={this.state.overview}/></Route>

              <Route path="/"><Home data={this.state.draws}/></Route>

          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;