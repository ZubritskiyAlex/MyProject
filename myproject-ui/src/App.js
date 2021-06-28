import React,{ Component } from "react";
import logo from './logo.svg';
import './App.css';
import './store';
import {Card} from "semantic-ui-react";
import {connect} from "react-redux";
import {setProducts} from "./action/products";
import products from '/products.json';
import axios from 'axios';
import { Menu } from './components/Menu';
import { ProductCard } from './components/ProductCard';


class App extends Component{
  componentWillMount() {
      const { setProducts} = this.props;
      axios.get('/products.json').then(({data}) =>{
          setProducts(data);
      });
  }


    render() {
      const { products, isReady } = this.props;
      return (
          <Container>
              <Menu/>
              <Card.Group itemsPerRow={4}>
              <ul>
              {!isReady ? 'Loading...' : products.map((product,i) =>(<ProductCard key={i} {...product} />))} </ul>
              </Card.Group>
          </Container>
      );
  }
}

const mapState = state => ({
    ...state
});

const mapStateToProps = ({products}) => ({
    products: products.items,
    isReady: products.isReady
});

const  mapDispatchToProps = dispatch => ({
    setProducts: products => dispatch(setProducts(products))
});

export default connect(mapState, mapDispatchToProps)(App);
