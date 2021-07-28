import React, {Component} from "react";
import {connect} from "react-redux";
import {Link} from "react-router-dom";
import {getProducts} from './actions/products.js'
import {render} from "react-dom";

class App extends Component {
    addProduct = () => {
        console.log('addProduct', this.productInput.value);
        this.props.onAddProduct(this.productInput.value);
        this.productInput.value = '';
    }

    findProduct(){
        console.log('findProduct', this.searchInput.value);
        this.props.onFindProduct(this.searchInput.value);
    }

    render() {
        console.log(this.props.products);
        return (
            <div>
                <div>
                    <input type="text" ref={(input) => {
                        this.productInput = input
                    }}/>
                    <button onClick={this.addProduct.bind(this)}>Add product</button>
                </div>

                <div>
                    <input type="text" ref={(input) => {
                        this.searchInput = input
                    }}/>
                    <button onClick={this.findProduct.bind(this)}>Find product</button>
                </div>


                <ul>
                    {this.props.products.map((product, index) =>
                        <li key={index}>
                                {product.name}
                        </li>
                    )}
                </ul>
            </div>
        );
    }
}
export default connect(
    state => ({
           products: state.products.filter(product => product.name.includes(state.filterProducts))
}),
    dispatch => ({
        onAddProduct: (name) => {
            const payload = {
                id: Date.now().toString(),
                name
            };
            dispatch({type: 'ADD_PRODUCT', payload});
        },
        onFindProduct: (name) => {
            dispatch({type: 'FIND_PRODUCT', payload: name});
        },
        onGetProducts: () => {
            dispatch(getProducts());
        }
    })
)(App);