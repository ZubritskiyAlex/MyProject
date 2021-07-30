import React, {Component} from "react";

class Maker extends Component {

    state = {
        activeFilter: 'all',
        productText:''
    }

    handleInputChange = ({target: {value} }) => {
        this.setState({
           productText: value,
        })
    }

    render() {
        const {activeFilter, productText} = this.state;
        const {products} = this.props;
        const isProductsExist = products && products.length > 0;


        return (
            <div className='todo-wrapper'>
            <MakerInput onChange={this.handleInputChange} value{productText} />

        )

}}




