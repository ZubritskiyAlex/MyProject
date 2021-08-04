import React, {Fragment} from "react";
import {connect} from "react-redux";
import {createProduct} from "../redux/action$";

class ProductForm extends React.Component{

//    constructor(props) {
//        super(props);
//        this.state = {
//            title: ''
//        }
//    }


    state = {
        inputText: '',
        textareaText: '',
        showData: {
            name: '',
            text: '',
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


    handleInputChange = ({target: {value}}) => {
        this.setState({
            textareaText: value,
        })
    }

    handleTextareaChange = ({target: {value}}) => {
        this.setState({
            textareaText: value,
        })
    }

    handleShow = (e) => {
        e.preventDefault();
        const {inputText, textareaText} = this.state;
        this.setState({
            inputText: '',
            textareaText: '',
            showData: {
                name: inputText,
                text: textareaText,
            }
        })
    }



    render() {
        const {inputText, textareaText, showData} = this.state;
        const {name, text} = showData;
        return(
            <Fragment>
            <form onSubmit={this.submitHandler}>
                <div className="form-group">
                    <label htmlFor="title">Product title: </label>
                    <input
                        type="text"
                        className="form-control"
                        id="title"
                        value={inputText}
                        name="title"
                        onChange={this.handleInputChange}
                    />
                    <label htmlFor="text">Price: </label>
                    <textarea id="text" value={textareaText} onChange={this.handleTextareaChange} /><br/>
                </div>
                <button className="btn btn-success" type="submit">Create!</button>
            </form>
            <h2>{name}</h2>
            <h3>{text}</h3>
           </Fragment>
        )
    }
}

const mapDispatchToProps = {
    createProduct
}

export default connect(null, mapDispatchToProps)(ProductForm)