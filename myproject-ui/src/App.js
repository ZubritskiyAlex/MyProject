import React,{ Component } from "react";
import logo from './logo.svg';
import './App.css';
import './store';
import {connect} from "react-redux";
import {setProducts} from "./action/products";
import products from "./reducers/products";

class App extends Component{
  render() {
      const { products } = this.props.products;
      const { setBooks } = this.props
      const newProducts = [{
          id:0,
          title: 'Shopping Cart'
      }];
      return (
          <div>
              <h1>{products[0].title}</h1>
              <button onClick= {setBooks.bind(this, newProducts)}>SET NEW product</button>
          </div>
      );
  }
}

const mapState = state => ({
    ...state
});

const mapStateToProps = dispatch => ({
    ...state
})

const  mapDispatchToProps = dispatch => ({
    setProducts: products => dispatch(setProducts(products))
});

export default connect(mapState, mapDispatchToProps)(App);
