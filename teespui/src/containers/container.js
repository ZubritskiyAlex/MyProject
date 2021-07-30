import React, {Component} from "react";
import * as ACTIONS from '../store/actions/action_s';

import {connect} from 'react-redux';


class Container1 extends Component{
    render() {
        const user_text = "text 1"

        }
        return(
            <div>
                <button onClick={() => console.log(this.props.stateprop1)}> Get State</button>
                <button onClick={() => this.props.action1()}>Dispatch Action 1 </button>
                <button onClick={() => this.props.action2()}>Dispatch Action 2 </button>
                <button onClick={() => this.props.action_creator_1()}>Dispatch Action Creator 1</button>
                <button onClick={() => this.props.action_creator_2()}>Dispatch Action Creator 2</button>
                <button onClick={() => this.props.action_creator_3(user_text)}>Dispatch Action Creator 3</button>
            </div>

        )}
}

function mapStateToProps(state){

    return{
        stateprop1: state.stateprop1
    }
}

function mapDispatchToProps(dispatch){
    return {

        action1: () => dispatch(ACTIONS.SUCCESS),
        action2: () => dispatch(ACTIONS.FAILURE),
        action_creator_1: () => dispatch(ACTIONS.success()),
        action_creator_2: () => dispatch(ACTIONS.failure()),
        action_creator_3: (text) => dispatch(ACTIONS.user_input(text)),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Container1);