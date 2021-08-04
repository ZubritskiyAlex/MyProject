import "./EditProductForm.css"
import SaveIcon from '@material-ui/icons/Save';
import CloseIcon from '@material-ui/icons/Close';
import {Button} from "@material-ui/core";
import {Component} from "react";


export class EditProductForm extends Component{
    constructor(props) {
        super(props);
        this.state = {
            productTitle: this.props.selectedProduct.title,
            productDescription: this.props.selectedProduct.description,
            productPrice:this.props.selectedProduct.price,
        }
    this.handleProductTitleChange = this.handleProductTitleChange.bind(this);
    this.handleProductDescriptionChange = this.handleProductDescriptionChange.bind(this);
    this.handleProductPriceChange = this.handleProductPriceChange.bind(this);
    this.saveProduct = this.saveProduct.bind(this);

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

    saveProduct = (e) => {
        e.preventDefault()
        const product = {
            id: this.props.selectedProduct.id,
            title: this.state.productTitle,
            description: this.state.productDescription,
            price: this.state.productPrice,
            in_cart: false,
        }

//    console.log(product)
        this.props.editBlogProduct(product)
        this.props.handleEditFormHide()
    }




    handleEscape = (e) => {
        if (e.key === "Escape") {
            this.props.handleEditProductFormHide();
        }
    };

    componentDidMount() {
        window.addEventListener('keyup', this.handleEscape)
    }

    componentWillUnmount() {
        window.removeEventListener('keyup', this.handleEscape)
    }





    render() {
    const handleEditFormHide = this.props.handleEditProductFormHide;
    return(
       <>
       <form className="editProductForm" onSubmit={this.saveProduct}>
            <button className="hideBtn" onClick={handleEditFormHide}><CloseIcon/></button>
           <h2> Edit a product</h2>
           <div>
               <input
                   className="editFormInput"
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
                   className="editFormInput"
                   name="productDescription"
                   placeholder="Description of product"
                   value={this.state.productDescription}
                   onChange={this.handleProductDescriptionChange}
                   required

               />
           </div>

            <div>
               <input
                   className="editFormInput"
                   type="text"
                   name="productPrice"
                   placeholder="Price of product"
                   value={this.productPrice}
                   onChange={this.handleProductPriceChange}
                   required

               />
           </div>
           <div>
               <Button variant="contained" color="primary"> Save <SaveIcon/></Button>
           </div>
       </form>
           <div onClick={this.props.handleEditFormHide} className="overlay"></div>
       </>
   )
}
}
