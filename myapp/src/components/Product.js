import React from 'react';
import {connect} from "react-redux";


const Product = ({product}) => <div>{product.name}</div>;

const mapStateToProps = (state, ownProps) => {
    console.log(ownProps);
    return{
        product: state.products.find(product => product.id === Number(ownProps.params.id))
    };
};

export default  connect()(Product);