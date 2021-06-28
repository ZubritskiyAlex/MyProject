import React,{ Component } from "react";
import logo from './logo.svg';
import './App.css';
import './store';
import {connect} from "react-redux";
import {setProducts} from "./action/products";
import products from '/products.json';
import axios from 'axios';

class App extends Component{
  componentWillMount() {
      const { setProducts} = this.props;
      axios.get('/products.json').then(({data}) =>{
          setProducts(data);
      });
  }


    render() {
      const { products } = this.props;
      return (
          <ul>
              {
                  !books ? 'Loading...' : books.map(book =>(
                      <li>
                          <b>{book.title}</b>-{book.author}
                      </li>
                      )
                  )
              }
          </ul>
      );
  }
}

const mapState = state => ({
    ...state
});

const mapStateToProps = ({products}) => ({
    products: products.items
});

const  mapDispatchToProps = dispatch => ({
    setProducts: products => dispatch(setProducts(products))
});

export default connect(mapState, mapDispatchToProps)(App);
