import React, {Component} from "react";
import './App.css'
import * as styles from './styles'

import Component1 from "./functional/component1";
import Container1 from "./containers/container";

class App extends Component {

  render(){
    return(
        <div className="App">
        <div style={styles.styles}>
            Welcome to my study app!
        </div>
        <button>Button 1</button>
            React
            <Container1 nickname="PI"/>
            <Component1 name ='Alex' age={21} />
        </div>
    );
}
}

export default App;
