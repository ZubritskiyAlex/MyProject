import React from 'react';

class EditProduct extends React.Component{
    constructor(props) {
        super(props);
        const {id, name, price} = props.location.state.product;
        this.state = {
            id,
            name,
            price,
        };
    }

    update = (e) => {
        e.preventDefault();
        if(this.state.name ==="" && this.state.price ===""){
            alert("All the fields are mandatory")
            return;
        }
        this.props.updateProductHandler(this.state);
        this.setState({name: "",  price: "", description:"", shop: ""})
        this.props.history.push("/");
    };
    render() {
        return(
            <div className='ui main'>
                <h2>Edit product!</h2>
                <form className='ui form' onSubmit={this.update}>
                    <div className="field">
                        <label>Product name:    </label>
                        <input type="text"
                               name="name"
                               placeholder="Enter the product name"
                               value={this.state.name}
                               onChange={(e) =>this.setState({name:e.target.value})}

                        />
                    </div>

                    <div className="field">
                        <label>Price:   </label>
                        <input type="text"
                               name="price"
                               placeholder="Enter the price"
                               value={this.state.price}
                               onChange={(e) =>this.setState({price:e.target.value})}
                        />
                    </div>

                    <div className="field">
                        <label>Store:   </label>
                        <input type="text"
                               name="name"
                               placeholder="Enter the name of store"
                               value={this.state.shop}
                               onChange={(e) =>this.setState({shop:e.target.value})}
                        />
                    </div>

                    <div className="field">
                        <label>Description: </label>
                        <input type="text" name="name" placeholder="Create description for product!"/>
                    </div>
                    <button className='ui button blue'> Update! </button>


                </form>

            </div>

        );

    }

}

export default EditProduct;