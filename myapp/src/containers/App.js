import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as productsActions from '../actions/products';
import App from '../components/App';
import orderBy from 'lodash/orderBy';

const sortBy = (products, filterBy) => {
  switch (filterBy) {
    case 'price_high':
      return orderBy(products, 'price', 'desc');
    case 'price_low':
      return orderBy(products, 'price', 'asc');
    case 'shop':
      return orderBy(products, 'shop', 'asc');
    default:
      return products;
  }
};

const filterProducts = (books, searchQuery) =>
  products.filter(
    o =>
      o.title.toLowerCase().indexOf(searchQuery.toLowerCase()) >= 0 ||
      o.shop.toLowerCase().indexOf(searchQuery.toLowerCase()) >= 0,
  );

const searchProducts = (products, filterBy, searchQuery) => {
  return sortBy(filterBooks(products, searchQuery), filterBy);
};

const mapStateToProps = ({ books, filter }) => ({
  products: products.items && searchProducts(products.items, filter.filterBy, filter.searchQuery),
  isReady: products.isReady,
});

const mapDispatchToProps = dispatch => ({
  ...bindActionCreators(productsActions, dispatch),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(App);