import './App.css';
import {Component} from "react";
import Sidebar from "./containers/Sidebar";
import {BrowserRouter as Router, Switch, Route, Redirect} from "react-router-dom";
import ProductListing from "./containers/ProductListing";
import ProductDetail from "./containers/ProductDetail";
import ShopListing from "./containers/ShopListing";
import ShopDetail from "./containers/ShopDetail";
import {About} from "./components/About/about";
import AuthPage from "./pages/authpage.component";
import ShopsPage from "./pages/shopspage.component";
import EditShopPage from "./pages/editshoppage.component";

class App extends Component{

    render() {
        return(
            <div className="container my-5">
                <Router>
                    <Sidebar/>
                    <Switch>
                        <Route path="/" exact component={ShopListing}/>
                        <Route path="/shop/:shopId" exact component={ShopDetail}/>
                        <Route path ='/products' exact component={ProductListing} />
                        <Route path="/product/:productId" exact component={ProductDetail}/>
                        <Route path="/about" exact component={About}/>
                        <Route path="/auth" exact component={AuthPage}/>
                        <Route path="/shops" exact component={ShopsPage}/>
                        <Route path="/edit-shop" exact component={EditShopPage}/>
                        <Redirect to="/products"/>
                    </Switch>
                </Router>
            </div>
        );
    }
}

export default App;