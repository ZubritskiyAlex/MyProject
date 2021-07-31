import './App.css';
import {Header} from "./components/Header";
import {Footer} from "./components/Footer/Footer";
import {ProductContent} from "./components/ProductContent/ProductContent";

function App() {
  return (
    <div className="App">
      <Header/>

      <main>
          <ProductContent />
      </main>

      <Footer year={new Date().getFullYear()}/>
    </div>
  );
}

export default App;
