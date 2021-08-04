import ProductForm from "./components/ProductForm";
import Products from "./components/Products";
import FetchedProducts from "./components/FetchedProducts";

function App() {
  return (
    <div className="container pt-3">
        <div className="row">
            <div className="col">
                <ProductForm/>
            </div>
        </div>
        <div className="row">
            <div className="col">
                <h2>Sync products</h2>
                <Products />
            </div>
            <div className="col">
                <h2>Async products</h2>
                <FetchedProducts products={[]}/>
            </div>
        </div>
    </div>
  );
}

export default App;
