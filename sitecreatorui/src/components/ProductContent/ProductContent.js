import {products} from "../../shared/projectData";
import {ProductCard} from "./components/ProductCard";
import {Component} from "react";
import {AddProductForm} from "./components/AddProductForm";
import {Button} from "@material-ui/core";
import axios from "axios";


export class ProductContent extends Component {

    state = {
        showProducts: true,
        showAddProductForm: false,
//      productsArr: JSON.parse(localStorage.getItem('blogProducts'))|| products
        productsArr: [],
        isPending: false
    };

    orderProduct = id =>{
        const temp = [...this.state.productsArr];
        temp[id].in_cart = !temp[id].in_cart;

        this.setState({
            productsArr:temp
        })

        localStorage.setItem('blogProducts',JSON.stringify(temp))
   }


   deleteProduct = (blogProduct) => {
       if (window.confirm(`Do you really want to delete ${blogProduct.title}?`)) {

           axios.delete(`https://6107ceafd73c6400170d3616.mockapi.io/api/v1/Products/${blogProduct.id}`)
               .then((response) => {
                   console.log('The product was deleted =>', response.data)
                   this.fetchProducts()
               })
               .catch((err) => {
                   console.log(err)
               })


       //     const temp = [...this.state.productsArr];
       //     temp.splice(id,1);

       //     this.setState({
       //         productsArr:temp
       //             })
       // localStorage.setItem('blogProducts', JSON.stringify(temp))
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

        axios.post('https://6107ceafd73c6400170d3616.mockapi.io/api/v1/Products', blogProduct)
            .then((response) => {
                console.log("Product was been created =>", response.data)
                this.fetchProducts()
            })
            .catch((err) =>{
                console.log(err)
            })

   //     this.setState((state) => {
   //         const products = [...state.productsArr];
   //         products.push(blogProduct);
   //         localStorage.setItem('blogProducts', JSON.stringify(products))
   //         return{
   //             productsArr: products
   //         }
   //     })
   };

   fetchProducts = () => {
    this.setState({
       isPending: true
    })
   axios.get('https://6107ceafd73c6400170d3616.mockapi.io/api/v1/Products')
            .then((response) =>{
                this.setState({
                    productsArr:response.data,
                    isPending: false
                })
                console.log(response)
            })
            .catch((err) => {
                console.log(err)
            })
   }


   componentDidMount() {
        this.fetchProducts()
        window.addEventListener('keyup', this.handleEscape);
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
                    deleteProduct = {() => this.deleteProduct(item)}
                />
            );
        }
    )

        if (this.state.productsArr.length === 0)
            return <h1>Loading...</h1>

        return (
                <div className="productsPage">
                {this.state.showAddProductForm && (
                  <AddProductForm
                  productsArr={this.state.productsArr}
                  addNewBlogProduct={this.addNewBlogProduct}
                  handleAddFormHide={this.handleAddProductFormHide}
                  />
                    )}
                    <>
                    <h1>Simple ProductCreator</h1>
                    <div className="addNewProduct">
                       <Button variant="contained" color="secondary"
                               onClick={this.handleAddProductFormShow}>
                           Create new product!
                       </Button>
                        </div>
                        {
                            this.state.isPending && <h1>Please, await</h1>
                        }
                        <div className="products">{blogProducts}</div>
                        </>
                    </div>
        );
  }
}



