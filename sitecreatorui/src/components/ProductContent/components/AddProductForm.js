import "./AddProductForm.css"
import AddCircleOutlineRoundedIcon from '@material-ui/icons/AddCircleOutlineRounded';
import {Button} from "@material-ui/core";
import CloseIcon from '@material-ui/icons/Close';
import {Component} from "react";


export class AddProductForm extends Component{

    state = {
        productTitle: '',
        productDescription: '',
        productPrice: ''
    }

    handleProductTitleChange = e => {
        this.setState({
            productTitle: e.target.value
        })

    }

    handleProductDescriptionChange = e => {
        this.setState({
            productDescription: e.target.value
        })

    }

    handleProductPriceChange = e => {
        this.setState({
            productPrice: e.target.value
        })
    }

    createProduct = () => {
        const product = {
            id: this.props.productsArr.length +1,
            title: this.state.productTitle,
            description: this.state.productDescription,
            price: this.state.productPrice,
            in_cart: false,
        }

    console.log(product)
        this.props.addNewBlogProduct(product)
    }





    render() {
    const handleAddFormHide = this.props.handleAddProductFormHide;
    return(
       <>
       <form action="" className="addProductForm" >
            <button className="hideBtn" onClick={handleAddFormHide}><CloseIcon/></button>
           <h2> Сreating a product</h2>
           <div>
               <input
                   className="addFormInput"
                   type="text"
                   name="productTitle"
                   placeholder="Title of product"
                   value={this.state.productTitle}
                   onChange={this.props.handleProductTitleChange}


               />
           </div>
           <div>
               <textarea
                   className="addFormInput"
                   name="productDescription"
                   placeholder="Description of product"
                   value={this.state.productDescription}
                   onChange={this.props.handleProductDescriptionChange}

               />
           </div>

            <div>
               <input
                   className="addFormInput"
                   type="text"
                   name="productPrice"
                   placeholder="Price of product"
           //        value={this.state.productPrice}
                   onChange={this.props.handleProductPriceChange}

               />
           </div>

           <div>
               <Button variant="contained" color="primary" onClick={this.createProduct}> Add product<AddCircleOutlineRoundedIcon/></Button>
           </div>
       </form>
           <div onClick={this.props.handleAddProductFormHide} className="overlay"></div>
       </>
   )
}
}
