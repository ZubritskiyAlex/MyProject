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
import ShopList from "./Components/ShopList";
import CreateShop from "./Components/CreateShop";
import ShopDetail from "./Components/ShopDetail";
import Homepage from "./Components/Homepage";




function App() {

  const LOCAL_STORAGE_KEY = "products";
  const LOCAL_STORAGE_KEY_1 = "shops";
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults]= useState([]);

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

const searchHandler=(searchTerm) => {
  setSearchTerm(searchTerm);
  if (searchTerm !== "") {
    const newProductList = products.filter((product) => {
      return Object.values(product)
          .join(" ")
          .toLowerCase()
          .includes(searchTerm.toLowerCase());
    });
    setSearchResults(newProductList);
  }else{
    setSearchResults(products);
  }
};


  useEffect(() => {
    const retriveProducts = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));
    if (retriveProducts) setProducts(retriveProducts);
  }, []);

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(products));
  }, [products]);


    const [shops, setShops] = useState([])

    const createShopHandler = (shop) =>{
      console.log(shop);
      setShops([...shops,{id:uuid(), ...shops}]);
    };

    const removeShopHandler = (id) => {
      const newShopList = shops.filter((shop) => {
        return shop.id !== id;
      })
      setShops(newShopList);
    };

    useEffect(() =>{
      const retriveShops = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY_1));
      if (retriveShops) setShops(retriveShops);

    }, []);


    useEffect(() =>{
      localStorage.setItem(LOCAL_STORAGE_KEY_1, JSON.stringify(shops));
    }, [shops]);



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
                products={searchTerm.length < 1 ? products : searchResults}
                getProductId={removeProductHandler}
                term={searchTerm}
                searchKeyword={searchHandler}
              />
            )}
          />
          <Route
            path="/createproduct"
            render={(props) => (
              <CreateProduct {...props} createProductHandler={createProductHandler} />
            )}
          />


          <Route path="/shops"
                 exact
                 render = {(props) =>(
                     <ShopList
                      {...props}
                      shops={shops}
                      getShopId={removeShopHandler}
                     />
                 )}
          />
          <Route
              path="/createshop"
              render={(props)=> (
                  <CreateShop {...props} createShopHandler={createShopHandler}/>
            )}
          />
          <Route path="/product/:id" component={ProductDetail}
          />

          <Route path="/shop/:id" component={ShopDetail}

          />
          <Route path="/" component={Homepage}
          />
        </Switch>
      </Router>
    </div>
  );
}
export default App;
