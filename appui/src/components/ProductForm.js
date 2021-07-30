import React from "react";
import {connect} from "react-redux";
import {createProduct} from "../redux/action$";

class ProductForm extends React.Component{

    constructor(props) {
        super(props);
        this.state = {
            title: ''
        }
    }

    submitHandler = event =>{
        event.preventDefault()

        const {title} = this.state

        const newProduct = {
            title, id: Date.now().toString()
        }

        console.log(newProduct)
        this.setState({title: ''})
    }



    //Universal method
    changeInputHandler = event => {
        event.persist()
        this.setState(prev => ({...prev,...{
            [event.target.name]: event.target.value
            }}))
    }

    render() {
        return(
            <form onSubmit={this.submitHandler}>
                <div className="form-group">
                    <label htmlFor="title">Product title</label>
                    <input
                        type="text"
                        className="form-control"
                        id="title"
                        value={this.state.title}
                        name="title"
                        onChange={this.changeInputHandler}
                    />
                </div>
                <button className="btn btn-success" type="submit">Create!</button>
            </form>
        )
    }
}

const mapDispatchToProps = {
    createProduct
}

export default connect(null, mapDispatchToProps)(ProductForm)