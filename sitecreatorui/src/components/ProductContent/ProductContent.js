import {products} from "../../shared/projectData";
import {ProductCard} from "./components/ProductCard";
import {Component} from "react";
import {AddProductForm} from "./components/AddProductForm";
import {Button} from "@material-ui/core";


export class ProductContent extends Component {

    state = {
        showProducts: true,
        showAddProductForm: false,
        productsArr: JSON.parse(localStorage.getItem('blogProducts'))|| products
    };

    orderProduct = id =>{
        const temp = [...this.state.productsArr];
        temp[id].in_cart = !temp[id].in_cart;

        this.setState({
            productsArr:temp
        })

        localStorage.setItem('blogProducts',JSON.stringify(temp))
   }


   deleteProduct = id => {
        if (window.confirm(`Do you really want to delete ${this.state.productsArr[id].title}, with id=${this.state.productsArr[id].id}?`)){
            const temp = [...this.state.productsArr];
            temp.splice(id,1);

            this.setState({
                productsArr:temp
                    })
        localStorage.setItem('blogProducts', JSON.stringify(temp))
        }}
   handleAddProductFormShow = () => {
        this.setState({
            showAddProductForm: true
        });
   }

   handleAddProductFormHide = () => {
        this.setState({
            showAddProductForm: false
        });
   }


   handleEscape = (e) => {
        if (e.key ==='Escape' && this.state.showAddProductForm){
            this.handleAddProductFormHide()
        }
   }

   addNewBlogProduct = (blogProduct) => {

        this.setState((state) => {
            const products = [...state.productsArr];
            products.push(blogProduct);
            localStorage.setItem('blogProducts', JSON.stringify(products))
            return{
                productsArr: products
            }
        })
   }

   componentDidMount() {
        window.addEventListener('keyup', this.handleEscape)
   }

   componentWillUnmount() {
        window.removeEventListener('keyup', this.handleEscape)
   }


    render(){
    const blogProducts = this.state.productsArr.map((item,id) => {
            return (
                <ProductCard
                    id ={item.id}
                    title = {item.title}
                    description = {item.description}
                    price = {item.price}
                    quantityCount={item.quantityCount}
                    orderProduct={() => this.orderProduct(id)}
                    deleteProduct = {() => this.deleteProduct(id)}
                />
            );
        }
    )

        return (
                <div className="productsPage">
                {this.state.showAddProductForm ? (
                  <AddProductForm
                  productsArr={this.state.productsArr}
                  addNewBlogProduct={this.addNewBlogProduct}
                  handleAddFormHide={this.handleAddProductFormHide}
                  />
                    ) : null}
                    <>
                    <h1>Simple ProductCreator</h1>
                    <div className="addNewProduct">
                       <Button variant="contained" color="secondary"
                               onClick={this.handleAddProductFormShow}>
                           Create new product!
                       </Button>
                        </div>
                        <div className="products">{blogProducts}</div>
                        </>
                    </div>
        );
  }
}



