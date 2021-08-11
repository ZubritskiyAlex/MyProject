import './App.css';
import React, {useEffect, useState} from "react";
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
import axios from "axios";
import 'react-toastify/dist/ReactToastify.css'
import {ToastContainer, Slide} from "react-toastify";

import {logoutUser} from "./redux/actions/authActionCreator";
import AddProductForm from "./containers/AddProductComponent";
import AddShopForm from "./containers/AddShopComponent";



function App({user, dispatchLogoutAction}){
    const [products, setProducts] = useState([])

    useEffect(() =>{
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/product/"
        }).then(response => {setProducts(response.data)
        })
    }, [])

    return (
        <React.Fragment>
            <ToastContainer position="top-right" autoClose={2000}
                hideProgressBar transition={Slide}/>
            <Spinner/>
            <Sidebar isLoggedIn={user.isLoggedIn} userName={user.fullName}
            onLogout={dispatchLogoutAction}
            />
            <div className="container my-5">
                <ul>
                    {products.map(p => (<li key={p.id}></li>))}
                </ul>

                {user.isLoggedIn ?
                    (<Switch>
                        <Route path="/auth" exact component={AuthPage}/>
                        <Route path="/" exact component={ShopListing}/>
                        <Route path="/shop/:shopId" exact component={ShopDetail}/>
                        <Route path='/products' exact component={ProductListing}/>
                        <Route path="/product/:productId" exact component={ProductDetail}/>
                        <Redirect to="/auth"/>
                    </Switch> ):
                    (<Switch>
                        <Route path="/" exact component={ShopListing}/>
                        <Route path="/shop/:shopId" exact component={ShopDetail}/>
                        <Route path='/products' exact component={ProductListing}/>
                        <Route path="/product/:productId" exact component={ProductDetail}/>
                        <Route path="/about" exact component={About}/>
                        <Route path="/auth" exact component={AuthPage}/>
                        <Route path="/shops" exact component={ShopsPage}/>
                        <Route path="/addshop" exact component={AddShopForm}/>
                        <Route path="/addproduct" exact component={AddProductForm}/>
                        <Redirect to="/auth"/>
                    </Switch>)
                }
            </div>
        </React.Fragment>
    );
}

const mapStateToProps = (state) => ({user:state.user});
const mapDispatchToProps = (dispatch) => ({
    dispatchLogoutAction: () => dispatch(logoutUser())
});



export default connect(mapStateToProps, mapDispatchToProps)(App);
