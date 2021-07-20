import React, {Component} from "react";


class Container2 extends Component{
    constructor(props) {
        super(props);

        this.state = {
            stateprop2: "Our Initial State"
        }
    }
    changeState =() => (
        this.setState({stateprop2: "New State"})
    )

    render(){
    return(
    <div>
        <button onClick={() => this.setState({stateprop2: "New State"})}>Change State</button>
        {this.state.stateprop2}
    </div>

    )}
}
export default Container2;