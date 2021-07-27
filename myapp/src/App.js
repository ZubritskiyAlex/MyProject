import React, {Component} from "react";
import {connect} from "react-redux";

class App extends Component{
    render() {
        console.log(this.props.testStore);
        return(
            <div>
                <input type="text"/>
                <button>Add product</button>
                <ul>
                    {this.props.testStore.map((product,index) =>
                    <li key={index}>{product}</li>
                    )}
                </ul>
            </div>
        );
    }
}
export default connect(
    state => ({
           testStore: state
    }),
    dispatch => ({})
)(App);