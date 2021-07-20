import React, {Component} from "react";
import './App.css'
import * as styles from './styles'
import Component1 from "./functional/component1";
import Component2 from "./functional/component2";
import Container2 from "./containers/container2"

class App extends Component{
    render() {


    return(
        <div className="App">
        <div style={styles.styles}>Welcome to creator of online stores </div>
        <button>Button 1</button>
        <Component1 title ='Hoodie' price ={120} />
        <Container2 store='TechnoStore' />
        <Component2 title ='Laptop' price ={2000} />
        </div>
    );
}
}

export default App;
