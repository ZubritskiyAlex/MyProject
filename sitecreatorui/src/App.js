import './App.css';
import React from "react";
import Sidebar from "./containers/Sidebar";
import { Switch, Route, Redirect} from "react-router-dom";
import ProductListing from "./containers/ProductListing";
import ProductDetail from "./containers/ProductDetail";
import ShopListing from "./containers/ShopListing";
import ShopDetail from "./containers/ShopDetail";
import {About} from "./components/About/about";
import AuthPage from "./pages/authpage.component";
import ShopsPage from "./pages/shopspage.component";
import {connect} from "react-redux";
import Spinner from "./components/spinner/spinner.component";
import 'react-toastify/dist/ReactToastify.css'
import {ToastContainer, Slide} from "react-toastify";

import AddProductForm from "./containers/AddProductComponent";
import AddShopForm from "./containers/AddShopComponent";
import Login from "./components/Login/login"



function App(){

    return (
        <React.Fragment>
            <ToastContainer position="top-right" autoClose={2000}
                hideProgressBar transition={Slide}/>
            <Spinner/>
            <Sidebar/>
            <div className="container my-5">
                    <Switch>

                        <Route path="/" exact component={ShopListing}/>
                        <Route path="/shop/:shopId" exact component={ShopDetail}/>
                        <Route path='/products' exact component={ProductListing}/>
                        <Route path="/product/:productId" exact component={ProductDetail}/>
                        <Route path="/about" exact component={About}/>
                        <Route path="/auth" exact component={AuthPage}/>
                        <Route path="/shops" exact component={ShopsPage}/>
                        <Route path="/addshop" exact component={AddShopForm}/>
                        <Route path="/addproduct" exact component={AddProductForm}/>
                        <Route path="/login" exact component={Login}/>

                        <Redirect to="/auth"/>
                    </Switch>
            </div>
        </React.Fragment>
    );
}





export default (App);
