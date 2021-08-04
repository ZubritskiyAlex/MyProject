import {products, productsApiURL} from "../../shared/projectData";
import {ProductCard} from "./components/ProductCard";
import {Component} from "react";
import {AddProductForm} from "./components/AddProductForm";
import {Button, CircularProgress} from "@material-ui/core";
import axios from "axios";
import {EditProductForm} from "./components/EditProductForm";


export class ProductContent extends Component {

    state = {
        showProducts: true,
        showAddProductForm: false,
//      productsArr: JSON.parse(localStorage.getItem('blogProducts'))|| products
        productsArr: [],
        isPending: false,

    };

    orderProduct = (blogProduct) =>{

        const temp = {...blogProduct};
        temp.in_cart = !temp.in_cart

        axios.put(`${productsApiURL}${blogProduct.id}`, temp)
            .then((response) =>{
                console.log("order edit", response.data);
                this.fetchProducts();
            })
            .catch((err) => {
                console.log(err)

        })




    // add product to cart
    //    const temp = [...this.state.productsArr];
    //    temp[id].in_cart = !temp[id].in_cart;

    //    this.setState({
    //        productsArr:temp
    //    })

    //    localStorage.setItem('blogProducts',JSON.stringify(temp))
   }


   deleteProduct = (blogProduct) => {
       if (window.confirm(`Do you really want to delete ${blogProduct.title}?`)) {
           this.setState({
       isPending: true
    })

           axios.delete(`${productsApiURL}${blogProduct.id}`)
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

   handleEditProductFormShow = () => {
        this.setState({
            showEditProductForm: true,
        });
   }

   handleEditProductFormHide = () => {
        this.setState({
            showEditProductForm: false,
        });
   }



   handleEscape = (e) => {
        if (e.key ==='Escape' && this.state.showAddProductForm){
            this.handleAddProductFormHide()
        }
   }

   addNewBlogProduct = (blogProduct) => {
        this.setState({
       isPending: true
    })

        axios.post(productsApiURL, blogProduct)
            .then((response) => {
                console.log("Product was been created =>", response.data)
                this.fetchProducts()
            })
            .catch((err) =>{
                console.log(err)
            })
       };



   editBlogProduct = (updatedBlogProduct) => {
       this.setState({
           isPending: true,
       });
       axios.put(`${productsApiURL}${updatedBlogProduct.id}`,updatedBlogProduct)
           .then((response) =>{
               console.log("Product was been changed",response.data);
               this.fetchProducts();
           })
           .catch((err) => {
               console.log(err);
           });
   }

   //     this.setState((state) => {
   //         const products = [...state.productsArr];
   //         products.push(blogProduct);
   //         localStorage.setItem('blogProducts', JSON.stringify(products))
   //         return{
   //             productsArr: products
   //         }
   //     })


   fetchProducts = () => {

   axios.get(productsApiURL)
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

   handleSelectProduct = (blogProduct) => {
       this.setState({
           selectedProduct: blogProduct
       })
   }


   componentDidMount() {
        this.fetchProducts();
   }


    render(){
    const blogProducts = this.state.productsArr.map((item) => {
            return (
                <ProductCard
                    id ={item.id}
                    title = {item.title}
                    description = {item.description}
                    price = {item.price}
                    quantityCount={item.quantityCount}
                    orderProduct={() => this.orderProduct(item)}
                    deleteProduct = {() => this.deleteProduct(item)}
                    handleEditFormShow = {this.handleEditProductFormShow}
                    handleSelectProduct = {() => this.handleSelectProduct(item)}

                />
            );
        }
    )

        if (this.state.productsArr.length === 0)
            return <h1>Loading...</h1>



        const productsOpacity = this.state.isPending ? 0.5 : 1


        return (
                <div className="productsPage">
                {this.state.showAddProductForm && (
                  <AddProductForm
                      productsArr={this.state.productsArr}
                      addNewBlogProduct={this.addNewBlogProduct}
                      handleAddFormHide={this.handleAddProductFormHide}
                  />
                    )}

                    {
                        this.state.showEditProductForm && (
                            <EditProductForm
                            handleEditFormHide={this.handleEditProductFormHide}
                            selectedProduct={this.state.selectedProduct}
                            editBlogProduct = {this.editBlogProduct}
                            />
                        )
                    }

                    <>
                    <h1>Simple ProductCreator</h1>
                    <div className="addNewProduct">
                       <Button variant="contained" color="secondary"
                               onClick={this.handleAddProductFormShow}>
                           Create new product!
                       </Button>
                        </div>

                        <div className="products" style={{opacity: productsOpacity}}>
                            {blogProducts}
                        </div>
                            {this.state.isPending && <CircularProgress color="secondary" className="preloader" /> }
                        </>
                    </div>
        );
  }
}



