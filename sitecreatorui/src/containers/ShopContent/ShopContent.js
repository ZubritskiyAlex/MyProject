import {shopsApiURL} from "../../shared/projectData";
import {ShopCard} from "./components/ShopCard";
import {Component} from "react";
import {AddShopForm} from "./components/AddShopForm";
import {Button, CircularProgress} from "@material-ui/core";
import axios from "axios";
import {EditShopForm} from "./components/EditShopForm";



export class ShopContent extends Component {

    state = {
        showShops: true,
        showAddShopForm: false,
        shopsArr: [],
        isPending: false,

    };

    fetchShops = () => {
    source=axios.CancelToken.source();
    axios.get(shopsApiURL)
            .then((response) =>{
                this.setState({
                    shopsArr:response.data,
                    isPending: false
                })
                console.log(response)
            })
            .catch((err) => {
                console.log(err)
            })
   }


   componentDidMount() {
        this.fetchShops();
   }

   componentWillUnmount() {
        if(source){
            source.cancel('Axios get canceled')
        }
   }


   deleteShop = (blogShop) => {
       if (window.confirm(`Do you really want to delete ${blogShop.title}?`)) {
           this.setState({
       isPending: true
    })

           axios.delete(`${shopsApiURL}${blogShop.id}`)
               .then((response) => {
                   console.log('The product was deleted =>', response.data)
                   this.fetchProducts()
               })
               .catch((err) => {
                   console.log(err)
               })
       }}


    handleAddShopFormShow = () => {
        this.setState({
            showAddShopForm: true
        });
   }

   handleAddShopFormHide = () => {
        this.setState({
            showAddShopForm: false
        });
   }

   handleEditShopFormShow = () => {
        this.setState({
            showEditShopForm: true,
        });
   }

   handleEditShopFormHide = () => {
        this.setState({
            showEditShopForm: false,
        });
   }

   handleEscape = (e) => {
        if (e.key ==='Escape' && this.state.showAddShopForm){
            this.handleAddProductFormHide()
        }
   }

   addNewBlogProduct = (blogShop) => {
        this.setState({
       isPending: true
    })

        axios.post(shopsApiURL, blogShop)
            .then((response) => {
                console.log("Product was been created =>", response.data)
                this.fetchShops()
            })
            .catch((err) =>{
                console.log(err)
            })
       };



   editBlogShop = (updatedBlogShop) => {
       this.setState({
           isPending: true,
       });
       axios.put(`${shopsApiURL}${updatedBlogShop.id}`,updatedBlogShop)
           .then((response) =>{
               console.log("Product was been changed",response.data);
               this.fetchShops();
           })
           .catch((err) => {
               console.log(err);
           });
   }


   handleSelectProduct = (blogShop) => {
       this.setState({
           selectedProduct: blogShop
       })
   }

    render(){
    const blogShops = this.state.productsArr.map((item) => {
            return (
                <ShopCard
                    id ={item.id}
                    title = {item.title}
                    description = {item.description}
                    deleteShop = {() => this.deleteShop(item)}
                    handleEditFormShow = {this.handleEditShopFormShow}
                    handleSelectShop = {() => this.handleSelectShop(item)}

                />
            );
        }
    )

        if (this.state.shopsArr.length === 0)
            return <h1>Loading...</h1>



        const shopsOpacity = this.state.isPending ? 0.5 : 1


        return (
                <div className="productsPage">
                {this.state.showAddShopForm && (
                  <AddShopForm
                      shopsArr={this.state.productsArr}
                      addNewBlogShop={this.addNewBlogProduct}
                      handleAddFormHide={this.handleAddShopFormHide}
                  />
                    )}

                    {
                        this.state.showEditShopForm && (
                            <EditShopForm
                            handleEditFormHide={this.handleEditShopFormHide}
                            selectedShop={this.state.selectedShop}
                            editBlogShop = {this.editBlogShop}
                            />
                        )
                    }

                    <>
                    <h1>Simple ShopCreator</h1>
                    <div className="addNewProduct">
                       <Button variant="contained" color="secondary"
                               onClick={this.handleAddShopFormShow}>
                           Create new Shop!
                       </Button>
                        </div>

                        <div className="products" style={{opacity: shopsOpacity}}>
                            {blogShops}
                        </div>
                            {this.state.isPending && <CircularProgress color="secondary" className="preloader" /> }
                        </>
                    </div>
        );
  }
}