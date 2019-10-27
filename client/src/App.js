import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Draws from './components/Draws'
import Home from './components/Home'
import Nocs from './components/Nocs'

class App extends React.Component {
  render(){
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/draws">Draws</Link></li>
              <li><Link to="/nocs">Nocs</Link></li>
            </ul>
          </nav>
          
          <Switch>
            <Route path="/draws"><Draws /></Route>
            <Route path="/nocs"><Nocs /></Route>
            <Route path="/"><Home /></Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;