import './App.css';
import {BrowserRouter as Router,Route, Switch,} from "react-router-dom";
import {Header} from "./components/Header";
import {Footer} from "./components/Footer/Footer";
import {ProductContent} from "./containers/ProductContent/ProductContent";
import {LoginPage} from "./containers/LoginPage/LoginPage";


function App() {
  return (
    <Router>
    <div className="App">
        <Header/>

      <main>
          <Switch>
          <Route exact path="/" component={ProductContent} />
          <Route path="/login" component={LoginPage} />
        </Switch>
      </main>

      <Footer year={new Date().getFullYear()}/>
    </div>
    </Router>
  );
}

export default App;
