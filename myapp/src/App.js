import React, {useEffect, useState} from 'react'
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Header from "./Components/Header";
import ProductsContent from "./Components/ProductsContent";
import Footer from "./Components/Footer";
import ProductList from "./Components/ProductList";
import CreateProduct from "./Components/CreateProduct";
import {uuid} from 'uuidv4';
import ProductDetail from "./Components/ProductDetail";
import EditProduct from "./Components/EditProduct";



function App() {


  const LOCAL_STORAGE_KEY = "products";
  const [products, setProducts] = useState([]);

  const createProductHandler = (product) => {
    console.log(product);
    setProducts([...products, { id: uuid(), ...product }]);
  };

  const removeProductHandler = (id) => {
    const newProductList = products.filter((product) => {
      return product.id !== id;
    });

    setProducts(newProductList);
  };

  useEffect(() => {
    const retriveProducts = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
    if (retriveProducts) setProducts(retriveProducts);
  }, []);

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(products));
  }, [products]);


      return (
    <div className="ui container">
      <Router>
        <Header />
        <Switch>
          <Route
            path="/products"
            exact
            render={(props) => (
              <ProductList
                {...props}
                products={products}
                getProductId={removeProductHandler}
              />
            )}
          />
          <Route
            path="/createproduct"
            render={(props) => (
              <CreateProduct {...props} createProductHandler={createProductHandler} />
            )}
          />

          <Route
            path="/createshop"
            render={(props) => (
              <CreateProduct {...props} createProductHandler={createProductHandler} />
            )}
          />

          <Route path="/product/:id" component={ProductDetail} />
        </Switch>
      </Router>
    </div>
  );
}
export default App;
