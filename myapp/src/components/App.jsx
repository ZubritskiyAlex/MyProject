import React,{Component} from "react";
import {Container} from "semantic-ui-react";
import axios from 'axios';
import ProductCard from '../containers/ProductCard';
import Filter from '../containers/Filter';
import  Menu  from '../containers/Menu';
import {Card} from "semantic-ui-react";


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
              <Filter />
              <Card.Group itemsPerRow={4}>
              {!isReady ? 'Loading...' : products.map((product,i) =>(<ProductCard key={i} {...product} />))}
              </Card.Group>
          </Container>
      );
  }
}

export default App;