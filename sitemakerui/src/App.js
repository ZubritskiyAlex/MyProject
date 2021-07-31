import React from "react";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import {About} from "./pages/About";
import {Home} from "./pages/Home";
import {Navbar} from "./components/Navbar";
import {ProductForm} from "./components/ProductForm";
import {ShopForm} from "./components/ShopForm";
import {Shops} from "./components/Shops";
import {Products} from "./components/Products";


function App() {
  return (

    <Router>
    <Navbar/>
    <div className="container pt-4">
      <Switch>
        <Route path={'/'} exact component={Home}/>
        <Route path={'/about'}  component={About}/>
        <Route path={'/createproduct'}  component={ProductForm}/>
        <Route path={'/createshop'}  component={ShopForm}/>
        <Route path={'/shops'}  component={Shops}/>
        <Route path={'/products'}  component={Products}/>
      </Switch>
    </div>
    </Router>

  );
}

export default App;
