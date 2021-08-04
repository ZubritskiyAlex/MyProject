import './App.css';
import {BrowserRouter as Router,Route, Switch,} from "react-router-dom";
import {Header} from "./components/Header/Header";
import {Footer} from "./components/Footer/Footer";
import {ProductContent} from "./containers/ProductContent/ProductContent";
import {LoginPage} from "./containers/LoginPage/LoginPage";
import {About} from "./components/About/about";
import {AddProductForm} from "./containers/ProductContent/components/AddProductForm";
import {useState} from "react";




function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(localStorage.getItem('isLoggedIn') === 'true');
    const [userName, setUserName] = useState(localStorage.getItem('userName'));


    return (
    <Router>
    <div className="App">
        <Header
            userName={userName}
            isLoggedIn={isLoggedIn}
            setIsLoggedIn={setIsLoggedIn}
        />

      <main>
          <Switch>
            <Route exact path="/products" component={ProductContent} />
            <Route exact path="/productcreate" component={AddProductForm} />

            <Route exact path="/login"
                render ={(props) =>
                    <LoginPage
                        {...props}
                        setIsLoggedIn={setIsLoggedIn}
                        setUserName={setUserName}/>}
            />



            <Route exact path="/" component={About}/>


          </Switch>
      </main>

      <Footer year={new Date().getFullYear()}/>
    </div>
    </Router>
  );
}

export default App;
