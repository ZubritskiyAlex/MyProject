import "./AddProductForm.css"
import AddCircleOutlineRoundedIcon from '@material-ui/icons/AddCircleOutlineRounded';
import {Button} from "@material-ui/core";
import CloseIcon from '@material-ui/icons/Close';
import {Component} from "react";


export class AddProductForm extends Component{
    constructor(props) {
        super(props);
        this.state = {
            productTitle: '',
            productDescription: '',
            productPrice: ''
        }
    this.handleProductTitleChange = this.handleProductTitleChange.bind(this);
    this.handleProductDescriptionChange = this.handleProductDescriptionChange.bind(this);
    this.handleProductPriceChange = this.handleProductPriceChange.bind(this);
    this.createProduct = this.createProduct.bind(this);

    }


//    state = {
//        productTitle: '',
//        productDescription: '',
//        productPrice: ''
//    }

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

    createProduct = (e) => {
        e.preventDefault()
        const product = {
            id: this.props.productsArr.length +1,
            title: this.state.productTitle,
            description: this.state.productDescription,
            price: this.state.productPrice,
            in_cart: false,
        }

    console.log(product)
        this.props.addNewBlogProduct(product)
        this.props.handleAddFormHide()
    }





    render() {
    const handleAddFormHide = this.props.handleAddProductFormHide;
    return(
       <>
       <form className="addProductForm" onSubmit={this.createProduct} >
            <button className="hideBtn" onClick={handleAddFormHide}><CloseIcon/></button>
           <h2> Сreating a product</h2>
           <div>
               <input
                   className="addFormInput"
                   type="text"
                   name="productTitle"
                   placeholder="Title of product"
                   value={this.state.productTitle}
                   onChange={this.handleProductTitleChange}
                   required

               />
           </div>
           <div>
               <textarea
                   className="addFormInput"
                   name="productDescription"
                   placeholder="Description of product"
                   value={this.state.productDescription}
                   onChange={this.handleProductDescriptionChange}
                   required

               />
           </div>

            <div>
               <input
                   className="addFormInput"
                   type="text"
                   name="productPrice"
                   placeholder="Price of product"
                   value={this.productPrice}
                   onChange={this.handleProductPriceChange}
                   required

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
